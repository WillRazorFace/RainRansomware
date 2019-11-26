from Crypto.Cipher import AES
from winreg import *
from shutil import copyfile
from ctypes import windll
from os import remove, rename
from os.path import splitext
from time import sleep
from struct import unpack, calcsize

class Decrypt:
    def __init__(self, key=None, decryptor=None):
        self.key = key
        self.decryptor = decryptor
        self.get_key()

    def get_key(self):
        winkey = OpenKey(HKEY_LOCAL_MACHINE, '')
        try:
            binkey = QueryValueEx(winkey, ' ')[0]
            self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
        except PermissionError:
            try:
                winkey = OpenKey(HKEY_CURRENT_USER, '')
                binkey = QueryValueEx(winkey, ' ')[0]
                self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
            except FileNotFoundError:
                exit(1)
        except FileNotFoundError:
            try:
                winkey = OpenKey(HKEY_CURRENT_USER, '')
                binkey = QueryValueEx(winkey, ' ')[0]
                self.key = (bytes(int(binkey[i: i + 8], 2) for i in range(0, len(binkey), 8)))
            except FileNotFoundError:
                exit(1)
        return 0

    def restore_background(self, appdata: str):
        old = appdata + '/Microsoft/Windows/Themes/OldTranscodedWallpaper'
        changed = appdata + '/Microsoft/Windows/Themes/TranscodedWallpaper'
        copyfile(old, changed)
        remove(old)
        windll.user32.SystemParametersInfoW(20, 0, changed, 0)

    def correct_ext(self, file: str):
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

        with open(filename, 'rb') as f:
            cnt += 1
            f.seek(cnt)
            filedata = f.read()

        with open(filename, 'wb') as f:
            f.write(filedata)

        return filename

    def decrypt_file(self, file: str, chunksize=64*2048):
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

decrypto = Decrypt()
decrypto.decrypt_file('data.rain')
