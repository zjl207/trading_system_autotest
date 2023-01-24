# coding=utf-8
# @time: 2023/1/24 21:27
# Author: zjl

import pymysql
from common.yaml_config import GetConf


class MysqlOperate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        """
        创建数据库连接
        :return:
        """
        # 创建连接connection
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                        port=self.port, charset="utf8")
        except Exception as e:
            print(e)
            return False
        # 获取游标对cursor
        self.cur = self.conn.cursor()
        return True

    def __close_conn_db(self):
        """
        关闭连接
        :return:
        """
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        """数据库更新或删除后提交"""
        self.conn.commit()
        return True

    def query(self, sql):
        """查询"""
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("没有获取到数据,表为空")
        else:
            pass
        self.__close_conn_db()
        return query_data

    def insert_update_table(self, sql):
        """插入/更新/删除"""
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close_conn_db()


if __name__ == '__main__':
    # result = MysqlOperate().query("select * from user;")
    # print(result[0][1])
    sql = "INSERT INTO `trading_system`.`product` (`product_id`, `product_title`, `product_stock`, `product_price`, `product_desc`, `product_cover_img`, `product_detail_img`, `product_status`, `create_time`, `update_time`, `publish_user_id`) VALUES (40, '新增批量商品测试book2', 2, 100.00, '新增批量商品测试详情2', 'http://192.168.119.128:9090/product/product_img/1673868668644e9dce160-455f-4876-91f5-655376c1defa', '', 1, '2023-01-16 19:31:15', '2023-01-16 19:31:15', 12);"
    MysqlOperate().insert_update_table(sql)
