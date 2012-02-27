# -*- coding: utf-8 -*-
import re, HTMLParser

def between(first, second, string):
    tmp = re.compile(first + '(.*?)' + second, re.DOTALL |  re.IGNORECASE).findall(string)
    try:
        tmp = tmp[0]
    except:
        tmp = ""
    return tmp

def all_between(first, second, string):
    return re.compile(first + '(.*?)' + second, re.DOTALL |  re.IGNORECASE).findall(string)
