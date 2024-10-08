from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_required_fields(self):
        """
        Test that the name field is required and
        validation fails when it's empty.

        """
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())