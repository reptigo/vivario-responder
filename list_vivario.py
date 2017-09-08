from socket import *
from time import gmtime, strftime

DISCOVERY_PORT = 41890
DISCOVERY_MSG  = b'VIVARIO_ARE_YOU_THERE'

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.bind(('', DISCOVERY_PORT))
cs.sendto(DISCOVERY_MSG, ('255.255.255.255', DISCOVERY_PORT))
print('Looking for Vivario in the local network...')

while True:
    message = cs.recvfrom(1024)
    if message[0].startswith(b'VIVARIO_') and message[0] != DISCOVERY_MSG:
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        serverip = message[1][0]
        print("[%s] Response from %s" % (now, serverip))
