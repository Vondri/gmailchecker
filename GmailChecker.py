__AUTHOR__ = "Vondri"
__VERSION__ = "1.0.0"
__GITHUB__ = "https://github.com/Vondri"

import sys
import os
import requests
import argparse
import time

def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')

def options():
    parser = argparse.ArgumentParser(description='The script was written to check the Gmail account')
    parser.add_argument('-u', '--userlist', help='File with users to be checked.', required=False)
    parser.add_argument('-o', '--output', help='Writes valid emails to text file.', action='store_true', required=False)
    parser.add_argument('-s', '--silent', help='Running script without banner.', action='store_true', required=False)
    parser.add_argument('-i', '--invalid', help='Writes invalid emails to the file.', action='store_true', required=False)
    parser.add_argument('-t', '--timeout', help='Set timeout between checks.', type=int, required=False)
    parser.add_argument('-e', '--email', help='Single email address to check.', required=False)
    global args
    args = parser.parse_args()

def handler():
    if len(sys.argv) == 1:
        print('\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] Enter something argument [!\033[38;5;245m]\033[0m')
        sys.exit(0)
    if args.userlist:
        try: open(args.userlist)
        except FileNotFoundError: 
            print('\033[38;5;245m[\033[38;5;9m!] Userlist not found [!\033[38;5;245m]\033[0m')
            sys.exit(0)
    if args.email:
        if not check_address(args.email):
            print('\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] Add @gmaill.com at the end of email [!\033[38;5;245m]\033[0m')
            sys.exit(0)

def banner():
    print(f''' 
\033[1m\033[38;5;21m ██████╗ ███╗   ███╗ █████╗ ██╗██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗\033[0m
\033[1m\033[38;5;27m██╔════╝ ████╗ ████║██╔══██╗██║██║     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗\033[0m
\033[1m\033[38;5;33m██║  ███╗██╔████╔██║███████║██║██║     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝\033[0m
\033[1m\033[38;5;39m██║   ██║██║╚██╔╝██║██╔══██║██║██║     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗\033[0m
\033[1m\033[38;5;45m╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║\033[0m
\033[1m\033[38;5;51m ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\033[0m
       \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mAuthor: {__AUTHOR__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mVersion: {__VERSION__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mGithub: {__GITHUB__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m                                                                                               
     ''')

def check_address(val):
    if args.email:
        if "@gmail.com" in val: return True
        else: 
            args.email += '@gmail.com'
            return True
    if args.userlist:
        if '@gmail.com' in val: return val
        else:
            val += '@gmail.com'
            return val

def single_check(val):
    req = requests.Session()
    request = req.get('https://mail.google.com/mail/gxlu?email=' + val).cookies
    if len(request.items()) > 0:
        print(f'\033[38;5;245m[\033[38;5;10m+\033[38;5;245m]\033[0m {val}')
    else:
        print(f'\033[38;5;245m[\033[38;5;9m-\033[38;5;245m]\033[0m {val}')

def check_from_file(path):    
    if args.output:
        localtime = time.localtime()
        strTime = time.strftime('%m-%d-%Y_%H-%M-%S', localtime)
        voutput = open(strTime+' Valid Users.txt', 'w')
        print('\033[38;5;245mValid users file output: \033[0m',str(strTime), ' Valid Users.txt')
    if args.invalid:
        localtime = time.localtime()
        strTime = time.strftime('%m-%d-%Y_%H-%M-%S', localtime)
        ioutput = open(strTime+' Invalid Users.txt', 'w')
        print('\033[38;5;245mInvalid users file output: \033[0m', str(strTime)+' Invalid Users.txt')
    userlist = open(path, 'r')
    userlist = userlist.readlines()
    print('\033[38;5;245m=\033[0m'*50)
    for user in userlist:
        user = user.strip()
        user = check_address(user)
        req = requests.Session()
        request = req.get('https://mail.google.com/mail/gxlu?email=' + user).cookies
        if len(request.items()) > 0:
            if args.output:
                voutput.write(user+'\n')
            print(f'\033[38;5;245m[\033[38;5;10m+\033[38;5;245m]\033[0m {user}')
        else:
            if args.invalid:
                ioutput.write(user+'\n')
            print(f'\033[38;5;245m[\033[38;5;9m-\033[38;5;245m]\033[0m {user}') 
        if args.timeout:
            time.sleep(args.timeout)
    if args.output:
        voutput.close()
    if args.invalid:
        ioutput.close()
    print('\033[38;5;245m=\033[0m'*50)

if __name__ == '__main__':
    try:
        clear()
        options()

        if not args.silent:
            banner()

        handler()

        if args.email:
            single_check(args.email)
        if args.userlist:
            check_from_file(args.userlist)
        print('\n'*3)
    except KeyboardInterrupt:
        print('Goodbye ^^/')
        sys.exit(0)