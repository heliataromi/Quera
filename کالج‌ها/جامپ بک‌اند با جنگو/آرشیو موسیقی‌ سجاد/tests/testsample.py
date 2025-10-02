import uuid

from django.conf import settings
from django.urls import get_resolver
from django.test import SimpleTestCase, TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile

from musify.models import Music, Singer


def serialize_music(music):
    return {
        "id": music.id,
        "title": music.title,
        "singer": {
            "id": music.singer.id,
            "name": music.singer.name,
        },
        "description": music.description,
        "year": int(music.year),
        "file": music.file.url if music.file else None
    }

def random_name():
    return f"{uuid.uuid4().hex}.mp3"

class MusicViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_client = APIClient()
        self.singer = Singer.objects.create(name="Googoosh")
        self.music = Music.objects.create(
            title="Behesht",
            description="A classic track",
            year=1975,
            singer=self.singer,
        )

    def test_list_view_returns_music_list(self):
        response = self.client.get("/musics/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Behesht")

    def test_list_view_filter_by_title(self):
        response = self.client.get("/musics/?title=beh")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_view1_invalid_request_method(self):
        for method in ['delete', 'put', 'patch']:
            response = getattr(self.client, method)('/musics/')
            self.assertEqual(response.status_code, 405)

    def test_retrieve_music(self):
        response = self.client.get(f"/musics/{self.music.id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_data = serialize_music(self.music)
        self.assertDictEqual(data, expected_data)

    def test_delete_music(self):
        response = self.client.delete(f"/musics/{self.music.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Music.objects.filter(id=self.music.id).exists())

    def test_delete_nonexistent_music(self):
        response = self.client.delete(f"/musics/999/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "Music not found.")


    def test_view2_invalid_request_method(self):
        for method in ['head', 'post']:
            response = getattr(self.client, method)('/musics/0/')
            self.assertEqual(response.status_code, 405)

