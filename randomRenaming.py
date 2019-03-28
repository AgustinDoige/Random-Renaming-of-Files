# decoder UTF-8

"""
DESCRIPTION: This program takes the files of a path (by default the current working directory)
and renames every file in it into a random 20 digit string. It also saves the new names so a new execution in the same folder
will only rename new files.
CREATOR: Agustin Marcelo Dominguez
DATE: November 2018
NOTE: The code is commented out to prevent damages caused by an accidental execution
USE: Un-comment the code and place on the folder where files should be renamed and execute. Alternatively
change the path of line 23 to the directory where the reaname should occur"""

import os
import random
from sys import argv

def getRanStr(length):
	# Produces a string of <lenght> random digits
	ans = ''
	for dig in range(length):
		ans += str(random.randint(0,9))
	return ans

def manualMessage():
	print("No arguments passed. Starting manual:\n\n")
	print("type  'python randomRenaming.py 1'  for basic update or start of a new execution with default settings.")
	print("type  'python randomRenaming.py 2'  for showcasing custom settings.")
	print("type  'python randomRenaming.py 3'  for checks for deleted files.")
	print("type  'python randomRenaming.py 4'  for renaiming of all files.")

def customSettingsMessage():
	pass

def readCache():
	cacheR = set()
	try:
		print("Reading Cache...")
		with open('cache.txt','r') as f:
			#This reads the already cached numbers so new uses don't need a complete re-execution
			while True:
				cached_value = f.readline()
				print(cached_value.rstrip())
				cacheR.append(cached_value.rstrip())
				if (cached_value == ''):
					print("Reading Cache done")
					break
	except FileNotFoundError:
		print("Cache File not found")
		pass

def writeCache(cacheSet):
	cacheToWrite = sorted(list(cacheSet))
	with open('cache.txt','w') as g:
		for element in cacheToWrite:
			g.write(element+"\n")

def start(digits=20,renameEverything=False,saveCache=True):
	if renameEverything:
		cache = set()
	else:
		cache = readCache()	

	for it in os.listdir():
		tupl = os.path.splitext(it) #This splits the name so we get the extension
		if (it == "cache.txt" or it == "randomRenaming.py" or (tupl[0] in cache)):
			pass
		else:
			random_string = getRanStr(digits)
			try:
				os.rename(it,random_string+tupl[1])
			except Exception:
				while True:
					try:
						#This takes the string, converts it into an Int and adds 1, then turns it back into a string and tries again.
						random_string = str((int(random_string)+1)).zfill(digits) 
						os.rename(it,random_string+tupl[1])
						break
					except Exception:
						pass
			cache.add(random_string)
	if saveCache:
		writeCache(cache)

arguments = sys.argv
	if len(arguments) == 1:
		manualMessage()
	elif arguments[1] == 1:
		start()
	elif arguments[1] == 2:
		customSettingsMessage()
	elif arguments[1] == 3:
		pass
	elif arguments[1] == 4:
		start(renameEverything=True)


