import configparser
import json
import os
from os.path import dirname
from utils.DriverFactory import DriverFactory

import pytest

ROOT_DIR = os.path.dirname(__file__)  # Project root dir


@pytest.fixture(scope='session')
def config():
    config_file = open(ROOT_DIR + "/config/config.json")
    return json.load(config_file)


@pytest.fixture(scope='session')
def context():
    return {}
