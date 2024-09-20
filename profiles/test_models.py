from django.test import TestCase
from django.contrib.auth.models import User


class TestUserProfileModel(TestCase):

    def setUp(self):
        # Create a user and user profile
        self.user = User.objects.create_user(username='testuser',
                                             password='password123')
        self.profile = self.user.userprofile

    def test_userprofile_str(self):
        """ Test the __str__ method of the UserProfile model """
        self.assertEqual(str(self.profile), 'testuser')
