from django.test import TestCase
from django.contrib.auth import get_user_model

from supplai_api.apps.transaction import models

def sample_user(username="someuser", first_name="Some",
                last_name="User", password="anypassword"):
    return get_user_model().objects.create_user(
        username, first_name, last_name, password
    )

class TransactionModelTest(TestCase):
    def test_saving_and_retriving_transaction(self):
        """Test that can saving and retriving transaction"""

        transaction = models.Transaction.objects.create(
            type="E",
            value="100.00",
            user=sample_user()
        )

        self.assertEqual(str(transaction), transaction.value)
