# @author Ryan Sidebottom
# Do not reproduce this. Feel free to use this or modify it.

# This script is designed to parse a log file, locate when a user
# is added, and deletes that user.

# Program supports two parameters (after name of program).
# @param1 This is the location of the log file to parse
# @param2 This is the name of a user to not delete
# readline() will hang at the EOF waiting for input.
# You most likely will not have to restart the script however,
# if Red Team uses a script it may not delete all the users added.
# In that case, restart the script and the users will be deleted.

import sys
import os

#this is to grab the log file to search
filename = sys.argv[1]

# saves a user
myname = sys.argv[2]

file = open(filename, 'r')


currLine = file.readline()


while( currLine != None ):
	#find username, delete user
	# format will probably be 'new user=username'
	# MODIFY THE FOLLOWING LINE PER OS 
	if "new user" in currLine:
		lineList = currLine.split("=")
		#name list will be list where we grab name from
		nameList = lineList[1].partition(",")
		
		# this will delete user is user is not your user
		if myname != nameList[0]:
			cmd = "userdel -f " + nameList[0] 
			os.system( cmd )
	currLine = file.readline()

file.close()
