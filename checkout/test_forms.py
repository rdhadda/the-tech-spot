from django.test import TestCase
from checkout.forms import OrderForm
from checkout.models import Order


class TestOrderForm(TestCase):

    def test_order_form_valid_data(self):
        # Test valid data
        form_data = {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Test Street',
            'street_address2': 'Apt 4',
            'town_or_city': 'Test City',
            'postcode': '12345',
            'country': 'GB',
            'county': 'Test County',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid
    
    def test_order_form_invalid_data(self):
        # Test missing required fields
        form_data = {
            'full_name': '',
            'email': 'invalidemail',
            'phone_number': '',
            'street_address1': '',
            'town_or_city': '',
            'postcode': '',
            'country': '',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())  # Form should be invalid
    
    def test_order_form_placeholder_attributes(self):
        # Test placeholders and attributes in form fields
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'Email Address *')
        self.assertEqual(form.fields['street_address1'].widget.attrs['placeholder'], 'Street Address 1 *')
        self.assertEqual(form.fields['street_address2'].widget.attrs['placeholder'], 'Street Address 2')
        self.assertEqual(form.fields['phone_number'].widget.attrs['placeholder'], 'Phone Number *')
    
    def test_order_form_autofocus(self):
        # Test autofocus attribute
        form = OrderForm()
        self.assertIn('autofocus', form.fields['full_name'].widget.attrs)
        self.assertTrue(form.fields['full_name'].widget.attrs['autofocus'])