#Figure out the authors twitter handle and do what 0x0056 tells you to do!

#        86      0x56    ff17    0000ff17-0000-1000-8000-00805f9b34fb    READ 
#                b"md5 of author's twitter handle"

#@hackgnar

from bluepy.btle import Peripheral
from hashlib import md5
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x0056).decode())

print(md5("@hackgnar".encode()).hexdigest()[0:20])



conn.disconnect()