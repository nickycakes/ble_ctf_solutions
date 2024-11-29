#Check out handle 0x0048 and google search gatt indicate. 
# Keep in mind that this chalange will require you to 
# parse multiple indicate responses in order to complete the chalange.

#        72      0x48    ff10    0000ff10-0000-1000-8000-00805f9b34fb    READ 
#                b'Listen to handle 0x004a for multi indications'

#        74      0x4a    ff11    0000ff11-0000-1000-8000-00805f9b34fb    READ WRITE INDICATE 
#


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

conn.writeCharacteristic(0x4a,b"asdf") #apparently need to hit this first to get it to send indications

while(1):
    conn.waitForNotifications(1)
conn.disconnect()
