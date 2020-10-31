from django.test import TestCase

from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    def test_create_user_successful(self):
        username = 'admin'
        password = 'somepassword'
        user_info = dict(first_name='Admin', last_name='User', phone='11-11111111')
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            **user_info
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user_info['first_name'], user.first_name)
        self.assertEqual(user_info['last_name'], user.last_name)
        self.assertTrue(user.check_password(password))

    def test_create_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'somepassword')
