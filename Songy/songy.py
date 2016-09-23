#! python3
# Song Downloader
#TODO: Declare variables
import requests, bs4, os;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
youtube = 
os.makedirs("Songy Downloads", exist_ok=True);
os.chdir("Songy Downloads");
path = os.getcwd();
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36"}
#TODO: Store the song(s) name from the user separated by a comma
user_input = str(input("Enter <song name> <artist> separated by comma:\n"));
songs = user_input.split(",");
#TODO: Loop through the songs name and do a musicpleer search of the names
#http://musicpleer.cc/#!photograph+ed+sheeran
for song in songs:
	