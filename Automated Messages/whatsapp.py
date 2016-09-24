#! python3 
#whatsapp3 
times = 100;
text = "K! "

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k
chrome = webdriver.Chrome();
chrome.get("https://web.whatsapp.com");
time.sleep(25);
d = chrome.find_elements_by_class_name("input")[1]
for i in range(times): 
	d.send_keys(text * i); 
	d.send_keys(k.ENTER);