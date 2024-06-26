import time
import os

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.webdriver import WebDriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    '''Функциональный тест'''

    def setUp(self):
        '''Установка'''
        self.browser = WebDriver()
        self.staging_server = os.environ.get('STAGING_SERVER')
        if self.staging_server:
            self.live_server_url = 'http://' + self.staging_server
    
    def tearDown(self):
        '''Удаление'''
        self.browser.quit()
    
    def wait_for(self, fn):
        '''Ожидать'''
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
