#Read handle 0032 and do what it says. Notice that its not telling you 
# to write to the flag handle as you have been. When you find the flag, 
# go ahead and write it to the flag handle you have used in the past flags.

#        50      0x32    ff05    0000ff05-0000-1000-8000-00805f9b34fb    READ WRITE 
#                b'Write anything here'



from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0032).decode()) #read from handle 32
conn.writeCharacteristic(0x0032,b"asdf") #write to handle 32
sleep(.25)
print(conn.readCharacteristic(0x0032).decode()) #read from handle 32

conn.disconnect()