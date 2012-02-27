# -*- coding: utf-8 -*-
import time, getpass, os, urllib2, random, cre
disable_logging = False

def query_string(msg):
	return "[+] %s | %s" % (time.strftime("%H:%M:%S"), str(msg))

def log(msg):
	if not disable_logging:
		print query_string(msg)

def push(msg):
	if not disable_logging:
		os.write(1, "\r" + query_string(msg))

def input(query):
	return raw_input(query_string(query))

def pwinput(query):
	return getpass.getpass(query_string(query))

def ensure_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def dump(data):
	open("dump", 'w').write(data)

def external_ip():
	return cre.between("<title>What's My IP - Your IP is: ", "</title>", urllib2.urlopen("http://whatsmyip.net/").read())

