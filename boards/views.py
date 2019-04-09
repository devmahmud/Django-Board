from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TopicCreateForm, PostCreateForm
from .models import Board, Topic, Post


class BoardListView(ListView):
    template_name = "boards/board_list.html"
    model = Board
    paginate_by = 8


class TopicListView(ListView):
    template_name = "boards/topic_list.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board"] = get_object_or_404(Board,pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = Topic.objects.filter(board__id=self.kwargs['pk'])
        return queryset


class TopicCreateView(LoginRequiredMixin, FormView):
    form_class = TopicCreateForm
    template_name = "boards/new_topic.html"

    def form_valid(self, form):
        topic = form.cleaned_data.get('topic')
        message = form.cleaned_data.get('message')
        board = get_object_or_404(Board, pk=self.kwargs['pk'])
        new_topic = Topic.objects.create(
            subject=topic, board=board, starter=self.request.user)
        new_post = Post.objects.create(
            message=message, topic=new_topic, created_by=self.request.user)

        return redirect('TopicList', self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = get_object_or_404(Board, pk=self.kwargs['pk'])
        return context


class TopicPostsView(DetailView):
    model = Topic
    template_name = "boards/topic_posts.html"

    def get_object(self):
        self.topic = get_object_or_404(
            Topic, board__pk=self.kwargs['pk'], pk=self.kwargs['topic_pk'])
        
        return self.topic

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk) # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here
        return super().get_context_data(**kwargs)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['message']
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'
    template_name = "boards/update_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('TopicPosts', pk=post.topic.board.pk, topic_pk=post.topic.pk)


class PostReplyView(LoginRequiredMixin,CreateView):
    template_name = "boards/reply_topic.html"
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.topic = get_object_or_404(
            Topic, pk=self.kwargs['topic_pk'])
        instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('TopicPosts', kwargs={'pk': self.kwargs['pk'], 'topic_pk': self.kwargs['topic_pk']})
