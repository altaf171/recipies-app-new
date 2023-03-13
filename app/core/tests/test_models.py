"""

Test for models


"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """
    Test models.

    """

    def test_create_user_with_email_successful(self):
        """
        Test that user model creation is successful with email.

        """

        email = "test@example.com"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """
        Test that new user email is  normalized.

        """

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'Sample@123')

            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """
        Test that creating new user without email address raises ValueError.

        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        """
        test creating superuser.

        """
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'sample123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)