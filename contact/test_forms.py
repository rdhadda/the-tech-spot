from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_form_placeholders(self):
        """
        Test that the contact form fields have the correct placeholders.
        Asserts that each field's placeholder matches the expected value.

        """
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
            self.assertEqual(
                form.fields[field].widget.attrs['placeholder'],
                placeholders[field]
            )

    def test_contact_form_autofocus(self):
        """ 
        Test that the 'name' field of
        the contact form has the autofocus attribute.

        """
        # Instantiate the form
        form = ContactForm()

        # Check that autofocus is applied to the 'name' field
        self.assertTrue(
            form.fields['name'].widget.attrs.get('autofocus', False)
        )

    def test_contact_form_labels(self):
        """
        Test that all labels are removed from the fields of the contact form.

        """
        # Instantiate the form
        form = ContactForm()

        # Ensure labels are removed for all fields
        for field in form.fields:
            self.assertFalse(form.fields[field].label)
