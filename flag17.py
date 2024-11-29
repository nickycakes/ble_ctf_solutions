#Check out handle 0x0050 and do what it says. 
# This chalange differs from other write chalanges 
# as your tool that does the write needs to have write 
# response ack messages implemente correctly. 
# This flag is also tricky as the flag will come back 
# as notification response data even though there is no "NOTIFY" property.

#        80      0x50    ff14    0000ff14-0000-1000-8000-00805f9b34fb    READ WRITE 
#                b"Write+resp 'hello'  "

from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0050).decode()) #read from handle 50

conn.writeCharacteristic(0x0050, b"hello", withResponse=True)

sleep(1)

print(conn.readCharacteristic(0x0050).decode()) #read from handle 50

conn.disconnect()