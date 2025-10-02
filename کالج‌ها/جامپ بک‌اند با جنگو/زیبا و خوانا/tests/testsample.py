from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from bs4 import BeautifulSoup

from blog.models import Post


class TestSampleTests(TestCase):
    def setUp(self):
        now = timezone.now()
        Post.objects.create(title="post 1", author="a", category="category a", content="This is a test content for first post.", rate=5, created_at=now - timezone.timedelta(days=1))
        Post.objects.create(title="post 2", author=None, category="category b", content="Second post content is a bit longer and has enough words to test truncation.", rate=None, created_at=now - timezone.timedelta(hours=10))
        Post.objects.create(title="post 3", author="b", category="category a", content="Life post content here. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", rate=0, created_at=now - timezone.timedelta(days=7))
        Post.objects.create(title="post 4", author="c", category="category c", content="another post content here.", rate=3, created_at=now - timezone.timedelta(days=31))
        self.posts = Post.objects.order_by('-created_at')
        self.url = reverse("post_list")
    
    def test_response_status_and_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_page_title_and_minimum_post_presence(self):
        """Page title should be correct and at least one post displayed."""
        response = self.client.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
    
        self.assertEqual("Blog Posts", soup.title.text.strip())

        posts = soup.select("article.post-card")
        n = self.posts.count()
        self.assertEqual(len(posts), n, f"{n} posts should be rendered on the page")


    def test_categories_and_post_basic_elements(self):
        """Categories should be displayed, and each post must have title, category and 'Read More' link."""
        response = self.client.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        categories = soup.select("h2.category-title")
        n = len(set(self.posts.values_list('category', flat=True)))
        self.assertEqual(len(categories), n, "There should be {n} category title displayed")
        
        posts = soup.select("article.post-card")
        categories = [cat.text.strip() for cat in soup.select("h2.category-title")]
        titles, links = [], []
        for post in posts:
            titles.append(post.select_one("h2.post-title").text.strip())
            links.append(post.select_one("a.read-more").get("href"))

        titles.sort()
        categories.sort()
        links.sort()

        expected_titles = sorted(map(lambda x: x.title(), self.posts.values_list('title', flat=True)))
        expected_categories = sorted(map(lambda x: x.title(), list(set(self.posts.values_list('category', flat=True)))))
        expected_links = sorted([reverse('post_detail', args=[post.id]) for post in self.posts])
        
        self.assertEqual(titles, expected_titles)
        self.assertEqual(categories, expected_categories)
        self.assertEqual(links, expected_links)



    def test_post_metadata_and_content_length(self):
        """Each post should display author, timesince, rate, and content length should not exceed 150 characters."""
        response = self.client.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        posts = soup.select("article.post-card")
        authors, timesinces, rates, contents = [], [], [], []
        for post in posts:
            authors.append(post.select_one("span.post-author").text.strip())
            timesinces.append(post.select_one("span.post-time-since").text.strip().replace('\xa0', ' '))
            rates.append(post.select_one("span.post-rate").text.strip())
            contents.append(len(post.select_one("p.post-content").text.strip()))

        authors.sort()
        timesinces.sort()
        rates.sort()
        contents.sort()

        expected_authors = sorted(['✍ a', '✍ b', '✍ Anonymous', '✍ c'])
        expected_timesinces = sorted(['⏳ 1 day ago', '⏳ 1 week ago', '⏳ 10 hours ago', '⏳ 1 month ago'])
        expected_rates = sorted(['⭐ 5', '⭐ 0', '⭐ No rating', '⭐ 3'])
        expected_contents = sorted([38, 150, 76, 26])

        self.assertListEqual(authors, expected_authors)
        self.assertListEqual(timesinces, expected_timesinces)
        self.assertListEqual(rates, expected_rates)
        self.assertListEqual(contents, expected_contents)
