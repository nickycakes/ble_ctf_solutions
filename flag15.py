#Check out handle 0x004c and do what it says. 
# Much like ethernet or wifi devices, you can 
# also change your bluetooth devices mac address.

#       76      0x4c    ff12    0000ff12-0000-1000-8000-00805f9b34fb    READ 
#                b'Connect with BT MAC address 11:22:33:44:55:66'

#doesn't seem possible to do this on a per-connection basis.  need to use 3rd party tool to change first
#used a CSR dongle with sudo bdaddr -r -t 11:22:33:44:55:66 and then replugged the usb to the vm without removing it

#uart log from esp32:
#I (6920781) ESP_GATTS_DEMO: 11 22 33 44 55 66
#I (6920791) ESP_GATTS_DEMO: THIS IS THE MAC YOU ARE LOOKING FOR

#replugging CSR dongle put its mac address back to original value


from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x004c).decode()) #read from handle 36


conn.disconnect()