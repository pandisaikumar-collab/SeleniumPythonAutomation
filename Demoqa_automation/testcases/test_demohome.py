import os
import yaml
import time
import pytest 
import logging 
from selenium import webdriver
from models.demohome import DemoHome
from models.elements import Elements

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

if not log.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)

@pytest.fixture(scope='session')
def config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.yaml')
    with open(config_path) as file:
        return yaml.safe_load(file)

@pytest.fixture()
def driver(config):
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox': 
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser in config.")

    driver.get(config['base_url'])
    driver.maximize_window()
    time.sleep(5)
    log.info("Waiting 10 seconds for website to stabilize")
    yield driver
    driver.quit()

def test_demo_home_page(driver, config):
    home_obj = DemoHome(driver)
    elements_obj = Elements(driver)
    if home_obj.is_demoqa_page_loaded():
        home_obj.click_elements_button()
        if elements_obj.is_elements_page_loaded():
            assert True, "Elements page loaded successfully"
            elements_obj.click_webtable_button()
            table_data = elements_obj.get_web_table_data()
            if table_data:
                log.info(f"Table data: %s", table_data)
            else:
                pytest.fail("No data found in the web table")
            
            payload = dict()
            payload['firstname'] = config['registration_form']['firstname']
            payload['lastname'] = config['registration_form']['lastname']
            payload['email'] = config['registration_form']['email']
            payload['age'] = config['registration_form']['age']
            payload['salary'] = config['registration_form']['salary']
            payload['department'] = config['registration_form']['department']

            if not payload:
                pytest.fail("No registration payload found in config file")
            else:
                elements_obj.fill_registration_form(payload)
    else:
        pytest.fail("Failed to load Demo Home page")
