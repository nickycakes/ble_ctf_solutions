#Take a look at handle 0x0052. 
# Notice it does not have a notify property. 
# Do a write here and listen for notifications anyways! 
# Things are not always what they seem!

#        82      0x52    ff15    0000ff15-0000-1000-8000-00805f9b34fb    READ WRITE 
#                b'No notifications here! really?'

from bluepy.btle import Peripheral, DefaultDelegate

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

conn.writeCharacteristic(0x52,b"asdf") #apparently need to hit this first to get it to send notifications

while(1):
    conn.waitForNotifications(1)
conn.disconnect()
