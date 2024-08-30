from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def copy(self):
        new_post = BlogPost()
        new_post.title = self.title
        new_post.body = self.body
        new_post.author = self.author
        new_post.data_created = timezone.now()
        new_post.save()
        for comment in Comment.objects.filter(blog_post=self):
            new_comment = Comment()
            new_comment.text = comment.text
            new_comment.blog_post = new_post
            new_comment.save()
        return new_post.pk


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
