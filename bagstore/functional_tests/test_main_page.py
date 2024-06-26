from selenium.webdriver.common.by import By

from django.urls import reverse

from .base import FunctionalTest

class MainPageTest(FunctionalTest):
    '''Тест главной страницы'''

    def test_shop_button(self):
        '''Тест: кнопка "магазин" переносит пользователя в магазин'''
        # Билл заходит на сайт
        self.browser.get(self.live_server_url)

        # Он видит кнопку "магазин" и нажимает на нее
        self.browser.find_element(By.LINK_TEXT, 'Магазин').click()

        # Сайт переносит его в магазин
        self.assertEqual(self.browser.current_url, reverse('shop'))
        
    def test_shopping_cart_button(self):
        '''Тест: кнопка "корзин" переносит пользователя в его корзину'''
        # Билл заходит на сайт
        self.browser.get(self.live_server_url)
        
        # Он видит кнопку "корзина" и нажимает на нее
        self.browser.find_element(By.LINK_TEXT, 'Корзина').click()

        # Сайт переносит его в корзину
        self.assertEqual(self.browser.current_url, reverse('shopping_cart'))
