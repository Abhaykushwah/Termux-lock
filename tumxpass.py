import os
change_your_username_here = "root"
change_your_password_here = "1290"
## checking user_name
def enteruname():
	uname = str(input("\033[1;32;40mEnter user name :"))
	if uname == change_your_username_here:
		enterpasswd()
	else:
		enteruname()


### checking password
def enterpasswd():
	passwd = str(input("Enter passwor :"))
	if passwd == change_your_password_here:
		print("Nothing")
	else:

		enteruname()
##calling of function to run the script
enteruname()
os.system('clear')
print('''		 𝕮𝖞𝖇𝖊𝖗𝕴𝖓𝖋𝖔
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬''')
