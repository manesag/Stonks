import yahoofinance
import os
import time
import json
import subprocess

print("Please enter a stock ticker:")
anyvalue = input()

exe = "python yahoofinance.py "
uwu = exe + anyvalue

os.system(uwu)

time.sleep(1)

why = "-summary.json"
imsai = anyvalue + why

f = open(imsai)

data = json.load(f)

beta = data['Beta (5Y Monthly)']

print(beta)

string =  data['52 Week Range']
lowEnd, highEnd = string.split(' - ')
print(lowEnd)
print(highEnd)
   
f.close()

os.remove(imsai)