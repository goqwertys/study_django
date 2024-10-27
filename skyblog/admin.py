from django.contrib import admin

from skyblog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview_image', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content', )
    ordering = ('-created_at', )
