#GetWeather.py - Gets the current local weather
#! python3
import requests, bs4
#TODO Get accuweather website
accu = requests.get("http://www.accuweather.com");
accu.raise_for_status();
accusoup = bs4.BeautifulSoup(accu.text, "html.parser");
#TODO Find the link containing the local city
city_tab = accusoup.select("#current-city-tab a")[0];
city_link = city_tab['href'];
city_name = city_tab.span.getText();
#TODO Get the local page
localweather = requests.get(city_link);
localweather.raise_for_status();
localsoup = bs4.BeautifulSoup(localweather.text, "html.parser");
temp_container = localsoup.select(".current .info")[0];
#TODO Get the temperature and condition and print it
temp = temp_container.div.span.getText();
cond = temp_container.select(".cond")[0].getText();
print("City:", city_name);
print("\t\tTemperature:", temp,"C");
print("\t\tCondition:", cond);
input()
