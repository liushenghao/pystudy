# -*- coding: utf-8 -*-

import argparse
import chardet
def detectCode(file):
    with open(file,'rb')as f:
        data=file.read(20000)
        dicts = chardet.detect(data)
    return dicts['encoding']
def main():
    parser= argparse.ArgumentParser()
    parser.add_argument('file','--codes',help='give the codes and the file',type =str)
    args = parser.parse_args()

    if args.codes:
        f= open(args.file,'r',encoding =args.codes)
        for line in f:
            b_line = line.encode('utf-8')
            print(b_line)
        f.close()
    else:
        f= open(args.file,'r',encoding =detectCode(args.file))
        for line in f:
            b_line = line.encode('utf-8')
            print(b_line)
        f.close()
