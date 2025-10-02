from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from blog.models import Post


class PostViewsSampleTests(TestCase):
    fixtures = ('posts.json', )

    @classmethod
    def setUpTestData(cls):
        cls.list_url = reverse('blog:post_list')
        cls.detail_url = lambda pk: reverse('blog:post_detail', args=[pk])

    def setUp(self):
        self.client = Client()

    def test_list_get_status_code_ok(self):
        res = self.client.get(self.list_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_list.html')

    def test_list_get_context_contains_posts_and_form(self):
        res = self.client.get(self.list_url)
        self.assertIn('posts', res.context)
        self.assertIn('form', res.context)

    def test_list_post_valid_creates_post_and_redirects(self):
        payload = {
            'title': 'New Post',
            'category': 'coding',
            'content': 'Some content',
        }
        res = self.client.post(self.list_url, data=payload, follow=False)
        self.assertEqual(res.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post', author__isnull=True).exists())
        msgs = [f'{m.level_tag}:{m.message}' for m in get_messages(res.wsgi_request)]
        self.assertEqual(msgs[0], 'success:پست جدید با موفقیت ساخته شد ✨')

    def test_list_post_invalid_shows_errors_and_renders_same_template(self):
        payload = {
            'title': '',
            'author': 'A',
            'category': 'coding',
            'content': '...',
        }
        res = self.client.post(self.list_url, data=payload, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_list.html')

        self.assertIn('form', res.context)
        self.assertTrue(res.context['form'].errors)

        msgs = [f'{m.level_tag}:{m.message}' for m in get_messages(res.wsgi_request)]
        self.assertEqual(msgs[0], 'error:لطفاً خطاهای فرم را برطرف کنید.')

    def test_detail_get_status_code_ok(self):
        url = self.detail_url(1)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_detail.html')

    def test_detail_404_when_not_found(self):
        url = self.detail_url(999999)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)
