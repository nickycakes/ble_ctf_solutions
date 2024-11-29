#Check out handle 0x0040 and google search gatt notify. 
# Some tools like gatttool have the ability to subscribe 
# to gatt notifications

#    64      0x40    ff0c    0000ff0c-0000-1000-8000-00805f9b34fb    READ WRITE NOTIFY 
#            b'Listen to me for a single notification'

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

conn.writeCharacteristic(0x40,b"asdf") #apparently need to hit this first to get it to send notifications

while(1):
    conn.waitForNotifications(1)
conn.disconnect()
