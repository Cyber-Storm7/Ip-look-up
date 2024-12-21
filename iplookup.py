import requests
import os
import pyfiglet
import termcolor
from termcolor import colored
from pyfiglet import Figlet
def style_print(text, red):
    print(colored(text,red, attrs=['bold']))
def check_and_cast(input_value):
    try:
        return float(input_value)
    except ValueError:
        print()
        style_print("[*] Invalid input", 'red')
os.system("clear")
style_print("=================================================", 'red')
print()
figlet = Figlet(font="slant")
ascii_banner = figlet.renderText("  IP Info")
lines = ascii_banner.split('\n')
colors = ["red"]
for i, line in enumerate(lines):
    color = colors[i % len(colors)]
    print(colored(line, color))
style_print("                              [ By Cyber Storm ]",'cyan')
print()
style_print("=================================================", 'red')
print()
style_print("[*] Welcome to Ip Info Tool", 'red')
print()
url = 'https://geoip.maxmind.com/geoip/v2.1/city/'

account_id = '1104565'  

license_key = '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'  
while True:
 ip_address = (input(colored("[*] Enter IP address as input ------> ", 'red', attrs=['bold'])))
 print()
 response = requests.get(url + ip_address, auth=(account_id, license_key))

 if response.status_code == 200:
    style_print(response.json(), 'red')
    print()
 else:
    style_print(f'[*] Error: {response.status_code}', "red")
    print()
