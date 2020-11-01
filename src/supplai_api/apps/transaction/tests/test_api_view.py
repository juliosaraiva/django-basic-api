from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from supplai_api.apps.transaction.models import Transaction
from supplai_api.apps.transaction.api.serializers import TransactionSerializer


TRANSACTIONS_URL = reverse('transaction:transaction-list')


def detail_url(user_id):
    """Return transaction detail URL"""
    return reverse("transaction:transaction-detail", args=[user_id])


class TransactionAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        user_data = {"username": "admin", "password": "somepass",
                     "first_name": "Admin", "last_name": "User"}
        self.user = get_user_model().objects.create_user(**user_data)

    def test_create_and_retrieve_transaction(self):
        payload = {"type": "e", "value": 50, "user": self.user.id}

        res = self.client.post(TRANSACTIONS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        exists = Transaction.objects.filter(
            user=self.user,
            value=payload['value']
        ).exists()

        self.assertTrue(exists)
