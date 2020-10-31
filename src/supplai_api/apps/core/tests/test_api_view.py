from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


API_URL = reverse('core:user-list')


class PublicAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_all_users(self):
        res = self.client.get(API_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
