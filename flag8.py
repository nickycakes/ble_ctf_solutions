#Follow the instructions found from reading handle 0x0038. 
# Pay attention to handles here. Keep in mind handles can 
# be refrenced by integer or hex. Most tools such as 
# gatttool and bleah allow you to specify handles both ways.

#        56      0x38    ff08    0000ff08-0000-1000-8000-00805f9b34fb    READ 
#                b'Write 0xC9 to handle 58'



from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0038).decode()) #read from handle 0x38
conn.writeCharacteristic(58,0xc9.to_bytes()) #write to handle decimal 58 (0x3a)
sleep(.25)
print(conn.readCharacteristic(0x0038).decode()) #read from handle 0x38

conn.disconnect()