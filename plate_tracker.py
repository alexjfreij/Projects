# Program to read a jpg files and convert it to one file 
# with data that has a time stamp from the file and convert 
# the content of the file into a character string of license plate 
# and date and time to process
#
#

import os, datetime, time
from datetime import datetime
from os.path import getmtime

import argparse, csv, struct, array, sys, operator, binascii, keyword, os, string
import subprocess, re, codecs
from subprocess import Popen, PIPE
from shutil import copyfile


#entries = os.listdir('plates/')
#for entry in entries:
#    print(entry)

# detect car coming in park
# 

# Take a snapshot
#

file="arabic.jpg"
file="alex.jpg"

# get time and date
#******************
str1 = time.ctime(os.path.getctime(file)) # retrieve Date and Time
datetime_object = datetime.strptime(str1, '%a %b %d %H:%M:%S %Y')
# print (datetime_object)
line = datetime_object.strftime("%m/%d/%Y    %H:%M:%S \n \n" ) # Date format change to 06/07/2013
#print (datetime_object.strftime)

#image_lp = open(file, 'rb')

#get license plates
#******************
command ="alpr.exe -c eu -n 1 " + file +" >> text.txt"	
subprocess.call(command, shell=True)

#with open('text.txt', 'r') as f:     # load file
#    lines = f.read().splitlines()  # read lines
#    lines = lines[10:10]
    #print (lines)
f = open('text.txt','r')
lines =f.read()
lines = lines[24:33]
f.close()

command ="del text.txt"
subprocess.call(command, shell=True)
	
fw = open("tracker.txt", "a")
fw.write(lines+line)
fw.close()