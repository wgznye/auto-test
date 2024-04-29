
import logging
import os
from datetime import datetime
from common.handle_path import LOG_DIR


class CreateLog:
    def __init__(self, name, level, filename, sh_level, fh_level):
        self.name = name
        self.level = level
        self.filename = filename
        self.sh_level = sh_level
        self.fh_level = fh_level

    def creat_log(self):
        # 创建日志收集器
        log = logging.getLogger(self.name)
        log.setLevel(self.level)
        # 输入日志到文件
        fh = logging.FileHandler(self.filename, encoding='utf-8')
        fh.setLevel(self.fh_level)
        log.addHandler(fh)
        # 输出日志到控制台
        sh = logging.StreamHandler()
        sh.setLevel(self.sh_level)
        log.addHandler(sh)
        # 设置日志格式
        formats = '%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s'
        log_format = logging.Formatter(formats)

        sh.setFormatter(log_format)
        fh.setFormatter(log_format)
        return log


today = str(datetime.now().strftime("%Y-%m-%d")) + '.log'
file_dir = os.path.join(LOG_DIR, today)
link_log = CreateLog(name="log", filename=file_dir, level='DEBUG', fh_level='DEBUG', sh_level='DEBUG')
dgLog = link_log.creat_log()
