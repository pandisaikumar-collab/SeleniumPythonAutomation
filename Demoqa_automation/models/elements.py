"""
elements.py
Page model for Demo home page
Author(s): Pandi Saikumar <pandisaikumar.tech@gmail.com>
"""
import os 
import time 
import yaml 
import logging

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException, TimeoutException

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

DEFAULT_WAITIME = 60

class Elements:
    """
    Page model for Elements 
    :param driver: selenium driver
    :type driver: object
    """

    def __init__(self, driver):
        """
        Constructor for Elements page
        """
        self.driver = driver 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.locators = current_dir + "/../locators/elements.yaml"

        with open(self.locators, 'r') as file:
            self.xpaths = yaml.safe_load(file)
    
    def is_elements_page_loaded(self):
        """
        Returns True if elements page loaded 
        False otherwise
        :returns: bool
        """
        page = 'Elements page'
        timeout = DEFAULT_WAITIME
        is_elements_page_loaded = True
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((
                    By.XPATH, self.xpaths["elements_groups"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_elements_page_loaded = False
            log.error(f"{page} not loaded: {e}")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((
                    By.XPATH, self.xpaths["elements_groups"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_elements_page_loaded = False
            log.error(f"{page} not loaded: {e}")
        
        return is_elements_page_loaded

    def select_dropdown_item(self, dropdown_xpath, dropdown_items_xpath, dropdown_item):
        """
        Generic function to select <dropdown> from <dropdown_xpath>>
        
        param: drpdown_xpath: Drpdown xpath
        :type drpdown_xpath: str
        :param drpdown_items: Dropdown items xpath
        :type drpdown_items: list
        """
        is_dropdown_selected = False 
        dropdown_element = self.driver.find_element(By.XPATH, dropdown_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
        dropdown_element.click()
        time.sleep(0.5)

        dropdown_item_elements = self.driver.find_element(By.XPATH, dropdown_items_xpath)
        for dropdown_item_element in dropdown_item_elements:
            if dropdown_item_element.text == dropdown_item:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_item_element)
                dropdown_item_element.click()
                is_dropdown_selected = True 
                break
            if not is_dropdown_selected:
                log.error(f"Dropdown item '{dropdown_item}' not found in dropdown")
        return is_dropdown_selected

    def click_button(self, xpath):
        """
        Metthod to click on a button using xpath
        :param xpath: ele xpath
        :type xpath: str
        """
        ele_text = self.driver.find_element(By.XPATH, xpath)
        log.info(f"Clicking on button with text: {ele_text.text}")
        ele = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        time.sleep(0.5)
        ele.click()
        
    def click_elements_button(self):
        """
        Clicks on the Elements button 
        """
        return self.click_button(xpath=self.xpaths["elements_wrapper"]["xpath"])
    
    def click_text_box_button(self):
        """
        Clicks on the Text Box button
        """
        return self.click_button(xpath=self.xpaths["elements_groups"]["text_box"]["xpath"])

    def click_webtable_button(self):
        """
        Clicks on the Web Table button
        """
        return self.click_button(xpath=self.xpaths["elements_groups"]["web_tables"]["xpath"])

    def get_web_table_data(self):
        """
        Return Table data 
        :returns: Dict data
        :rtype: dict 
        """
        table_info = {}

        first_name_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["firstname"]["xpath"])
        last_name_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["lastname"]["xpath"])
        age_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["age"]["xpath"])
        email_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["email"]["xpath"])
        salary_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["salary"]["xpath"])
        department_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["department"]["xpath"])
        if not first_name_eles:
            log.info("No data found in the table")
            return table_info

        for index, first_name_ele in enumerate(first_name_eles):
            last_name_ele = last_name_eles[index]
            age_ele = age_eles[index]
            email_ele = email_eles[index]
            salary_ele = salary_eles[index]
            department_ele = department_eles[index]

            first_name = first_name_ele.text.strip()
            last_name = last_name_ele.text.strip()
            age = age_ele.text.strip()
            email = email_ele.text.strip()
            salary = salary_ele.text.strip()
            department = department_ele.text.strip()

            table_data = {
                "Firstname": first_name,
                "Lastname": last_name,
                "Age": age,
                "Email": email,
                "Salary": salary,
                "Department": department
            }

            table_info[first_name] = table_data

        return table_info
