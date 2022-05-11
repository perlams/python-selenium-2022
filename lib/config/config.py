import json
from lib.config.default import DEFAULT_CONFIG

__CONFIG_FILE_PATH = "config.json"

__config_data = DEFAULT_CONFIG


def load_config():
    global __config_data
    with open (__CONFIG_FILE_PATH, 'r') as config_file:
        __user_config = json.load(config_file)
        __config_data.update(__user_config)
