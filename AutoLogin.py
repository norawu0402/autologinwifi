import time
import subprocess
import netifaces
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# comment and uncomment which browser you are using. Now is using Chrome
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

################################################################################
# uncomment which OS you're using (now is uising Linux)
#for Windows, ssid and name put your wifi AP,like my school is YZUWLAN
# subprocess.call(["netsh", "wlan", "connect", "ssid=""YZUWLAN""", "name=YZUWLAN"])
#for Linux, Chang Wifi AP's SSID
subprocess.call(["nmcli", "dev", "wifi", "connect", "YZUWLAN"])

#set website
websiteUrl = ""
#set your username and password for Login
username = ""
password = ""

#set web source code's id names
sc_username = ""
sc_password = ""
sc_submit = ""

###########################################################
# set Browser comment and uncomment which you you are using
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get((websiteUrl))
try:
	browser_user = browser.find_element_by_name(sc_username)
	browser_user.send_keys(username)
	browser_password = browser.find_element_by_name(sc_password)
	browser_password.send_keys(password)
	browser_login = browser.find_element_by_name(sc_submit)
	browser_login.click()

except Exception:
	print("Something Wrong or Wifi is Connecting")
