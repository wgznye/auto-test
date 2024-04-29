
import pytest, allure
from common.handle_config import conf
from page.coal_play_page import CoalPlayPage


@allure.suite('物流站台模块')
@allure.story('创建上煤计划')
class TestCoalPlay:
    phone = conf.get('test3-rest', 'phone')
    code = conf.get('test3-rest', 'code')

    @allure.title('创建上煤计划')
    def test_coaling_play(self, login_fixture):
        page = login_fixture
        coal_play_page = CoalPlayPage(page)
        coal_play_page.login(self.phone, self.code)
        coal_play_page.coaling_play()
        assert coal_play_page.is_new_success() == '新建上煤计划成功'


if __name__ == '__main__':
    pytest.main()
