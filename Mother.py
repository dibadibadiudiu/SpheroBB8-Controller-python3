# coding=UTF-8
#!/usr/bin/python

import time
from BB8 import bb8client
from Car import carclient
import json
import traceback

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print(self.data)
        data = json.loads(self.data)
        if data["name"] == 'bb8':
            if data["type"] == 'connect':
                if bb8client.get():
                    self.sendMessage('BB8准备就绪')
                else:
                    if bb8client.reconnect():
                            self.sendMessage('BB8准备就绪')
                    else:
                            self.sendMessage('BB8准备失败，请重新启动')
            if data["type"] == 'close':
                bb8client.colse()
            if data["type"] == 'control':
                if(data["angle"] != -1):
                    bb8client.roll(100,data["angle"])
        if data["name"] == 'car':
            if data["type"] == 'connect':
                self.sendMessage('正在打开服务端并等待小车连接')
                carclient.get()
                self.sendMessage('小车准备就绪')
            if data["type"] == 'control':
                if data["angle"] == 0:
                    carclient.run('c')
                if data["angle"] == 90:
                    carclient.run('a')
                if data["angle"] == 180:
                    carclient.run('d')
                if data["angle"] == 270:
                    carclient.run('b')
                if data["angle"] == -1:
                    carclient.run('e')
                print('未识别的指令',data["angle"])

            if data["type"] == 'close':
                carclient.close()
            self.sendMessage('未识别的小车指令')
        self.sendMessage('未识别的指令')

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('0.0.0.0', 888, SimpleEcho)
server.serveforever()

