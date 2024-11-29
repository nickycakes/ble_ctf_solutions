import binascii
from bluepy.btle import Peripheral

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")
services = conn.getServices()
for service in services:
    print(service.uuid)
    characteristics = service.getCharacteristics()
   
    for characteristic in characteristics:
        line = "\t"
        handle = characteristic.getHandle()
        line += str(handle) + "\t" + hex(handle) + "\t"
        line += str(characteristic.uuid)[4:-28] + "\t" + str(characteristic.uuid) + "\t"
        line += characteristic.propertiesToString()
        print(line)
        if characteristic.supportsRead():
            print("\t\t", end="")
            print(characteristic.read())

conn.disconnect()
