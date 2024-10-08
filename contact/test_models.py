from django.test import TestCase
from .models import Contact


class TestContactModels(TestCase):

    def test_string_representation(self):
        """ Test the string representation of the Contact model."""
        contact = Contact(
            name='Test',
            email="test@email.com",
            subject='Test',
            message='Test'
        )
        self.assertEqual(str(contact), f"{contact.name} - {contact.subject}")

    def test_resolved_defaults_to_false(self):
        """
        Test that the resolved field defaults
        to False for a new Contact instance.

        """
        contact = Contact.objects.create(
            name='Test',
            email="test@email.com",
            subject='Test',
            message='Test'
        )
        self.assertFalse(contact.resolved)
