#Read handle 0x004e? and do what it says. 
# Setting MTU can be a tricky thing. Some tools may provide mtu flags, 
# but they dont seem to really trigger MTU negotiations on servers. 
# Try using gatttool's interactive mode for this task. By default, the 
# BLECTF server is set to force an MTU size of 20. The server will listen 
# for MTU negotiations, and look at them, but we dont really change 
# the MTU in the code. We just trigger the flag code if you trigger 
# an MTU event with the value specified in handle 0x0048. GLHF!

#        78      0x4e    ff13    0000ff13-0000-1000-8000-00805f9b34fb    READ 
#                b'Set your connection MTU to 444'

# using gatttool interactive to set mtu, doesn't seem to be a thing in bluepy

#[C8:2E:18:F1:6A:52][LE]> connect
#Attempting to connect to C8:2E:18:F1:6A:52
#Connection successful
#[C8:2E:18:F1:6A:52][LE]> mtu 444
#MTU was exchanged successfully: 444
#[C8:2E:18:F1:6A:52][LE]> char-read-hnd 0x4e
#Characteristic value/descriptor: 62 31 65 34 30 39 65 35 61 34 65 61 66 39 66 65 35 31 35 38



from bluepy.btle import Peripheral
from time import sleep

conn = Peripheral(deviceAddr="C8:2E:18:F1:6A:52")


print(conn.readCharacteristic(0x004e).decode()) #read from handle 4e


conn.disconnect()