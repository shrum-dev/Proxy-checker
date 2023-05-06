import requests
import threading
from colorama import Fore, init
import os

os.system("cls")
init()

def proxy_check(proxy, mstime):
    try:
        if proxy[0:8] == "http://":
            proxies = {"http": proxy, "https": proxy}
        else:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        
        resp = requests.get("https://github.com/dontskid", proxies=proxies, timeout=int(mstime))
        if resp.status_code == 200:
            with open("checked.txt", "a") as f:
                f.write(f"{proxy}\n")
            return proxy
        else:
            return None
    except Exception as e:
        None

ref = Fore.GREEN + "(" + Fore.RESET + "+" + Fore.GREEN + ")" + Fore.RESET
print(ref, "Checking proxies..")
proxy_file = input(ref + " Enter proxy file name (Leave blank if proxy file name is `proxies.txt`) : ")
milliseconds = input(ref + " Enter MS to check proxies : ")
seconds = int(milliseconds) / 1000
formatted_time = '{:.0f}'.format(round(seconds))

if proxy_file == "":
    with open(f"proxies.txt", "r") as bitch:
        bitch = bitch.read().splitlines()
        for bitches in bitch:
            threading.Thread(target=proxy_check, args=(bitches, formatted_time,)).start()
        print(f"{ref} Checking {len(bitch)} proxies! Seconds: {int(formatted_time)}")
else:
    with open(f"{proxy_file}.txt", "r") as bitch:
        bitch = bitch.read().splitlines()
        for bitches in bitch:
            threading.Thread(target=proxy_check, args=(bitches, formatted_time,)).start()
        print(f"{ref} Checking {len(bitch)} proxies! Seconds: {int(formatted_time)}")
