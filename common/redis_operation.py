# coding=utf-8
# @time: 2023/1/26 18:13
# Author: zjl

import redis

from common.yaml_config import GetConf


class RedisOperation:
    def __init__(self):
        redis_info = GetConf().get_redis()
        self.redis_client = redis.Redis(
            host=redis_info["host"],
            port=redis_info["port"],
            db=redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding="UTF-8"
        )  # 如果有用户名密码 password=user:password

if __name__ == '__main__':
    print(RedisOperation().redis_client.get("ZJL"))