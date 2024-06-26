from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    '''Тест макета и стилевого оформления'''
    def test_layout_and_styling(self):
        '''Тест: макет и стилевое оформление'''
        # Билл открывает главную страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1480, 800)

        # Он замечает, что на страницу отображается картинка
        self.browser.find_element(By.TAG_NAME, 'src')
        # Тут же отображается текст
        main_text = self.browser.find_element(By.ID, 'main_text')
        self.assertAlmostEqual(main_text.location['x'], 760, delta=10)
        self.assertAlmostEqual(main_text.location['y'], 300, delta=10)

        # Вверху страницы он замечает лого
        logo = self.browser.find_element(By.ID, 'logo')
        self.assertAlmostEqual(logo.location['x'], 100, delta=10)

        # Рядом с лого расположены кнопки меню
        shop = self.browser.find_element(By.LINK_TEXT, 'Магазин')
        self.assertAlmostEqual(shop.location['x'], 380, delta=10)

        # Между ними примерно 60 px
        cart = self.browser.find_element(By.LINK_TEXT, 'Корзина')
        self.assertAlmostEqual(cart.location['x'] - shop.location['x'], 60, delta=10)
        
        # Кнопки расположены на одном уровне
        self.assertAlmostEqual(shop.location['y'], cart.location['y'])
