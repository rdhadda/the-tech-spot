from django.test import TestCase


class TestContactViews(TestCase):

    def test_get_contact_page(self):
        """
        Test that the contact page loads 
        successfully and uses the correct template.

        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
