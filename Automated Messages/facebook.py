#! python3 
# ~digi0ps~ 
times = 500;
text = ["Bro", "Bruh", "Dude", "xD", "<3", ":D"]
import time
from random import randint as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k
chrome = webdriver.Chrome();
chrome.get("https://www.facebook.com");
chrome.find_element_by_id("email").send_keys(input("Username: "));
chrome.find_element_by_id("pass").send_keys(input("Password: "));
time.sleep(1);
chrome.find_element_by_id("pass").send_keys(k.ENTER);
chrome.get("https://www.facebook.com/messages/" + "username");
chat = chrome.find_elements_by_class_name("_1rv")[0];

for x in range(1, times+1):
	#chat.send_keys("Square of " + str(x) +" : " + str(x**2));
	#chat.send_keys("Hi " + text[r(0,len(text)-1)]);
	#chat.send_keys(str(x)+": Go eat");
	chat.send_keys(k.ENTER);
