from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name="BoardList"),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name="TopicList"),
    path('boards/<int:pk>/new/', views.TopicCreateView.as_view(), name="NewTopic"),
    path('boards/<int:pk>/topics/<int:topic_pk>/',
         views.TopicPostsView.as_view(), name="TopicPosts"),
    path('boards/<int:pk>/topics/<int:topic_pk>/edit/<int:post_pk>/',
         views.PostUpdateView.as_view(), name="PostUpdate"),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/',
         views.PostReplyView.as_view(), name="PostReply"),
]
