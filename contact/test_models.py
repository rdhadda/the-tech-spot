from django.test import TestCase
from .models import Contact


class TestContactModels(TestCase):

    def test_string_representation(self):
        contact = Contact(name='Test', email="test@email.com", subject='Test', message='Test')
        self.assertEqual(str(contact), f"{contact.name} - {contact.subject}")

    def test_resolved_defaults_to_false(self):
        contact = Contact.objects.create(
            name='Test',
            email="test@email.com",
            subject='Test',
            message='Test'
        )
        self.assertFalse(contact.resolved)

