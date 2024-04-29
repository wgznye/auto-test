
import os
import pytest
import requests
import json
import allure
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_config import conf
from openpyxl import load_workbook
from core.commonRequest import common_api
from common.dealrely import treat_data
from common.handle_assert import AssertRe
from common.handle_request import HandleRequest
from common.CleanCache import CleanCache
from common.handle_redis import redisOps

CleanCache.clean_dir("./reports")

excel_file_path = os.path.join(DATA_DIR, 'api/rest.xlsx')
excel = HandleExcel(filename=excel_file_path)

wb = load_workbook(excel_file_path)
data = excel.read_file()

titles = []
handleRequest = HandleRequest()
assertRe = AssertRe()

@allure.parent_suite('数链')
class TestApi():

    # 用例优先级
    # blocker：阻塞缺陷（功能未实现，无法下一步）
    # critical：严重缺陷（功能点缺失）
    # normal： 一般缺陷（边界情况，格式错误）
    # minor：次要缺陷（界面错误与ui需求不符）
    # trivial： 轻微缺陷（必须项无提示，或者提示不规范）
    @allure.severity('critical')
    @pytest.mark.parametrize('case_id, env, module, title, method, path, header, auth, param, param_type, execute_sql,'
                             'sql, expect, change_word, execute_count, casesId', data)
    def test_api(self, case_id, env, module, title, method, path, header, auth, param, param_type, execute_sql, sql, expect, change_word, execute_count, casesId):
        allure.dynamic.suite(env)
        allure.dynamic.sub_suite(module)
        allure.dynamic.description(path)
        allure.dynamic.title(str(case_id) + "、" + title)
        if execute_count is None:
            execute_count = 1
        # execute_count == 0 直接跳过不执行
        if execute_count == 0:
            pytest.skip()

        for i in range(int(execute_count)):
            title = title + "-" + str(i+1)
            # 判断用例是否执行过，执行过就pass掉【根据title名称】
            if title not in titles:
                titles.append(title)
                data = param
                print(f'执行用例参数—case_id：{case_id}；env：{env}；module：{module}；title：{title}；method：{method}；path：{path}；header：{header}；auth：{auth}；param：{param}；param_type：{param_type}；execute_sql：{execute_sql}；sql：%s；expect：{expect}；change_word：{change_word}')
                with allure.step(f'第{i + 1}条用例处理数据依赖，修改body'):
                    data = treat_data(execute_sql, change_word, sql, param, case_id)
                    handleRequest.save_body(case_id, data)
                with allure.step(f'第{i + 1}条用例发送请求，得到响应'):
                    root_url = conf.get(env, 'base_url')
                    # casesId, host, path, body, param_type, method, header, header_change
                    test_result = common_api(casesId, root_url, path, data, param_type, method, header, auth)
                with allure.step(f'第{i + 1}条用例与预期结果比较断言'):
                    loads = json.loads(expect)
                    assertRe.assert_job(test_result, loads)



