# -*- coding=utf8 -*-
from __future__ import print_function

import sys
import json
import time

from colorprint import print


filename = sys.argv[1]
members = json.load(open(filename))

def choose_loop():
    member_list = [m['name'] for m in members]

    while 1:
        # list all
        for i, m in enumerate(member_list):
            try:
                print.green(format(i,'02d'), m)
            except:
                print.red(format(i, '02d'), repr(m))
        # choose
        try:
            num = raw_input('choose one to extract as simgle file: ')
        except KeyboardInterrupt:
            exit()
        # check validation
        try:
            m = members[int(num)]
            with open(m['name'], 'w') as fp:
                fp.write(m['source'].encode('utf8'))
        except (ValueError, IndexError):
            print.red('THE INPUT IS WRONG')
            time.sleep(2)

def extract_all():
    print.blue('be sure where you run this program,\n'
               'all will be extract there')
    time.sleep(5)
    for m in members:
        with open(m['name'], 'w') as fp:
            fp.write(m['source'].encode('utf8'))


if __name__=='__main__':
    while 1:
        try:
            num = raw_input('1: extract_all ; 2: choose_loop => ')
            if num not in ('1', '2'):
                print.red('please choose one of them')
                time.sleep(2)
                print('='*20)
            else:
                (extract_all if num=='1' else choose_loop)()
        except KeyboardInterrupt:
            exit()
        
