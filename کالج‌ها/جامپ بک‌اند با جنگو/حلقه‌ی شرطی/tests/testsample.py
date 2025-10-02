from django.test import TestCase
from django.urls import reverse

from datetime import date

from events.models import Event

class TestSampleTest(TestCase):
    fixtures = ('events.json', )

    def test_event_title_current_year(self):
        current_year = date.today().year
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"رویدادهای سال {current_year}")

    def test_event_list_displays_events(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "دورهمی حضوری")
        self.assertContains(response, "هوش مصنوعی")
        self.assertContains(response, "بدون توضیح")
        self.assertContains(response, "ماه: January", count=1)

    def test_event_list_empty_message(self):
        Event.objects.all().delete()
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "هیچ رویدادی یافت نشد.")
