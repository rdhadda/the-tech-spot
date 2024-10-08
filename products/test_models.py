from django.test import TestCase
from .models import Category, Product


class TestModels(TestCase):

    def test_product_string_method(self):
        """Test the string representation of the Product model."""
        product = Product.objects.create(name='Test Product', price=100)
        self.assertEqual(str(product), 'Test Product')

    def test_category_string_method(self):
        """Test the string representation of the Category model."""
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_friendly_name_method(self):
        """Test the get_friendly_name method of the Category model."""
        friendly_name = Category.objects.create(name='Test Category 1',
                                                friendly_name='Friendly Name')
        self.assertEqual(friendly_name.get_friendly_name(), 'Friendly Name')
