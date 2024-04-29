
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')


conf_file = os.path.join(CONF_DIR, 'config.ini')
conf = Config(conf_file)


