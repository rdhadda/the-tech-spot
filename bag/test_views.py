from django.test import TestCase
from django.urls import reverse
from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        # create a product
        self.product = Product.objects.create(name='Test Product', price=100)

    def test_get_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):

        post_data = {
            'quantity': 2,
            'redirect_url': reverse('product_detail', args=[self.product.id])
        }

        self.client.post(reverse(
            'add_to_bag', args=[self.product.id]), post_data
            )
        
        bag = self.client.session.get('bag', {})

        self.assertIn(str(self.product.id), bag)
        self.assertEqual(bag[str(self.product.id)], 2)

    def test_remove_from_bag(self):

        post_data = {
            'quantity': 1,
            'redirect_url': reverse('product_detail', args=[self.product.id])
        }

        self.client.post(reverse(
            'add_to_bag', args=[self.product.id]), post_data
            )

        bag = self.client.session.get('bag', {})

        self.client.post(reverse(
            'remove_from_bag', args=[self.product.id])
            )
              
        bag = self.client.session.get('bag', {})

        self.assertNotIn(str(self.product.id), bag)
