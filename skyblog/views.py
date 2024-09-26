from django.shortcuts import render
from django.views.generic import ListView

from skyblog.models import BlogPost


# Create your views here.
class HomePostListView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.all()[:5]
