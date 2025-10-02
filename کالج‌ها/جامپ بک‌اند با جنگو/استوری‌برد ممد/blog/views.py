from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from blog.models import Post
from blog.forms import PostCreateForm

class PostListCreateView(View):
    def get(self, request):
        queryset = Post.objects.all()
        form = PostCreateForm()
        context = {
            'posts': queryset,
            'form': form,
        }
        return render(request, 'blog/post_list.html', context)

    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "پست جدید با موفقیت ساخته شد ✨")
            form.save()
            return redirect('blog:post_list')

        queryset = Post.objects.all()
        context = {
            'posts': queryset,
            'form': form,
        }
        messages.add_message(request,
                             messages.ERROR,
                             "لطفاً خطاهای فرم را برطرف کنید."
        )
        return render(request, 'blog/post_list.html', context)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog/post_detail.html', context)
