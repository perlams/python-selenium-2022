import json
from lib.config.default import DEFAULT_CONFIG

__CONFIG_FILE_PATH = "config.json"

__config_data = DEFAULT_CONFIG


def load_config():
    global __config_data
    with open (__CONFIG_FILE_PATH, 'r') as config_file:
        __user_config = json.load(config_file)
        __config_data.update(__user_config)
        print(f'Driver configuration: {__config_data}')

def get_url():
    return __config_data['url']


def get_browser_name() -> str:
    return __config_data['browser_name']


def get_driver_path() -> str:
    return __config_data['path']


def get_incognito_mode() -> bool:
    return __config_data['incognito']


def get_headless_mode() -> bool:
    return __config_data['headless']['enabled']


def get_headless_resolution() -> dict:
    """Get resolution width and height from user config.

    :return: Dictionary with width and height.
    """
    return __config_data['headless']['resolution']


def get_page_load_timeout():
    return __config_data['page_load']


def get_implicit_wait():
    return __config_data['implicit_wait']


def get_explicit_wait_small():
    return __config_data['explicit_waits']['small']


def get_explicit_wait_medium():
    return __config_data['explicit_waits']['medium']


def get_explicit_wait_large():
    return __config_data['explicit_waits']['large']