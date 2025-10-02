from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView

from blog.models import Post
from blog.forms import PostCreateForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.save()
        messages.success(self.request, f'پست «{post.title}» با موفقیت ایجاد شد ✨')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'اطلاعات فرم نامعتبر است. لطفاً دوباره بررسی کنید.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create'
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        post = form.save()
        messages.success(self.request, f'پست «{post.title}» با موفقیت ویرایش شد ✨')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'اطلاعات فرم نامعتبر است. لطفاً دوباره بررسی کنید.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'update'
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'

    def get_success_url(self):
        title = self.get_object().title
        messages.success(self.request, f'پست «{title}» حذف شد.')
        return reverse_lazy('blog:post_list')
