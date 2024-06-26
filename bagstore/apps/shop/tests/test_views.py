from django.test import TestCase
from django.urls import reverse

class MainPageTest(TestCase):
    '''Тест главной страницы'''

    def test_main_page_template(self):
        '''Тест: используется шаблон для главной страницы'''
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'index.html')
    

class ShopPageTest(TestCase):
    '''Тест страницы магазина'''

    def test_shop_page_template(self):
        '''Тест: используется шаблон для страницы магазина'''
        response = self.client.get(reverse('shop'))
        
        self.assertTemplateUsed(response, 'shop.html')
