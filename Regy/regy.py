#! python3
import requests, re, json, time;
from bs4 import BeautifulSoup;
from pprint import pprint;
from os import path;
from datetime import datetime

#TODO: Get moodle
payload = {
	"username": "16bce1026",
	"password": "password(M00DLE);"
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
#TODO: 
def search():
	with open(r'data\data.json', 'r') as file:
		database = json.load(file);
		print("1. Search by RegNo\n2. Search by Year\n3. Search by Dept\n4. Search by Name\n");
		c = int(input("Enter choice: ")); #choice variable
		if c==1:
			print("Enter registration number: ");
			ureg = str(input());
			flag = 0;
			for reg in database.keys():
				if ureg.upper()==reg:
					flag = 1;
					print("FOUND:", database[reg]);
					break;
		elif c==2:
			print("Enter the last two digits of the year: ");
			uyear = str(input()); 
			flag = 0;
			total = 0;
			for reg in database.keys():
				if uyear==reg[0:2]:
					flag = 1;
					print(database[reg],"-",reg);
					total+=1;
			print("\nTotal Entries:", str(total));
		elif c==3:
			print("Enter the department: ");
			udept = str(input()); 
			flag = 0;
			total = 0;
			for reg in database.keys():
				if udept.upper()==reg[2:5]:
					flag = 1;
					print(database[reg],"-",reg);
					total+=1;
			print("\nTotal Entries:", str(total));
		elif c==4:
			print("Enter the name: ");
			uname = str(input()); 
			flag = 0;
			total = 0;
			for reg, name in database.items():
				if uname.upper() in name.upper():
					flag = 1;
					print(name,"-",reg);
					total+=1;
			print("\nTotal Entries:", str(total));
		else:
			print("Invalid input");
			return;
		if not flag:
			print("Entry not found. ");
		return;

def repeat():
	i = 1;
	while i:
		n = datetime.now();
		print("\n\nTime:", str(n.hour)+":"+str(n.minute));
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
