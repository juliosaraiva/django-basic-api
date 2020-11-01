from django.test import TestCase

from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    def test_create_user_successful(self):
        user_info = dict(username="admin", password="somepassword",
        first_name='Admin', last_name='User', phone='11-11111111')
        user = get_user_model().objects.create_user(**user_info)

        self.assertEqual(user.username, user_info['username'])
        self.assertEqual(user_info['first_name'], user.first_name)
        self.assertEqual(user_info['last_name'], user.last_name)
        self.assertTrue(user.check_password(user_info['password']))

    def test_create_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'somepassword', last_name=None)
