import pytest
import yaml
import os
import time 
from selenium import webdriver
from models.demohome import DemoHome

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
    print("Wating 30 for website stable")
    time.sleep(30)
    yield driver
    driver.quit()


def test_demo_home_page(driver):
    home_obj = DemoHome(driver)
    assert home_obj.is_demoqa_page_loaded()
    
