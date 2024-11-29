#Check out all of the handle properties on 0x0054! 
# Poke around with all of them and find pieces to your flag.

#        84      0x54    ff16    0000ff16-0000-1000-8000-00805f9b34fb    BROADCAST READ WRITE NOTIFY EXTENDED PROPERTIES 
#                b'So many properties!'

#07e4a0cc48
#fbb966958f
from bluepy.btle import Peripheral, DefaultDelegate
from time import sleep 

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    
    def handleNotification(self, cHandle, data):
        print("-----")
        print(cHandle)
        print(data)
        return super().handleNotification(cHandle, data)

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")
conn.setDelegate(MyDelegate())

conn.writeCharacteristic(0x54,b"asdf") #apparently need to hit this first to get it to send notifications
sleep(.25)
print(conn.readCharacteristic(0x54))

while(1):
    conn.waitForNotifications(1)
conn.disconnect()
