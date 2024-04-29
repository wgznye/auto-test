
import pymysql
from sshtunnel import SSHTunnelForwarder
from common.handle_config import conf


class HandleMysql:

    def __init__(self, remote_bind_address, user, passwd):
        """
        跳板机配置 连接数据库
        """
        host = conf.get('JUMP_SERVE', 'host')
        port = conf.getint('JUMP_SERVE', 'port')
        id_rsa = conf.getint('JUMP_SERVE', 'id_rsa')
        self.ssh_server = SSHTunnelForwarder(
            # 跳板机配置信息
            ssh_address_or_host=(host, port),
            ssh_username='app',
            ssh_pkey=id_rsa,
            remote_bind_address=(remote_bind_address, 3306)
        )
        self.ssh_server.start()

        self.con = pymysql.connect(
            host='127.0.0.1',
            port=self.ssh_server.local_bind_port,
            user=user,
            passwd=passwd
        )

    def execute_sql(self, sql):
        """
        处理传入的sql语句
        :param sql: sql语句
        :return:
        """
        with self.con.cursor() as cur:
            res = cur.execute(sql)
            self.con.commit()
        return res

    def find_one(self, sql):
        """
        获取查询集中的第一条数据
        :param sql:
        :return:
        """
        with self.con.cursor() as cur:
            cur.execute(sql)
        return cur.fetchone()

    def find_all(self, sql):
        """
        获取查询集中的所有数据
        :param sql:
        :return:
        """
        with self.con.cursor() as cur:
            cur.execute(sql)
        return cur.fetchall()

    def __del__(self):
        self.con.close()


mydb = HandleMysql(remote_bind_address=conf.get('MYSQL_TEST3_TRADE', 'host'),
                   user=conf.get('MYSQL_TEST3_TRADE', 'user'),
                   passwd=conf.get('MYSQL_TEST3_TRADE', 'password'))
