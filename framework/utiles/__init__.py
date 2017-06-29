from testconfig import config
import requests

CONFIG = {
    'url': config['config']['url'],
    'admin_username': config['config']['admin_username'],
    'admin_password': config['config']['admin_password'],
    'user_username': config['config']['user_username'],
    'user_password': config['config']['user_password'],
    'browser': config['config']['browser'],
    'session': requests.Session()
}
