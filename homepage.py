"""
homepage.py
Page model for home navigation
Author(s) <pandisaikumar.tech@gmail.com>
"""
import yaml
import os
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)


def read_xpaths(file_path=r"C:\Users\pasaikum\PycharmProjects\MyAutomation\seleniumautomation\core\locators\homepage.yaml"):
    with open(file_path, 'r') as file:
        xpaths = yaml.safe_load(file)
    return xpaths

def read_config(file_path = r"C:\Users\pasaikum\PycharmProjects\MyAutomation\seleniumautomation\config\config.yaml"):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class HomeNavigation:

    def __init__(self, driver):
        """
        Constructor for the HomeNavigation
        :param driver:
        """
        self.driver = driver
        self.xpaths = read_xpaths()


    def connect_to_browser(self,url):
        """
        Launching the browser
        :param url:
        :return:
        """
        return self.driver.get(url)


    def is_home_page_loaded(self):
        """
        Function to check whether the home page is loaded
        :return:
        """
        try:
            time.sleep(20)
            log.info("Checking is home page is loaded or not")
            home_element = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((
                    By.XPATH, self.xpaths['home_header']['xpath'])))

        except Exception as error:
            log.error(error)

    def scroll_into_view(self, element):
        """
        Function to scroll an element into view
        :param element: The XPath of the element to scroll into view
        :return: None
        """
        ele = self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("scrolling page until element is visible")
        time.sleep(60)

    def click_on_home_link(self):
        """
        Function to click on home link
        :return:
        """
        home_link_element = self.driver.find_element(By.XPATH, self.xpaths['home_link']['xpath'])
        self.scroll_into_view(home_link_element)
        home_link_element.click()


    def click_on_web_inputs(self):
        """
        Function to click on web inputs link
        :return:
        """
        try:
            log.info("Clicking on web inputs link")
            webinput_element = self.driver.find_element(By.XPATH, self.xpaths['web_inputs']['xpath'])
            self.scroll_into_view(webinput_element)
            time.sleep(60)
            webinput_element.click()


        except Exception as error:
            log.error(error)

    def quit(self):
        """
        close the all browsers
        :return:
        """

        return self.driver.quit()










