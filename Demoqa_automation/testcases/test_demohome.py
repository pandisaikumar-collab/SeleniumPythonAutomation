import pytest 
import yaml 
import selenium import webdriver 

@pytest.fixture(scop='session')
def config():
    with open("") as file:
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
    yield driver
    driver.quit()


