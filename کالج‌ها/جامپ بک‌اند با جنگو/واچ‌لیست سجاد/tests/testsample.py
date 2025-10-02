from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from watchlist.models import WatchItem


class WatchItemModelTest(TestCase):
    def test_create_watch_item(self):
        item = WatchItem.objects.create(
            title="The Dark Knight",
            type="M",
        )
        self.assertEqual(str(item), "The Dark Knight")
        self.assertFalse(item.is_watched)
        self.assertIsNone(item.url)


class WatchItemListCreateViewTest(TestCase):
    def setUp(self) -> None:
        i1 = WatchItem.objects.create(title="The Avengers", type="M")
        i2 = WatchItem.objects.create(title="Superman", type="M")
        i3 = WatchItem.objects.create(title="Ironheart", type="S")
        i4 = WatchItem.objects.create(title="Arrow", type="S")
        self.items = [i1, i2, i3, i4]

    def test_get_watchlist_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_create.html")
        self.assertCountEqual(response.context["items"], self.items)

    def test_post_watch_item(self):
        data = {
            "title": "Avengers: Endgame",
            "type": "M",
            "url": "https://example.com"
        }
        poster = SimpleUploadedFile("poster.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post("/", data | {"poster": poster}, follow=True)
        context = response.context
        
        self.assertTrue(WatchItem.objects.filter(title="Avengers: Endgame").exists())
        self.assertTemplateUsed(response, "list_create.html")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(context["message"], "آیتم جدید با موفقیت اضافه شد!")
        self.assertCountEqual(context["items"], [WatchItem.objects.get(title="Avengers: Endgame")] + self.items)
