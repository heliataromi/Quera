from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from blog.models import Post


class TestSampleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = Post.objects.create(title='T', author='A', category='C', content='text')
        self.post_create_url = reverse('blog:post_create')
        self.post_update_url = reverse('blog:post_update', args=[self.obj.pk])
        self.post_delete_url = reverse('blog:post_delete', args=[self.obj.pk])

    def test_post_create_view_get_renders_form_and_mode_create(self):
        res = self.client.get(self.post_create_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_form.html')
        self.assertIn('form', res.context)
        self.assertEqual(res.context.get('mode'), 'create')

    def test_post_create_view_valid_form(self):
        payload = {
            'title': 'Created by CBV',
            'author': 'MMD',
            'category': 'coding',
            'content': 'hello world',
        }
        res = self.client.post(self.post_create_url, data=payload, follow=True)
        self.assertEqual(res.status_code, 200)

        obj = Post.objects.get(title='Created by CBV')
        self.assertTemplateUsed(res, 'blog/post_detail.html')
        self.assertEqual(res.context['post'].pk, obj.pk)

        msgs = [f'{m.level_tag}:{m.message}' for m in get_messages(res.wsgi_request)]
        self.assertTrue(any(m.startswith('success:') for m in msgs))

    def test_post_update_view_get_renders_prefilled_form_and_mode_update(self):
        res = self.client.get(self.post_update_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_form.html')
        self.assertIn('form', res.context)
        self.assertEqual(res.context.get('mode'), 'update')
        self.assertEqual(res.context['form'].initial.get('title') or res.context['form'].data.get('title'), 'T')

    def test_post_update_view_valid_form(self):
        payload = {
            'title': 'T (edited)',
            'author': 'A',
            'category': 'C',
            'content': 'updated',
        }
        res = self.client.post(self.post_update_url, data=payload, follow=True)
        self.assertEqual(res.status_code, 200)
        self.obj.refresh_from_db()
        self.assertEqual(self.obj.title, 'T (edited)')

        self.assertTemplateUsed(res, 'blog/post_detail.html')
        self.assertEqual(res.context['post'].pk, self.obj.pk)

        msgs = [f'{m.level_tag}:{m.message}' for m in get_messages(res.wsgi_request)]
        self.assertTrue(any(m.startswith('success:') for m in msgs))

    def test_post_delete_view_renders_confirm_template(self):
        res = self.client.get(self.post_delete_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blog/post_confirm_delete.html')

        self.assertIn('object', res.context)
        self.assertEqual(res.context['object'].pk, self.obj.pk)

    def test_post_delete_view_deletes_object(self):
        res = self.client.post(self.post_delete_url, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertFalse(Post.objects.filter(pk=self.obj.pk).exists())

        self.assertTemplateUsed(res, 'blog/post_list.html')

        msgs = [f'{m.level_tag}:{m.message}' for m in get_messages(res.wsgi_request)]
        title = self.obj.title
        self.assertTrue(any(m == f'success:پست «{title}» حذف شد.' for m in msgs))
