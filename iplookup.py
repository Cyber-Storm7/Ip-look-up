import ipwhois
from ipwhois import IPWhois
import requests
import os
import pyfiglet
import termcolor
from termcolor import colored
from pyfiglet import Figlet
import ipaddress
def is_valid_ip(ip):
    """Check if the input is a valid IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
def style_print(text, color):
    print(colored(text, color, attrs=['bold']))

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
style_print("                              [ By Cyber Storm ]", 'cyan')
print()
style_print("=================================================", 'red')
print()
style_print("[*] Welcome to IP Info Tool", 'red')
print()
style_print("[*] Note : You must connected to the internet to use the tool", 'red')
print()
url = 'https://geoip.maxmind.com/geoip/v2.1/city/'
account_id = '1104565'  
license_key = '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'  
url2 = 'https://ipinfo.io/'  
url_2 = '?token=2bf898aa276766'

while True:
    ip_address = input(colored("[*] Enter IP address as input ------> ", 'red', attrs=['bold']))
    print()
    if is_valid_ip(ip_address):
    
     response = requests.get(url + ip_address, auth=(account_id, license_key))

     if response.status_code == 200:
        style_print(f"[*] Information from MaxMind Database about IP : {ip_address}", 'red')
        print()
        style_print(response.json(), 'red')
        print()
     else:
        response2 = requests.get(url2 + ip_address + url_2)
        if response2.status_code == 200:
            ip_info = response2.json()
            style_print(f"[*] Information from ipinfo.io about IP : {ip_address}", 'red') 
            print()
            for key, value in ip_info.items():
                style_print(f"{key}: {value}", 'red')  
                print()  
        else:
            style_print(f"Error fetching data from ipinfo.io: {response2.status_code}", 'red')
    
     ip_info = IPWhois(ip_address)
     result = ip_info.lookup_rdap()
     style_print(f"[*] WHOIS Information for {ip_address} :\n", 'red')
     for key, value in result.items():
      style_print(f"{key}: {value}\n", 'red') 
     print()
    else:
        style_print(f"{ip_address} is not a valid IP address.", 'red')
        print()
