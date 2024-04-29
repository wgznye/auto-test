from common.handle_log import dgLog
from common.handle_mysql import MysqlDb
from common.GeneRandomData import data_generator
import json

class DealDepend(object):
    def __init__(self):
        pass
def treat_data(execute_sql, change_word, sql, param, case_id):
    dbClient = MysqlDb()


    # 判断param字段是否为字典类型，不是就转成字典
    if isinstance(param, dict):
        pass
    elif isinstance(param, list):
        pass
    else:
        if param is not None:
            param = json.loads(param)
            data_generator(param)
    # 【判断依赖类型】
    # 1 是否数据库依赖
    if execute_sql == 1:
        # 依赖字段是否为空，说明只执行sql
        if change_word is None:
            dbClient.select_data(sql)
        else:
            # 把excel的change_word字段分割
            update_words = change_word.split(',')
            # 从数据库取到的字段值,可能有多个字段的值
            msg = dbClient.select_data(sql)
            # 遍历每个字段
            for field in range(len(msg)):
                # 判断param的类型是dict还是list
                if isinstance(param, list):
                    param[0][update_words[field]] = msg[field]
                elif isinstance(param, dict):
                    param[update_words[field]] = msg[field]
    return param


