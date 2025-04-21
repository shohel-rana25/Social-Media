
from django.db import models
from Accounts.models import ProfileModel 
from django.contrib.auth.models import User


class PostModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='posts')
    caption = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.profile.user.username}'s post"


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} on {self.post.id}'
