#! python3
#2048.py - Automated Playing Of The Online Game 2048
#digi0ps
#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time, sys
#Declaration
arrows = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT];
chrome = webdriver.Chrome();
chrome.get("https://gabrielecirulli.github.io/2048/");
body = chrome.find_element_by_tag_name('body');
retry = chrome.find_elements_by_class_name("retry-button")[0];
score = chrome.find_elements_by_class_name("score-container")[0];
best = chrome.find_elements_by_class_name("best-container")[0];
scores = [];
play = 'yes';
#Core
def main():
	while not len(chrome.find_elements_by_class_name("game-over")):
		n = randint(0,3);
		body.send_keys(arrows[n]);
	time.sleep(1);
	print("Your score:", score.text, "Best Score:", best.text);
	scores.append(int(score.text));
#Main
if len(sys.argv)>1:
	n = int(sys.argv[1]);
	for i in range(n):
		print("Try", i+1);
		main();
		retry.click();
else:		
	while play=="yes":
		main();
		play = str(input("Do you wanna again? (yes/no): ")).lower();
		retry.click();
input();
chrome.quit();
