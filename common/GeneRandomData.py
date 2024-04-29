import re
import random
from common.enums.RandomDataTypeEnum import RandomDataTypeEnum
import string
import uuid
from datetime import datetime, timedelta

# 根据类型生成随机数据
def data_generator(param):
    if isinstance(param, dict):
        for key, value in param.items():
            if value == RandomDataTypeEnum.INTEGER.value:
                param[key] = random.randint(0, 10000000)
            elif value == RandomDataTypeEnum.FLOAT.value:
                param[key] = random.uniform(0, 10000000)
            elif value == RandomDataTypeEnum.STRING.value:
                characters = string.ascii_letters + string.digits  # 包含字母和数字
                param[key] = ''.join(random.choices(characters, k=length))
            elif value == RandomDataTypeEnum.RANDOM_ID.value:
                param[key] = str(uuid.uuid4()).replace('-', '')
            elif value == RandomDataTypeEnum.EMAIL.value:
                username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
                domains = ['gmail.com', 'qq.com', '163.com', 'sina.com', '126.com', 'outlook.com']
                print("随机邮箱》》》" + username + "@" + random.choice(domains))
                param[key] = username + "@" + random.choice(domains)
            elif value == RandomDataTypeEnum.DATE.value:
                start_date = "2020-01-01"
                end_date = "2024-12-31"
                start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
                end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
                # 计算日期范围
                delta = end_datetime - start_datetime
                # 生成随机日期
                random_days = random.randint(0, delta.days)
                random_date = start_datetime + timedelta(days=random_days)
                param[key] = random_date

            # 生成随机日期
            elif value == RandomDataTypeEnum.DATETIME.value:
                start_date = "2020-01-01"
                end_date = "2024-12-31"
                start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
                end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
                # 计算日期范围
                delta = end_datetime - start_datetime
                # 生成随机日期
                random_days = random.randint(0, delta.days)
                random_date = start_datetime + timedelta(days=random_days)
            elif value == RandomDataTypeEnum.PHONE.value:
                param[key] = '1' + ''.join(random.choices('0123456789', k=10))
            elif value == RandomDataTypeEnum.ID_CARD.value:
                random_date = start_datetime + timedelta(days=random_days)








