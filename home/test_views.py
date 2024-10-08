from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        """
        Test that the home page loads
        successfully and uses the correct template.

        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
