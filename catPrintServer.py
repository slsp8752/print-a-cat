#!/usr/bin/env python2.7

import requests
import urllib
import random
import os
from scapy.all import *

def nohidden(path):
	files = os.listdir(path)
    for f in files:
        if f.startswith('.'):
			files.remove(f)
	return files
			
def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            print "ARP received"
            if pkt[ARP].hwsrc == 'a0:02:dc:7d:4e:dc': # Put your button's MAC address here
				print "Choosing Cat"
				catfname = random.choice(nohidden(os.getcwd() + "/cats"))
                print "Printing Cat!"
                os.system("lpr -r {}".format("cats/" + catfname))
                print(catfname)
                r = requests.get("http://thecatapi.com/api/images/get?format=src&size=full&type=jpg")
		urllib.urlretrieve(r.url, "cats/" + catfname)
                print "Cat Replaced"

print sniff(prn=arp_display, filter="arp", store=0)
 
