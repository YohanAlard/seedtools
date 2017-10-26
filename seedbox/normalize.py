#!/usr/bin/python
import os
import re

ROOT_DIR ='/root/downloads/outcoming/' 
def normalize(directory):
    print('directory' +directory );
    for filename in os.listdir(directory):
		if filename.endswith('.html') or filename.endswith('.nfo'):
			os.remove(directory + filename)
		else:
			newFileName = filename
			niark, file_extension = os.path.splitext(filename)
			episode_pattern = re.compile(r"S\d+E\d+", re.IGNORECASE)
			for m in re.finditer(episode_pattern, filename):
				end = m.end() + 6;
				newFileName = filename[0 : m.end()]   + file_extension
			
			newFileName = newFileName.replace(" ", "")
			newFileName = newFileName.replace("[", "").replace("]", "")
			newFileName = newFileName.replace("www.CpasBien.cm", "") 
			newFileName = newFileName.replace("Torrent9.info", "") 
			newFileName = newFileName.replace("Torrent9.ws", "") 
			newFileName = newFileName.replace("Torrent9.tv", "") 
			newFileName = newFileName.replace("www.Cpasbien.me", "") 
			newFileName = newFileName.replace("www.Cpasbien.pe", "") 
			newFileName = newFileName.replace("www.Cpasbien.pw", "") 
			newFileName = newFileName.replace("www.CpasBien.pw", "") 
			os.rename(directory + filename, directory + newFileName)
		
def unfolderize(directory):
	 for filename in os.listdir(directory):
		if os.path.isdir(directory + '/'+ filename):
			unfolderize(directory + '/'+  filename)
		else:
			print(directory + filename + " go to " + '/root/downloads/outcoming/' +filename)
			os.rename(directory  + '/'+ filename, '/root/downloads/outcoming/' +filename)
		

def delFolder(directory):
	for root, dirs, files in os.walk(directory, topdown=False):
		for name in dirs:
			os.rmdir(os.path.join(root, name))
		
unfolderize('/root/downloads/outcoming/')
delFolder('/root/downloads/outcoming/')
normalize('/root/downloads/outcoming/')
