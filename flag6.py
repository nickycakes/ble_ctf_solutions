#Follow the instructions found from reading handle 0x0034. 
# Keep in mind that some tools only write hex values while 
# other provide methods for writing either hex or ascii

#        52      0x34    ff06    0000ff06-0000-1000-8000-00805f9b34fb    READ WRITE 
#                b'Write the ascii value "yo" here'



from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0034).decode()) #read from handle 34
conn.writeCharacteristic(0x0034,b"yo") #write to handle 34
sleep(.25)
print(conn.readCharacteristic(0x0034).decode()) #read from handle 34

conn.disconnect()