#Talke a look at handle 0x003e and do what it says. 
# Keep in mind that some tools have better connection speeds 
# than other for doing reads and writes. This has to do with 
# the functionality the tool provides or how it uses cached 
# BT connections on the host OS. Try testing different tools 
# for this flag. Once you find the fastest one, whip up a script 
# or bash 1 liner to complete the task. FYI, once running, this 
# task takes roughly 90 seconds to complete if done right.

#        62      0x3e    ff0b    0000ff0b-0000-1000-8000-00805f9b34fb    READ 
#                b'Read me 1000 times'

from bluepy.btle import Peripheral

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")
service = conn.getServiceByUUID("000000ff-0000-1000-8000-00805f9b34fb")
ch = service.getCharacteristics(forUUID="0000ff0b-0000-1000-8000-00805f9b34fb")[0]
line = ""
handle = ch.getHandle()
handle = handle
line += str(handle) + "\t" + hex(handle) + "\t"
line += str(ch.uuid)[4:-28] + "\t" + str(ch.uuid) + "\t"
line += ch.propertiesToString()
print(line)
if ch.supportsRead():
    print(ch.read())

for i in range(0,1001):
    print(ch.read() + str(i).encode("utf-8")) 
print(ch.read())

conn.disconnect()
