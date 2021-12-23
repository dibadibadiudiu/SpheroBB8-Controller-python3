import socket
import traceback
from time import ctime

class Car():

    car = False

    def get(self):
        try:
            hostname = '192.168.4.1'
            port = 7777
            addr = (hostname,port)
            clientsock = socket.socket() ## 创建一个socket
            clientsock.connect(addr) # 建立连接
            self.car = clientsock

        except Exception as ex:
            ex_type, ex_val, ex_stack = sys.exc_info()
            traceback.print_exc()
            print(ex_type)
            print(ex_val)
    
    def run(self,content):
        try:
            print('send data'+content)
            self.car.send(content.encode("utf-8"))
        except Exception as ex:
            ex_type, ex_val, ex_stack = sys.exc_info()
            traceback.print_exc()
            print(ex_type)
            print(ex_val)

    def close(self):
        self.car.close()

carclient = Car()
