#!/usr/bin/env/python3

#imports
from colorama import Fore
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

def sendsms(number):
    payload = {
        "cellphone":number
    }
    result = requests.post(
    'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp/',
    data=payload
    )
    # print(result.text)
    if result.status_code == 200:
        status = True
    else:
        status = False
        
    return status
