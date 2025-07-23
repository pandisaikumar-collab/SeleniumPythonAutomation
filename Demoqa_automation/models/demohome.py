import os 
import yaml 
import logging

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException, TimeoutException

DEFAULT_WAITIME = 60 

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)


class DemoHome:
    """
    Page model for Demo Home 

    :param driver: selenium driver 
    :type driver: object 
    :returns: DemoHome 
    :rtype: Object 
    """

    def __init__(self, driver):
        """
        Constructor for page
        """
        self.driver = driver 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        locator_path = os.path.join(current_dir, "..", "locators", "demohome.yaml")

        with open(locator_path, 'r') as f:
            self.locators = yaml.safe_load(f)
    
    def is_demoqa_page_loaded(self):
        """
        Returns True if Demo Home page successfully loaded.
        False otherwise 
        
        :returns: Returns status of Home demo page loading 
        :rtype: bool
        """
        page = 'Demo Home Page'
        timeout = DEFAULT_WAITIME 
        is_demo_page_loaded = True 
        try:
            WebDriverWait(self.driver, DEFAULT_WAITIME).until(
                EC.visibility_of_element_located((
                    By.XPATH, self.locators["demoheader"]["xpath"])))
            
        except TimeoutException: 
            is_demo_page_loaded = False 
            log.error(f"{page} header not loading within {timeout} seconds")

        try:
            WebDriverWait(self.driver, DEFAULT_WAITIME).until(
                EC.visibility_of_all_elements_located((
                    By.XPATH, self.locators["all_demo_elements"]["xpath"]
                )))
            
        except TimeoutException: 
            is_demo_page_loaded = False 
            log.error(f"{page} elements not loading within {timeout} seconds")

        return is_demo_page_loaded