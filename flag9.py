#Take a look at handle 0x003c and do what it says. 
# You should script up a solution for this one. Also 
# keep in mind that some tools write faster than others.

#bruteforce 0x00 to 0xff



from bluepy.btle import Peripheral

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")
service = conn.getServiceByUUID("000000ff-0000-1000-8000-00805f9b34fb")
ch = service.getCharacteristics(forUUID="0000ff0a-0000-1000-8000-00805f9b34fb")[0]
#ch = ch[0]
line = ""
handle = ch.getHandle()
handle = handle
line += str(handle) + "\t" + hex(handle) + "\t"
line += str(ch.uuid)[4:-28] + "\t" + str(ch.uuid) + "\t"
line += ch.propertiesToString()
print(line)
if ch.supportsRead():
    print(ch.read())

for i in range(0,256):
    ch.write(i.to_bytes(1,'big'))
    print(ch.read())

conn.disconnect()
