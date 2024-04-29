import redis
import os
import json
from common.read_data import data
from common.handle_log import dgLog
from core.result_base import ResultBase

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "config.ini")
data = data.load_ini(data_file_path)["redis"]

REDIS_CONF = {
    "host": data["REDIS_HOST"],
    "port": int(data["REDIS_PORT"]),
    "password": data["REDIS_PSWD"],
}

class RedisOperations():

    def __init__(self, config_data=REDIS_CONF):
        # 读取配置文件
        # 连接到 Redis
        self.redis_client = redis.Redis(host=config_data['host'], port=config_data['port'], password=config_data['password'])

    def set_key_value(self, key, value):
        """设置 Redis 中的键值对"""
        self.redis_client.set(key, value)
        self.redis_client.expire(key, 3600)

    def get_value(self, key):
        """获取 Redis 中指定键的值"""
        return self.redis_client.get(key)

    def delete_key(self, key):
        """删除 Redis 中指定的键"""
        self.redis_client.delete(key)

    def get_keys(self, pattern='*'):
        """获取 Redis 中匹配指定模式的键"""
        return self.redis_client.keys(pattern)


# 示例用法
if __name__ == "__main__":
    redis_ops = RedisOperations()
    resultBase = ResultBase()

    resultBase.source = "PC"
    resultBase.token = "12345678"
    result_json = json.dumps(resultBase.__dict__)
    # 将resultBase保存到redis
    redis_ops.set_key_value("1", result_json)
    # 设置键值对

    # 获取值
    value = redis_ops.get_value('1')

    # 删除键
    redis_ops.delete_key('1')


redisOps = RedisOperations()
