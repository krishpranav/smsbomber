#!/usr/bin/env/python3

#imports
from colrama import Fore
import subprocess
import requests
import platform
import json
import time 
osname = platform.uname()[0]
def clear():
    if osname == 'Windows':
        subprocess.call(("cls"),shell=True)
    else:
        subprocess.call(("clear"),shell=True)

clear()
