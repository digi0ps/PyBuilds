#! python3
# pw.py - An insecure password manager
import sys, pyperclip, time;
usernames = {}
passwords = {}
arg = sys.argv[1];
if not arg:
    print("ENTER ARGUMENT: either 'add' or an 'username'");
    quit();
elif arg == "add":
        website = str(input("Enter the website address: "));
        user = str(input("Enter your username in the website: "));
        pwd = str(input("Enter your passwrod in the website: "));
        usernames[website] = user;
        passwords[user] = pwd;
        print("Saving...");
        time.sleep(1);
        print("Username and Password saved. ");
        quit();
elif arg in usernames:
        user = usernames[arg]
        pwd = passwords[user];
        print("Username : "+str(user));
        pyperclip.paste(pwd);
        print("Password: Has been copied to clipboard. ");
else:
    print("Invalid Argument. ");
