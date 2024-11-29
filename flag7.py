#Follow the instructions found from reading handle 0x0036. 
# Keep in mind that some tools only write hex values while 
# other provide methods for writing either hex or ascii

#        54      0x36    ff07    0000ff07-0000-1000-8000-00805f9b34fb    READ WRITE 
#                b'Write the hex value 0x07 here'


from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0036).decode()) #read from handle 36
conn.writeCharacteristic(0x0036,0x07.to_bytes()) #write to handle 36
sleep(.25)
print(conn.readCharacteristic(0x0036).decode()) #read from handle 36

conn.disconnect()