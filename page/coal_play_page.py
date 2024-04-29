
from locator.login_locator import LoginLocator
from locator.coaling_play_locator import CoalingPlayLocator
from common.base_page import BasePage
from common.handle_config import conf
from common.handle_log import dgLog
from playwright.sync_api import sync_playwright, expect


class CoalPlayPage(BasePage):

    def login(self, phone, code):
        self.input_element(LoginLocator.phone_loc, phone, '输入手机号')
        self.input_element(LoginLocator.pwd_loc, code, '输入验证码')
        self.click_element(LoginLocator.login_button_loc, '登录按钮')

    def coaling_play(self):
        self.click_element(CoalingPlayLocator.station_tab_loc, '物流仓储中心')
        self.click_element(CoalingPlayLocator.create_coaling_loc, '创建上煤合同')
        self.click_element(CoalingPlayLocator.not_link_loc, '暂不关联')
        self.click_element(CoalingPlayLocator.forwarding_unit_loc, '选择发货单位')
        self.click_element(CoalingPlayLocator.forwarding_unit_select_loc, '天宇源')
        self.click_element(CoalingPlayLocator.receiving_unit_loc, '选择收货单位')
        self.click_elements(CoalingPlayLocator.receiving_unit_select_loc, 1, '河南荣厚')
        self.click_element(CoalingPlayLocator.coal_loc, '选择煤种')
        self.click_element(CoalingPlayLocator.coal_select_loc, '煤种：123')
        self.click_element(CoalingPlayLocator.warehouse_loc, '选择仓房')
        self.click_element(CoalingPlayLocator.warehouse_select_loc, '仓房：1号煤堆区')
        self.click_element(CoalingPlayLocator.goods_allocation_loc, '选择货位')
        self.click_element(CoalingPlayLocator.goods_allocation_select_loc, '货位：货位2')
        self.input_element(CoalingPlayLocator.forwarding_station_loc, '郑州', '输入发站')
        self.input_element(CoalingPlayLocator.plan_wright_loc, '50', '输入计划吨数')
        self.input_element(CoalingPlayLocator.description_loc, '输入计划吨数输入框1234', '输入内容描述')
        self.click_element(CoalingPlayLocator.submit_loc, '提交按钮')

    def is_new_success(self):
        try:
            expect(self.get_element(CoalingPlayLocator.plan_wright_loc, '创建按钮')).to_contain_text('创建上煤')
        except AssertionError as e:
            dgLog.error("断言失败")
            dgLog.exception(e)
            self.screen_shots()
            res = '新建上煤计划失败'
        else:
            res = '新建上煤计划成功'
        return res


class IndexPage(BasePage):

    def is_login_success(self):
        try:
            expect(self.get_element(LoginLocator.index_help, '帮助中心')).to_contain_text('帮助中心')
        except AssertionError as e:
            dgLog.error('登录失败')
            dgLog.exception(e)
            self.screen_shots()
            res = '登录失败'
        else:
            res = '登录成功'

        return res


if __name__ == '__main__':
    with sync_playwright() as p:
        url = conf.get('test3', 'url')
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        content = browser.new_context(no_viewport=True)
        page = content.new_page()
        page.goto(url)
        CoalPlayPage(page).coaling_play()
