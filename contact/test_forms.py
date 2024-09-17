from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_form_placeholders(self):
        # Instantiate the form
        form = ContactForm()

        # Check the placeholders for each field
        placeholders = {
            'name': 'Name *',
            'email': 'Email *',
            'subject': 'Subject *',
            'message': 'Message *'
        }

        for field in placeholders:
            self.assertEqual(form.fields[field].widget.attrs['placeholder'], placeholders[field])

    def test_contact_form_autofocus(self):
        # Instantiate the form
        form = ContactForm()

        # Check that autofocus is applied to the 'name' field
        self.assertTrue(form.fields['name'].widget.attrs.get('autofocus', False))

    def test_contact_form_labels(self):
        # Instantiate the form
        form = ContactForm()

        # Ensure labels are removed for all fields
        for field in form.fields:
            self.assertFalse(form.fields[field].label)
