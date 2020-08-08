import subprocess
import requests
import time

################################################################################
#for Linux, Chang Wifi AP's SSID
subprocess.call(["nmcli", "dev", "wifi", "connect", "YZUWLAN"])

#set website
websiteUrl = ""
#set your username and password for Login
data = {
    'user': '',
    'password': '',
}
#set website header's
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}

#########################################################################################################################
try:
    session = requests.Session()
    session.post(websiteUrl, headers=headers, data=data)
    time.sleep(2)
    
except Exception:
	print("Something Wrong or Wifi is Connecting")
