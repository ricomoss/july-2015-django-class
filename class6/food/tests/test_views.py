from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class MealListViewTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_get(self):
        resp = self.c.get(reverse('food:meals'))
        expected_result = 200
        self.assertEqual(resp.status_code, expected_result)
