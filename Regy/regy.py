#! python3
import requests, re, json, time;
from bs4 import BeautifulSoup;
from pprint import pprint;
from os import path;

#TODO: Get moodle
passs = str(input());
payload = {
	"username": "16bce1026",
	"password": passs
}
url = 	"http://moodlecc.vit.ac.in/login/index.php";
input_ = ""
def update():
	with open(r'data\data.json', 'r') as file:
		database = json.load(file);
	tempcount = 0;
	print("\tGETTING DATA FROM MOODLE");
	req = requests.post(url, data=payload);
	soup = BeautifulSoup(req.text, "html.parser");
	print("\tPARSING DATA")
	users = soup.select(".user"); 
	userreg = re.compile(r'(.+)(\d{2}\w{3}\d{4})');
	print("\tSTORING DATA");
	for user in users:
		data = userreg.search(user.a.text);
		if data:
			name = data.group(1);
			if name[-1].isspace:
				name = name[:-1]; 
			reg = data.group(2);
			if not reg in database.keys():
				database[reg] = name;
				tempcount+=1;
	total = len(database.keys());
	with open(r'data\data.json', 'w') as file:
		database = json.dump(database, file, sort_keys = True, indent = 4);
		print("\tDATABASE UPDATED.\n\tENTRIES UPDATED: %d\n\tTOTAL ENTRIES: %d" %(tempcount, total));

def search():
	with open(r'data\data.json', 'r') as file:
		database = json.load(file);
		regno = str(input("Enter the registration number: "));
		regno = regno.upper();
		if regno in database.keys():
			print(database[regno]);
		else:
			print("Registration number not found.");

def repeat():
	i = 1;
	while i<25:
		print("Update",i);
		update();
		print("Program snoozing")
		time.sleep(300);
		i+=1;
#MAIN:

while input_ != "exit":
	input_ = str(input(">> "))
	input_ = input_.lower();
	if input_ == "update":
		update();
	elif input_ == "search":
		search();
	elif input_ == "repeat_update":
		repeat();
	elif input_ == "database":
		pprint(database);
	else:
		print("Invalid input.");
