
import subprocess
import pytest
from common.handle_path import TESTCASE_DIR,REPORT_DIR

pytest.main([f'{TESTCASE_DIR}/api_test', '-s', '-v', f'--alluredir={REPORT_DIR}'])
# pytest.main([f'{TESTCASE_DIR}/ui_test', '-s', '-v', f'--alluredir={REPORT_DIR}'])
allure_serve_command = ["allure", "serve", "reports"]
subprocess.run(allure_serve_command)