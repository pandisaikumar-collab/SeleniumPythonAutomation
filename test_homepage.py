import unittest
import time
import logging
import os
from pprint import pprint

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumautomation.core.models.homepage import HomeNavigation, read_config

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

class CommonSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = FirefoxService(GeckoDriverManager().install())
        cls.driver = webdriver.Firefox(service=service)
        config = read_config()
        cls.homepage = HomeNavigation(cls.driver)

        url = config['url']
        cls.homepage.connect_to_browser(url)
        cls.homepage.is_home_page_loaded()
        print("Launched browser successfully and waiting 60 seconds for stable")

    def test_web_inputs(self):
        """
        Method to perform webinputs page
        :return:
        """
        self.homepage.click_on_web_inputs()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()