"""
test_realpython.py
"""

import pytest
import requests
import os
import json 
import yaml 
import logging
from models.rest.realpython import RealPython

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

current_dir = os.path.dirname(os.path.abspath(__file__))
end_pionts = os.path.join(current_dir, '../../config/endpoints.yaml')
with open(end_pionts, 'r') as file:
    endpoints = yaml.safe_load(file)

def test_get_request():
    realpython_obj = RealPython()
    get_url = endpoints['REALPYTHON_GET']
    response = realpython_obj.get(get_url)

    if response.status_code == 200:
        data = response.json()
        log.info(f"Response data: {data}")
        log.info(f"Response content: {response.content}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response elapsed time: {response.elapsed.total_seconds()} seconds")
        log.info(f"Response URL: {response.url}")
        log.info(f"Response encoding: {response.encoding}")
        log.info(f"Response reason: {response.reason}")
        log.info(f"Response text: {response.text}")

    else:
        log.info(f"GET request failed with status code: {response.status_code}")
        log.info(f"Response content: {response.content}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response text: {response.text}")
        pytest.fail(f"GET request failed with status code: {response.status_code}")
