from selenium.webdriver.common.by import By

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    '''Тест макета и стилевого оформления'''
    def test_layout_and_styling_main_page(self):
        '''Тест: макет и стилевое оформление главной страницы'''
        # Билл открывает главную страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1480, 800)

        # Он замечает, что на страницу отображается картинка
        main_img = self.browser.find_element(By.ID, 'main_img')
        self.assertAlmostEqual(main_img.location['x'], 260, delta=10)
        # Тут же отображается текст
        main_text = self.browser.find_element(By.ID, 'main_text')
        self.assertAlmostEqual(main_text.location['x'], 700, delta=10)
        self.assertAlmostEqual(main_text.location['y'], 300, delta=10)

        # Билл видит аккуратное меню навигация в левом верхнем углу
        self.the_correct_location_of_the_navigation_buttons(self)

    def test_layout_and_styling_shop_page(self):
        '''Тест: макет и стилевое оформление страницы магазин'''
        # Билл открывает главную страницу и переходит в раздел "Магазин"
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.LINK_TEXT, 'Магазин').click()

        # Здесь билл так же видит лого и кнопки меню рядом с ним
        self.the_correct_location_of_the_navigation_buttons(self)

        # Билл видит карточки товаров
        products = self.browser.find_elements(By.CLASS_NAME, 'product_card')
        # Первая и вторая карточка расположены рядом друг с другом
        first = products[0]
        second = products[1]
        # вторая карточка справа от первой карточки 
        # и они располагаются на одном уровне
        self.assertAlmostEqual(
            first.location['x'] + first.size['width'], 
            second.location['x'], 
            delta=40
        )
        self.assertEqual(first.location['y'], second.location['y'])
        
        third = products[2]
        # Третья карточка расоложена слева под первой карточкой
        self.assertEqual(first.location['x'], third.location['x'])
        self.assertEqual(first.location['y'] + first.size['width'], third.location['y'], delta=40)
        
    def test_layout_and_styling_cart_page(self):
        '''Тест: макет и стилевое оформление страницы корзины'''
                # Билл открывает главную страницу и переходит в раздел "Магазин"
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.LINK_TEXT, 'Корзина').click()

        # Здесь билл так же видит лого и кнопки меню рядом с ним
        self.the_correct_location_of_the_navigation_buttons(self)

        self.fail('доделать тест')
        