#!/usr/bin/env python

import sys
from argparse import ArgumentParser


def printUsage():
    print '\nUsage:'
    print 'gpioutil -p PIN_NAME'
    print 'gpioutil -c CHIP_NAME default aspeed'
    exit(1)


def convertAspeedGpio(name):
    offset = int(''.join(list(filter(str.isdigit, name))))
    port = list(filter(str.isalpha, name.upper()))
    a = ord(port[-1]) - ord('A')
    if len(port) > 1:
        a += 26
    base = a * 8
    return base + offset

ConvertFuncs = {'aspeed': convertAspeedGpio}

if __name__ == '__main__':
    parser = ArgumentParser(description="Converts pin name to key code")
    parser.add_argument('-p', '--pin', dest='pin', default='',
                        help='sfp definitional yaml')
    parser.add_argument('-c', '--chip', dest='chip', default='aspeed',
                        help='output directory')

    args = parser.parse_args()

    if(args.pin == ''):
        printUsage()

    key_code = ConvertFuncs[args.chip](args.pin)

    print("pin_name" + ":" + args.pin + "-->" +
          "key_code" + ":" + str(key_code))
