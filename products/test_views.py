from django.test import TestCase
from django.urls import reverse
from .models import Product


class TestProductViews(TestCase):

    def setUp(self):
        """ create a product """
        self.product = Product.objects.create(name='Test Product', price=100)

    def test_product_details_view(self):
        """
        Test that the product details view loads
        successfully with the correct context.

        """

        # gets the URL of what would be passed through
        # to the product detail view
        url = reverse('product_detail', args=[self.product.id])

        # simulate a get request to the product detail view
        response = self.client.get(url)

        # assert that the request was successful
        self.assertEqual(response.status_code, 200)

        # assert that the correct template is used
        self.assertTemplateUsed(response, 'products/product_detail.html')

        # assert the correct product is passed in the context
        self.assertEqual(response.context['product'], self.product)

    def test_get_products_page(self):
        """
        Test that the products page loads successfully
        and uses the correct template.

        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page_user(self):
        """Test that the add product page redirects for unauthorized users."""
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
