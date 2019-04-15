import os.path as op
import os
from os import scandir
import types

BLOCK_SIZE = 65536


class DirectoryIter:
    """
    produces an iterator for a file tree
    """

    def __init__(self, path):
        if not op.exists(path):
            FileNotFoundError(path)
        self.path = path

    def iter_files(self, path: str) -> types.GeneratorType:
        """
        Recursively yield DirEntry objects for given directory
        """
        for entry in scandir(path):
            if entry.is_dir(follow_symlinks=False):
                yield from self.iter_files(entry.path)
            else:
                yield entry.path

    def iter_directories(self) -> types.GeneratorType:  # consider os.scandir()
        """
        iteratively yield directories
        """
        for root, dirs, files in os.walk(self.path):
            for dir in dirs:
                yield os.path.join(root, dir)

