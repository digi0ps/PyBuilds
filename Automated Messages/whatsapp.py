#! python3 
#whatsapp3 
text = str(input("Enter text to send: "));
times = int(input("Enter number of times: "));

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k
chrome = webdriver.chrome();
chrome.get("https://web.whatsapp.com");
time.sleep(30);
d = chrome.find_elements_by_class_name("input")[1]
for i in range(times): 
	d.send_keys(text * i); 
	d.send_keys(k.ENTER);