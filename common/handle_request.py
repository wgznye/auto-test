import json
import jsonpath
from common.handle_log import dgLog

class HandleRequest(object):

    def __init__(self):
        # 初始化保存请求和相应的两个字典
        self.actual_body_1 = {}
        self.actual_body_2 = {}

    # 保存请求方法
    def save_body(self,case_id, actual_body):
        # 添加一个键值对到字典
        self.actual_body_1[case_id] = actual_body

    def read_depend_data(self, depend):
        # 定义一个函数返回的修改后的字典
        depend_dict = {}

        if isinstance(depend, dict):
            pass
        else:
            # 字典转为json格式的字符串
            temp = json.dumps(depend)
            # json格式字符串转为字典
            depend = json.loads(temp)

        # 判断depend字典里面是否有body字段，有说明需要从之前的body上取，修改body
        if 'body' in depend:
            # 对depend字典的每个键值对遍历
            for k,v in depend.items():
                try:
                    # 如果键是body，就不用处理
                    if k == 'body':
                        # print('不处理')
                        pass
                    else:
                        # 对每个value遍历
                        for value in v:
                            # print('body字典的值为: %s' % self.actual_body_1)
                            dgLog.info('body字典的值为: %s' % self.actual_body_1)
                            # 根据这个value的key，到保存请求的字典actual_body_1找对应的value
                            actual = self.actual_body_1[k]
                            # 切片
                            d_k = value.split('.')[-1]
                            # 找到的value值添加到depend_dict字典里
                            depend_dict[d_k] = jsonpath.jsonpath(actual,value)[0]
                except TypeError as e:
                    dgLog.error(f'实际body中无法正常使用该表达式提取到任何内容，发现异常{e}')
        else:
            for k,v in depend.items():
                try:
                    for value in v:
                        # print('body字典的值为: %s' % self.actual_body_2)
                        dgLog.info('body字典的值为: %s' % self.actual_body_2)
                        actual = self.actual_body_2[k]
                        # 返回依赖数据的key
                        d_k = value.split('.')[-1]
                        # 添加到依赖数据字典并返回
                        depend_dict[d_k] = jsonpath.jsonpath(actual, value)[0]
                except TypeError as e:
                    dgLog.error(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')

        return depend_dict


