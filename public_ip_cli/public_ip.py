#!/usr/bin/python3


import requests as rq
from colorama import Fore, Style


# ansi color definitions
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
reset = Fore.RESET



def get_public_ip() -> str:
    result = rq.get('https://api.ipify.org/?format=json')
    ip_dict = result.json()
    public_ip_address = ip_dict['ip']
    return public_ip_address


def get_public_ip_origin(target_ip) -> str:
    result = rq.get(f'https://ipinfo.io/{target_ip}/geo')
    ip_origin_details_dict = result.json()
    return ip_origin_details_dict


def main():
    # api call to retrive public ip address
    returned_public_ip = get_public_ip()
    # api call to retrive json list of ip origin details
    origin_details = get_public_ip_origin(returned_public_ip)
    # Print data from API calls
    print(f'ip address: {green}{returned_public_ip}{reset}')
    #[ip_dict['city'], ip_dict['country'], ip_dict['region'], ip_dict['loc'], ip_dict['postal'], ip_dict['timezone']]
    #print(f"Public ip: {green}{origin_details['ip']} {reset}") # uncomment line if other API stops working
    print(f"City: {green}{origin_details['city']} {reset}")
    print(f"Country: {green}{origin_details['country']} {reset}")
    print(f"Region: {green}{origin_details['region']} {reset}")
    print(f"Long/Lat: {green}{origin_details['loc']} {reset}")
    print(f"Postal: {green}{origin_details['postal']} {reset}")
    print(f"Timezone: {green}{origin_details['timezone']} {reset}")
    

if __name__ == '__main__':
    main()



