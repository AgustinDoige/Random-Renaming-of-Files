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
arguments = sys.argv

def getRanStr(length):
	# Produces a string of <lenght> random digits
	ans = ''
	for dig in range(length):
		ans += str(random.randint(0,9))
	return ans

def main():
	cache = []
	digits = 20

	try:
		with open('cache.txt','r') as f:
			#This reads the already cached numbers so new uses don't need a complete re-execution
			while True:
				cached_value = f.readline()
				print(cached_value.rstrip())
				cache.append(cached_value.rstrip())
				if (cached_value == ''):
					break
	except FileNotFoundError:
		pass

	with open('cache.txt','a') as g:
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
				g.write(random_string+"\n")
				cache.append(random_string)