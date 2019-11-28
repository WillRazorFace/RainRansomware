from Decrypter import Decrypt
from os.path import expanduser
from os import chdir, getenv
from string import ascii_uppercase

drives = []

for letter in list(ascii_uppercase):
    letter = letter + ':'
    drives.append(letter)

decrypto = Decrypt()

desktop = expanduser('~/Desktop')
downloads = expanduser('~/Downloads')
documents = expanduser('~/Documents')
appdata = getenv('APPDATA')

decrypto.delete_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'Rain')

decrypto.decrypt_directory(desktop)
decrypto.decrypt_directry(downloads)
decrypto.decrypt_directry(documents)

decrypto.restore_background(appdata)

for drive in drives:
    try:
        chdir(drive + '/')
        decrypto.decrypt_directory(drive)
    except FileNotFoundError:
        continue
    except PermissionError:
        continue
