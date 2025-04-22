from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
   

    def publish(self):
        """Sets the published_at date to now."""
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        """String representation of the Post object."""
        return self.title

    class Meta:
        ordering = ['-published_at', '-created_at'] 
