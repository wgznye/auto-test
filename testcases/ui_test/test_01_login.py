
import pytest, allure
from page.coal_play_page import CoalPlayPage, IndexPage
from data.ui.login_data import LoginData


@allure.suite('用户模块')
@allure.story('登录功能')
class TestLogin:

    @pytest.mark.parametrize('case', LoginData.case_data)
    def test_login(self, login_fixture, case):
        allure.dynamic.title(case['title'])
        page = login_fixture
        coal_play_page = CoalPlayPage(page)
        coal_play_page.login(phone=case['mobile'], code=case['code'])
        assert IndexPage(page).is_login_success() == case['expected']
