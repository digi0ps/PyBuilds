#! python3 
# ~digi0ps~ 
import time
from random import randint as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k

def gra(max_val):
	# Get random alphabet
	alpha = ["a", "b", "c", "d", "e", "d","a", "b", "c"]
	return alpha[r(0,max_val-1)]

def grn():
	# Get Random Name
	names = ['Toshiko', 'Ayesha', 'Jolyn', 'Giovanni', 'Tyler', 'Shannan', 'Carmelo', 'Lucien', 'Jenette', 'Oma']
	return names[r(0, len(names)-1)]

def justdoit(n):
	chrome = webdriver.Chrome()
	chrome.get("https://digi0ps.typeform.com/to/Stjpda")
	time.sleep(5)
	chrome.find_element_by_css_selector("body").send_keys(k.ENTER)
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(grn())
	chrome.switch_to_active_element().send_keys(k.ENTER)
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(6))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(2))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(7))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(5))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(4))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(r(3,10))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(3))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(r(13,18))
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(k.ENTER)
	time.sleep(1)
	chrome.switch_to_active_element().send_keys(gra(3))
	time.sleep(2)
	chrome.switch_to_active_element().send_keys(k.ENTER)
	time.sleep(n)
	chrome.close()

total = 100
count = 3
for i in range(1,4):
	justdoit(4)
	count+=1;