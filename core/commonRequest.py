import requests
import json
import datetime
from core.result_base import ResultBase
from common.handle_redis import redisOps
from core.rest_client import RestClient
from common.handle_log import dgLog


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

def common_api(casesId, host, path, param, param_type, method, header, header_change):
    # 封装请求
    client = RestClient(host)
    redis_auth = redisOps.get_value(casesId)
    headerObj = assemble_header(header, redis_auth, header_change)

    result = None
    response = None
    resultBase = ResultBase()

    try:
        if method == 'POST' and (param_type is None or param_type == 'json'):
            response = client.post(path, json=param, headers=headerObj)
            result = response.json()
        elif method == 'POST' and param_type == 'params':
            response = client.post(path, params=param, headers=headerObj)
            result = response.json()
        elif method == 'GET':
            response = client.get(path, params=param, headers=headerObj)
            result = response.json()
        elif method == 'PUT':
            response = client.put(path, data=param, headers=headerObj)
            result = response.json()
        else:
            print(param)
    except requests.exceptions.ConnectTimeout as e:
        result = {response.content: 'timeout'}

    dgLog.info('实际响应为：%s' % result)

    status = result["success"]
    if path == '/dg-user-api/api/login/code' and status == True :
        resultBase.source = result["data"]["source"]
        resultBase.token = result["data"]["token"]
        result_json = json.dumps(resultBase.__dict__)
        redisOps.set_key_value(casesId, result_json)
    return result


def assemble_header(header, redis_auth, header_change):

    headerObj = {}
    if header is not None:
        headerObj = eval(header)

    if header_change is not None and redis_auth is not None:
        result_dict = json.loads(redis_auth)
        # 从字典中提取 token 属性
        token = result_dict.get("token", None)
        headerObj[header_change] = token
        print("headerObj:", headerObj)

    source_ = headerObj.get('Source')
    if source_ is None:
        headerObj['Source'] = "PC"
    return headerObj



