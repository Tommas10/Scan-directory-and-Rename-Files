#!/usr/bin/env python

#This is small auto Python script file to scan directory and rename files. Under macOS.
#Created by Tommas Huang 
#Created date: 2019-07-23


import os
#The OS module in Python provides a way of using operating system dependent functionality. 
#The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux. 

path = '/Users/TommasHuang/Desktop/Test2'
#Need rename file directory path.
for filename in os.listdir(path):
#The os.listdir() method is used to return a list of the names of the files or folders contained in the specified folder.
    if filename.startswith("test"):
    #The method startswith() checks whether string starts with str, optionally restricting the matching with the given indices start and end.
        print ("found")
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("test_", " ")))
        #When you rename you should use the full path.
    else:
        continue