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
import sys

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
	while True:
		temp_d = input("How many digits should the files have? (default: 20) :  ")
		try:
			d = int(temp_d)
			break
		except Exception:
			pass

	while True:
		temp_re = input("Rename every file? (y/n) :  ")
		if temp_re.lower() == 'y':
			re = True
			break
		elif temp_re.lower() == 'n':
			re = False
		else:
			pass

	while True:
		temp_sc = input("Save cache at the end? (y/n) :  ")
		if temp_sc.lower() == 'y':
			sc = True
			break
		elif temp_sc.lower() == 'n':
			sc = False
			break
		else:
			pass

	start(digits=d,renameEverything=re,saveCache=sc)

def readCache():
	cacheR = set()
	try:
		print("Reading Cache...")
		with open('cache.txt','r') as f:
			#This reads the already cached numbers so new uses don't need a complete re-execution
			while True:
				cached_value = f.readline()
				# print(cached_value.rstrip())
				cacheR.add(cached_value.rstrip())
				if (cached_value == ''):
					print("Reading Cache done")
					return cacheR
	except FileNotFoundError:
		print("Cache File not found")
		return set()

def writeCache(cacheSet):
	print("Writing cache...")
	cacheToWrite = sorted(list(cacheSet))
	with open('cache.txt','w') as g:
		for element in cacheToWrite:
			g.write(element+"\n")
	print("Writing cache done")

def getFileList():
	l = []
	for it in os.listdir():
		l.append(os.path.splitext(it)[0]) #This is the name of the file without the extension
	return l
		
def start(digits=20,renameEverything=False,saveCache=True):
	repeat = False
	if renameEverything:
		cache = set()
	else:
		cache = readCache()	

	for it in os.listdir():
		tupl = os.path.splitext(it) #This splits the name so we get the extension
		# print(tupl[0],tupl)
		# print(cache)
		if (it == "cache.txt" or it == "randomRenaming.py" or (tupl[0] in cache)):
			pass
		else:
			try:
				random_string = getRanStr(digits)	
				if random_string not in cache:
					os.rename(it,random_string+tupl[1])

				else:
					while random_string in cache:
						random_string = str((int(random_string)+1)).zfill(digits)
					os.rename(it,random_string+tupl[1])
				cache.add(random_string)
			except Exception: # This is a dumb hack and I know it
				repeat = True
				while True:
					try:
						random_string = str((int(random_string)+1)).zfill(digits)
						os.rename(it,random_string+tupl[1])
						break
					except Exception:
						pass
	if saveCache:
		writeCache(cache)

	# if repeat:
		# start(digits=digits,renameEverything=renameEverything,saveCache=saveCache)

def checkFiles():
	print("Checking for missing files...")
	files = set(getFileList())
	cache = list(readCache())
	deletedFiles = set()

	uncorrupted = True
	for fileName in cache:
		if fileName not in files:
			if fileName != '':
				uncorrupted = False
				deletedFiles.add(fileName)
				print(fileName, "not found in folder")
	if uncorrupted:
		print("No files missing")
	else:
		while True:
			action = input("Delete missing files from cache? (y/n) :  ")
			if action.lower() == 'y':
				newCache = set()
				for ca in cache:
					if ca not in deletedFiles:
						newCache.add(ca)
				writeCache(newCache)
				break
			elif action.lower() == 'n':
				break
			else:
				pass

arguments = sys.argv
if len(arguments) == 1:
	manualMessage()
elif arguments[1] == '1':
	start()
elif arguments[1] == '2':
	customSettingsMessage()
elif arguments[1] == '3':
	checkFiles()
elif arguments[1] == '4':
	start(renameEverything=True)
print("Program Completed.")