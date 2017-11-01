#!/usr/bin/python
import os
import re
import subprocess

SOURCE_DIR ='/mnt/freebox/darkness/51.15.76.14/outcoming/' 
DEST_DIR = '/mnt/freebox/toSee/'

def listFiles():
	print "listFiles()"

	#list files on download folder 
	for filename in os.listdir(SOURCE_DIR):
		#print file
		niark, file_extension = os.path.splitext(filename)
		episode_pattern = re.compile(r"S\d+E\d+", re.IGNORECASE)
		gatherDirName=''
		for m in re.finditer(episode_pattern, filename):
			end = m.end()
			gatherDirName = filename[0 : m.end() -7] + '/'
			gatherDirName = gatherDirName.replace('.',' ');
			
		#gather metadata on file 
		file = {'name' : filename, 'sourcePath': SOURCE_DIR +filename, 'gatherDirName' : gatherDirName, 'destDir' : DEST_DIR + gatherDirName + filename}
		if not os.path.isdir(DEST_DIR + gatherDirName):
			os.mkdir(DEST_DIR + gatherDirName);
		print file['destDir']
		os.rename(file['sourcePath'],file['destDir']);		
			
listFiles()