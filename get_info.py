#importing necessary library's
import os
import platform

#printing the info
print "OS name: "+os.name
print "Platform: "+platform.system()
print "Release: "+platform.release() 
print "User: "+os.getlogin()
