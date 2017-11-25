#! python3 
# ~digi0ps~ 
times = 100;
text = ["Bro", "Bruh", "Dude", "xD", "<3", ":D"]
smileys = ["<3", ":D", ":P", "-_-", "xD", "xP"]
import time
from random import randint as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k
user = str(input("Username: "));
pwd = str(input("Password: "));
target = str(input("Target username: "));
chrome = webdriver.Chrome();
chrome.get("https://www.messenger.com");
chrome.find_element_by_id("email").send_keys(user);
chrome.find_element_by_id("pass").send_keys(pwd);
time.sleep(1);
chrome.find_element_by_id("pass").send_keys(k.ENTER);
chrome.get("https://www.facebook.com/messages/" + target);
chat = chrome.find_elements_by_class_name("_1rv")[0];
for x in range(1, times+1):
	chat.send_keys("Square of " + str(x) +" : " + str(x**3));
	#chat.send_keys("Hi Karapampoochi " + smileys[r(0,len(text)-1)]);
	#chat.send_keys("DONT SEND " * x);
	chat.send_keys(k.ENTER);
