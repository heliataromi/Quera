from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from blog.models import Post
from blog.forms import PostCreateForm

class PostListCreateView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super(PostListCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_queryset(self):
        return Post.objects.all()

    def get_form(self):
        if self.request.method == 'POST':
            form = PostCreateForm(self.request.POST)
        else:
            form = PostCreateForm()
        return form

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "پست جدید با موفقیت ساخته شد ✨")
            form.save()
            return redirect('blog:post_list')

        messages.add_message(request,
                             messages.ERROR,
                             "لطفاً خطاهای فرم را برطرف کنید."
                             )
        return self.render_to_response(self.get_context_data(form=form))

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'