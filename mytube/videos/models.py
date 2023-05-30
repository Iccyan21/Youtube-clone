from django.db import models
from accounts.models import User
import uuid

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)  # 再生回数のフィールドを追加する

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:50]}"

    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.video.id)])
