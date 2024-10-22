from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from skyblog.models import BlogPost


# Create your views here.
class BaseView(TemplateView):
    """ Base page """
    template_name = 'skyblog/base.html'


class HomePostListView(ListView):
    """ Home page with the five latest blog posts """
    model = BlogPost
    template_name = 'skyblog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)[:5]


class PostListView(ListView):
    """ List of all the posts """
    model = BlogPost
    template_name = 'skyblog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Page for creating a post """
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    template_name = 'skyblog/form_post.html'
    success_url = reverse_lazy('skyblog:on_moderation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'New Post'
        return context


class EditPostView(LoginRequiredMixin, UpdateView):
    """ Page og editing post """
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    template_name = 'skyblog/form_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Post'
        return context

    def get_success_url(self):
        post = self.get_object()
        return reverse('skyblog:post_detail', kwargs={'pk': post.pk})


class OnModerationView(TemplateView):
    """ Success page for Create and Edit """
    template_name = 'skyblog/on_moderation.html'


class BlogPostDetailView(DetailView):
    """ Page for detailed viewing of the post """
    model = BlogPost
    template_name = 'skyblog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()

        return obj


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ Page for deleting post """
    model = BlogPost
    template_name = 'skyblog/post_confirm_delete.html'
    success_url = reverse_lazy('skyblog:post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.title
        return context
