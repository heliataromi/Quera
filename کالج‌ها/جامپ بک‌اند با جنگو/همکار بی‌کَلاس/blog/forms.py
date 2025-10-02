from django import forms

from blog.models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'content']
        labels = {
            'title': 'عنوان پست',
            'author': 'نام نویسنده (اختیاری)',
            'category': 'دسته‌بندی',
            'content': 'متن کامل پست',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'ui-input', 'placeholder': 'مثلاً: هک رشد با جنگو'}),
            'author': forms.TextInput(attrs={'class': 'ui-input', 'placeholder': 'اگر ننویسید، Anonymous نمایش داده می‌شود'}),
            'category': forms.TextInput(attrs={'class': 'ui-input', 'placeholder': 'coding / travel / reading یا هرچیز…'}),
            'content': forms.Textarea(attrs={'rows': 6, 'class': 'ui-textarea', 'placeholder': 'اینجا داستان یا آموزش‌تان را بنویسید…'}),
        }
