from django.test import TestCase
from .models import Order, Shop

# Create your tests here.
class ShopModelTest(TestCase):
    def test_sample(self):
        temp = True
        self.assertIs(temp, True)

class OrderModelTest(TestCase):
    def test_sample(self):
        temp = True
        self.assertIs(temp, True)
