

class LoginData:
    case_data = [
        {'title': '登录成功', 'mobile': '13200000000', 'code': '143888', "expected": '登录成功'},
        {'title': '不输入手机号', 'mobile': '', 'code': '143888', "expected": '登录失败'},
        {'title': '不输入验证码', 'mobile': '13200000000', 'code': '', "expected": '登录失败'}
    ]
