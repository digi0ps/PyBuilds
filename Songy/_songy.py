#! python3
"""
Songy - Search for song names and download them
Dev: digi0ps
"""
#Imports
import requests, time
from bs4 import BeautifulSoup as bs;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as k
import os
os.makedirs("Songy", exist_ok=True);
os.chdir("Songy");
#TODO: Get input from user and parse it.
user = str(input("---Enter song name(s) separated by comma---\n"));
songs = user.split(",")
#TODO: Loop through input.
for song in songs:
	#TODO: Use Request to get youtube search 
	print("Searching for " + song);
	search = requests.get("https://www.youtube.com/results?search_query="+song);
	search.raise_for_status();
	#TODO: Use BS4 to get the url of the top search result
	bsearch = bs(search.text, "html.parser");
	top = bsearch.select(".yt-uix-tile-link")[0];
	title = top["title"];
	href = top["href"];
	url = "https://www.youtube.com"+href;
	durl = "http://www.clipconverter.cc/?ref=opensearch&url="+url;
	#TODO: Use selenium to pass the link to yout and download the file
	print("Getting " + title);
	chrome = webdriver.Chrome();
	chrome.get(durl);
	mp3button = chrome.find_elements_by_class_name("ui-button-text-only")[1];
	mp3button.click();	
	cbutton = chrome.find_elements_by_class_name("ui-corner-all")[-1];
	print(cbutton.get_attribute("href"));
	cbutton.click();
	print("Converting...");
	time.sleep(2);
	dbutton = chrome.find_element_by_id("downloadbutton");
	link = dbutton.get_attribute("href");
	print("Downloading " + title);
	#TODO: Pass link to requests and save it as an mp3
	mp3 = requests.get(link);
	mp3.raise_for_status();
	mp3_name = song+".mp3";
	mp3_file = open(mp3_name, "wb");
	for chunk in mp3.iter_content(100000):
		mp3_file.write(chunk);
	mp3_file.close();
	chrome.quit();
print("All files downloaded succcessfully.");
#TODO: Listen to email 
#TODO: If someone mails the song, get the list of songs
#TODO: Download and send the bitly links back.