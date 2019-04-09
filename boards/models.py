from django.db import models
from django.db.models import Count
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

    def get_topic_count(self):
        return Topic.objects.filter(board=self).count()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def get_reply_count(self):
        return Post.objects.filter(topic=self).count()-1

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ("-last_updated",)


class Post(models.Model):
    message = RichTextUploadingField()
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.message[:30]

    class Meta:
        ordering = ("-created_at",)
