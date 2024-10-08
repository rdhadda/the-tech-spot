from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserProfileForm


class TestProfile(TestCase):

    def setUp(self):
        """
        Set up a test user with a UserProfile and log
        them in for the test case.
        """
        # Create a user and associate it with a UserProfile
        self.user = User.objects.create_user(username='testdjangouser',
                                             password='password123')
        self.profile = self.user.userprofile

        # Log the user in
        self.client.login(username='testdjangouser', password='password123')

    def test_get_profile(self):
        """ Test GET request to profile view """
        response = self.client.get(reverse('profile'))

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'profiles/profile.html')

        # Check if the form in the context is the correct form
        self.assertIsInstance(response.context['form'], UserProfileForm)

    def test_post_valid_profile_update(self):
        """ Test POST request with valid form data """
        post_data = {
            'default_phone_number': '1234567890',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Test 1',
            'default_town_or_city': 'Test City',
            'default_postcode': '12345',
            'default_country': 'GB',
            'default_county': 'Test County'
        }

        self.client.post(reverse('profile'), post_data)       

        # Check if the profile is updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '1234567890')
