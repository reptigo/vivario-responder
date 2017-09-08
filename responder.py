import random
from socket import *
from time import gmtime, strftime

DISCOVERY_PORT = 41890

cs = socket(AF_INET, SOCK_DGRAM)
cs.bind(('', DISCOVERY_PORT))

# Completely useless variation in the possible answers
answers = [
    b'HELLO',
    b'I_AM_HERE',
    b'I_LIKE_SPACE',
    b'PLEASE_HELP_ME',
    b'LEAVE_ME_ALONE',
    b'RUN_RABBIT_RUN',
    b'WAITING_FOR_YOU',
    b'WHAT_CAN_I_DO_FOR_YOU',
    b'KING_ARTHUR_FOR_THE_WIN',
    b'I_AM_BUSY_MINING_BITCOINS',
    b'MARMELADE_A_LOT_MARMELADE',
]
while True:
    message = cs.recvfrom(1024)
    if message[0].startswith(b'VIVARIO_ARE_YOU_THERE'):
        now = strftime('%Y-%m-%d %H:%M:%S', gmtime())
        serverip = message[1][0]
        print("[%s] %s is looking for us!" % (now, serverip))

        answer = b"VIVARIO_%s" % random.choice(answers)
        cs.sendto(answer, (serverip, DISCOVERY_PORT))
