from django.test import TestCase
from django.shortcuts import redirect
from django.test import Client


class TestCart(TestCase):
    client = Client()

    def test_add_to_cart_view_fail(self):
        response = self.client.get('add-to-cart/1/') 
        self.assertTrue(response, redirect('login'))
        
    def test_add_to_cart_view_success(self):
        self.client.login(username='a', password='123')
        response = self.client.get('add-to-cart/1/')
        self.assertTrue(response, redirect('/store/order_summary'))
    