from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    preview_image = models.ImageField(upload_to='blog_previews/', null=True, blank=True, verbose_name="Blog previews")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at")
    is_published = models.BooleanField(default=False, verbose_name="Publication flag")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Views count")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"
        ordering = ['-created_at']