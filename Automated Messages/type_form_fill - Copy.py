#! python3 
# ~digi0ps~ 
import time
from random import randint as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k

USERNAME = "16BCE1026"
PASSWORD = "password(FALL17);"

def get(c, sel):
	return c.find_element_by_css_selector(sel);

def gets(c, sel):
	return c.find_elements_by_css_selector(sel);

def justdoit():
	chrome = webdriver.Chrome()
	chrome.get("https://academicscc.vit.ac.in/WINSEM201617_FEEDBACK/")
	get(chrome, ".textbox2").send_keys(USERNAME);
	get(chrome, ".textbox").send_keys(PASSWORD);
	time.sleep(10);
	get(chrome, ".submit3").click();
	time.sleep(3);
	post_elements = gets(chrome, ".submit3")
	print(post_elements);

justdoit();