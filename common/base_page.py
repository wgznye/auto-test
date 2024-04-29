
import time, os

import allure

from common.handle_log import dgLog
from common.handle_path import SCREEN_DIR

class BasePage:
    def __init__(self, page):
        self.page = page

    def get_element(self, loc, desc=None):

        try:
            ele = self.page.locator(loc)
        except Exception as e:
            dgLog.error(f'查找元素--【{desc}】--失败')
            dgLog.exception(e)
            self.screen_shots()
            raise e
        else:
            dgLog.info(f'查找元素--【{desc}】--成功')
        return ele

    def click_element(self, loc, desc=None):
        try:
            self.get_element(loc, desc).click()
        except Exception as e:
            dgLog.error(f'点击元素--【{desc}】--失败')
            dgLog.exception(e)
            self.screen_shots()
            raise e
        else:
            dgLog.info(f'点击元素--【{desc}】--成功')

    def click_elements(self, loc, num, desc=None):
        try:
            self.get_element(loc, desc).nth(num).click()
        except Exception as e:
            dgLog.error(f'点击元素--【{desc}】--失败')
            dgLog.exception(e)
            self.screen_shots()
            raise e
        else:
            dgLog.info(f'点击元素--【{desc}】--成功')

    def input_element(self, loc, value, desc=None):
        try:
            self.get_element(loc, desc).fill(value)
        except Exception as e:
            dgLog.error(f'输入元素--【{desc}】--[{value}]--失败')
            dgLog.exception(e)
            self.screen_shots()
            raise e
        else:
            dgLog.info(f'输入元素--【{desc}】--[{value}]--成功')

    def screen_shots(self):
        today = time.strftime('%Y-%m-%d')
        file = os.path.join(SCREEN_DIR, today)
        dir = os.listdir(path=SCREEN_DIR)
        if today not in dir:
            os.mkdir(file)
        file_name = f'{time.strftime("%H_%M_%S")}.png'
        file_dir = os.path.join(file, file_name)
        try:
            self.page.screenshot(path=file_dir, full_page=True)
        except Exception as e:
            dgLog.error(f'图片保存路径【{file_dir}】--失败')
            dgLog.exception(e)
            raise e
        else:
            with open(file_dir, 'rb') as f:
                file = f.read()
                allure.attach(file, '报错截图', allure.attachment_type.PNG)
            dgLog.info(f'图片保存路径【{file_dir}】--成功')
