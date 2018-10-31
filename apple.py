# /lib/usr/python
# Handcrafted with Love
# Kirnath x ZeroByte.ID

import requests
import sys
from termcolor import colored
import time
import threading
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings() 

class warna:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
w 		= warna.HEADER + " _   ___                  _   _     \n" + warna.ENDC
gans 	= warna.HEADER + "| | / (_)                | | | |    \n" + warna.ENDC
sangat 	= warna.HEADER + "| |/ / _ _ __ _ __   __ _| |_| |__  \n" + warna.ENDC
kirnath = warna.HEADER + "|    \| | '__| '_ \ / _` | __| '_ \ \n" + warna.ENDC
coded 	= warna.HEADER + "| |\  \ | |  | | | | (_| | |_| | | |\n" + warna.ENDC
me 		= warna.HEADER + "\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n" + warna.ENDC
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
print warna.BOLD + warna.WARNING + "                       ZeroByte.ID\n" + warna.ENDC + warna.ENDC
def main():
	start_time = time.time()
	url = 'https://www.kirnath.com/apple/index.php'
	print warna.OKBLUE + "[+] Make sure this script in Directory with your mailist file !" + warna.ENDC
	api = str(raw_input("[+] Enter your apikey: "))
	tanya = str(raw_input("[+] Enter Mailist File: "))
	mailist = open(tanya, 'r').read().split('\n')
	print "[+] ",len(mailist),"Mailist Loaded"
	live = []
	for data in mailist:
		datapost = {
		'apikey':api,
		'email':data
		}
		request = requests.post(url, data=datapost, verify=False)
		respon = str(request.text)
		if respon == "Credits isn't enough!":
			print warna.WARNING + "[ + ] Credits isn't enough!" 
			print "[ + ] Exiting in 3 seconds ..." + warna.ENDC
			sys.exit(3)
		if respon == "INVALID SECRET KEY":
			print warna.WARNING + "[ + ] Your Apikey is Invalid !"
			print "[ + ] Exiting in 3 seconds ..." + warna.ENDC
			sys.exit(3)
		if respon == "DEAD" or False:
			print warna.FAIL + "[ DIE ] ",data + warna.ENDC
		if "Valid" in respon:
			print warna.GREEN + "[ LIVE ] ",data + warna.ENDC
			liva = "[ LIVE ] ",data
			live.append(liva)
			# print "live.txt",live
		else:
			print warna.WARNING + "[ Unknown ]",data
	print warna.WARNING + "[+] Result will be saved as .txt files, enter file name below"
	tanya_lagi = str(raw_input("Enter File Name: "))
	# print "live.txt",str(live)
	string = str(live).replace("('","").replace("'),","\n").replace("'","").replace(",","")
	
	save = open(tanya_lagi+'.txt', 'a')
	# for item in live:	
	save.write('\n'+string)
	save.close()
	time_total = time.time() - start_time
	print "[ + ] All Job has finished!"
	print "[ + ] Total Time: ", time_total, " Seconds"
t=threading.Thread(target=main)
t.start()