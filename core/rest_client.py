import requests
import json as complexjson
from common.handle_log import dgLog


class RestClient():

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        self.request_log(url, method, data, json, params, headers)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None,  **kwargs):
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        # 组装请求内容
        api_request_content = "接口请求地址 ==>> {}".format(url) + "\n接口请求方式 ==>> {}".format(method)
        if(headers != None):
            api_request_content = api_request_content + "接口请求头 ==>> {}\n".format(complexjson.dumps(headers, indent=4, ensure_ascii=False))
        if(params != None):
            api_request_content = api_request_content + "接口请求 params 参数 ==>> {}\n".format(complexjson.dumps(params, indent=4, ensure_ascii=False))
        if (data != None):
            api_request_content = api_request_content + "接口请求体 data 参数 ==>> {}\n".format(complexjson.dumps(data, indent=4, ensure_ascii=False))
        if (json != None):
            api_request_content = api_request_content + "接口请求体 json 参数 ==>> {}\n".format(complexjson.dumps(json, indent=4, ensure_ascii=False))
        dgLog.info(api_request_content);
