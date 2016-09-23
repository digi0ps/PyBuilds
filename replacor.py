#digi0ps
import time;
from datetime import datetime;
now = datetime.now();
print("Welcome to REPLACOR: ");
print("Current time: %i:%i:%i" %(now.hour, now.minute, now.second));

#MAIN DICTIONARY CONTAINING ALL PAIRS:
main = {};
main["li"] = "Lithium";
main["he"] = "Helium";

#input function:
def replacor_input():
	return str(input("Enter the sentence: "));

def replacor_search(x):
	n = len(x);
	i = 0;
	keys = [];
	while i<n:
		if x[i]=='~':
			keys.append(x[i+1]+x[i+2]);
			i+=3;
		else:
			i+=1;
	for z in range(0,len(keys)):
		keys[z]=keys[z].lower();
	return keys;

def replacor_replace(x,k):
	n = len(x);
	i = 0; j = 0;
	string = str();
	while i<n:
		if x[i]=='~':
			string+=main[k[j]];
			i+=3;
			j+=1;
		else:
			string+=x[i];
			i+=1;
	return string;





#main execution
sent = replacor_input();
keyz = replacor_search(sent);
final = replacor_replace(sent, keyz);
print('\n'*5);
print("REPLACED SENTENCE: ");
print();
print(final);

#exit
input();
exit
