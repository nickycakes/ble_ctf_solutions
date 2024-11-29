#Check out handle 0x0042 and google search gatt indicate. 
# For single response indicate messages, like this challenge, 
# tools such as gatttool will work just fine.

#        66      0x42    ff0d    0000ff0d-0000-1000-8000-00805f9b34fb    READ 
#                b'Listen to handle 0x0044 for a single indication'



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

conn.writeCharacteristic(0x44,b"asdf") #apparently need to hit this first to get it to send notifications

while(1):
    conn.waitForNotifications(1)
conn.disconnect()
