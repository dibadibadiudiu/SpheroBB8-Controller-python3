from bluepy import btle
import struct
import traceback
import BB8_driver
import sys
import time

class BB8():

    bb8 = False
    
    def connect(self):
        try:
            print('connect bb8...')
            self.bb8 = BB8_driver.Sphero()
            self.bb8.connect()
            self.bb8.start()
            time.sleep(2)
            self.bb8.roll(5,120,1,False)
        except Exception as ex:
                ex_type, ex_val, ex_stack = sys.exc_info()
                traceback.print_exc()
                print(ex_type)
                print(ex_val)

    def reconnect(self):
        try:
            print('reconnect bb8...')
            self.connect()
            return True
        except Exception as ex:
                ex_type, ex_val, ex_stack = sys.exc_info()
                traceback.print_exc()
                print(ex_type)
                print(ex_val)

    def get(self):
        if self.bb8 == False:
                self.connect()
                return self.bb8
        else:
            return self.bb8

    def roll(self,speed,angle):
        self.bb8.roll(speed,angle,1,False)
        self.bb8.join()

    def colse(self):
        self.bb8.disconnect()
        self.bb8 = False
        return True

bb8client = BB8()
