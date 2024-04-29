"""
封装断言方法

思路：
#1 遍历返回结果的每个key，
#2 根据key去预期结果找对应值
#3 比较两个结果值是否相等
"""

class AssertRe:
    def __init__(self):
        pass
    @staticmethod
    def assert_job(test_result, excepted):
        # 遍历返回结果的键值，每个值断言
        for k, v in excepted.items():
            if(type(v) == dict) :
                AssertRe.assert_job(test_result[k], v)
                continue
            #判断key是否存在
            assert k in test_result, f"结果中字段：{k}不存在！"
            assert v == test_result[k], f"字段：“{k}”中的值不相等！期望：{v}({type(v).__name__})，结果：{test_result[k]}({type(test_result[k]).__name__})"
        return None


if __name__ == '__main__':
    AssertRe().assert_job({
    "code": 0,
    "data": [],
    "msg": "成功"
}, {
    "code": 1,
    "msg": "成功"
})

