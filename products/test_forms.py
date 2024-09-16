from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_required_fields(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())