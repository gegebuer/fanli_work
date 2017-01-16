#!python
#!-*- coding: utf-8 -*-

import sys

def eliminateErrorChar(old_column):
    try:
        new_column = ''
        for ch in old_column:
            ascii = ord(ch)
            if ascii >= 19968 and ascii <= 40869:
                new_column += ch
            elif ascii >= 1 and ascii <= 127:
                new_column += ch
            else :
                new_column += '*'
        return new_column
    except:
        return '*'
    
def isNullOrNo(str_target):
    if str_target is None or str_target == '':
        return '*'
    else:
        return str_target
    
for line in sys.stdin:
    try:
        (dv_id, user_name, real_name, duixian_realname) = line.strip().split('\t')
        user_name = isNullOrNo(user_name)
        real_name = isNullOrNo(real_name)
        duixian_realname = isNullOrNo(duixian_realname)
        user_name = user_name.decode('utf-8')
        real_name = real_name.decode('utf-8')
        duixian_realname = duixian_realname.decode('utf-8')
        user_name = eliminateErrorChar(user_name)
        real_name = eliminateErrorChar(real_name)
        duixian_realname = eliminateErrorChar(duixian_realname)
        print '\t'.join([dv_id, user_name.encode('utf-8'), real_name.encode('utf-8'), duixian_realname.encode('utf-8')])
    except:
        pass

