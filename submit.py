#made this to submit the flags because if i reboot the board the score resets
#(found this out the hard way after half the challenges)

from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")

score = conn.readCharacteristic(0x002a)
print(score.decode())



#submit flags
conn.writeCharacteristic(0x002c,b"12345678901234567890") #flag 1
conn.writeCharacteristic(0x002c,b"d205303e099ceff44835") #flag 2
conn.writeCharacteristic(0x002c,b"5cd56d74049ae40f442e") #flag 3
conn.writeCharacteristic(0x002c,b"2b00042f7481c7b056c4") #flag 4
conn.writeCharacteristic(0x002c,b"3873c0270763568cf7aa") #flag 5
conn.writeCharacteristic(0x002c,b"c55c6314b3db0a6128af") #flag 6
conn.writeCharacteristic(0x002c,b"1179080b29f8da16ad66") #flag 7
conn.writeCharacteristic(0x002c,b"f8b136d937fad6a2be9f") #flag 8
conn.writeCharacteristic(0x002c,b"933c1fcfa8ed52d2ec05") #flag 9
conn.writeCharacteristic(0x002c,b"6ffcd214ffebdc0d069e") #flag 10
conn.writeCharacteristic(0x002c,b"5ec3772bcd00cf06d8eb") #flag 11
conn.writeCharacteristic(0x002c,b"c7b86dd121848c77c113") #flag 12
conn.writeCharacteristic(0x002c,b"c9457de5fd8cafe349fd") #flag 13
conn.writeCharacteristic(0x002c,b"b6f3a47f207d38e16ffa") #flag 14
conn.writeCharacteristic(0x002c,b"aca16920583e42bdcf5f") #flag 15
conn.writeCharacteristic(0x002c,b"b1e409e5a4eaf9fe5158") #flag 16
conn.writeCharacteristic(0x002c,b"d41d8cd98f00b204e980") #flag 17
conn.writeCharacteristic(0x002c,b"fc920c68b6006169477b") #flag 18
conn.writeCharacteristic(0x002c,b"fbb966958f07e4a0cc48") #flag 19
conn.writeCharacteristic(0x002c,b"d953bfb9846acc2e15ee") #flag 20

sleep(1)
score = conn.readCharacteristic(0x002a)
print(score.decode())

conn.disconnect()