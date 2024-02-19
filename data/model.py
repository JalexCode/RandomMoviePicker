from pathlib import Path

from helper.util import *


class MovieFile:
    def __init__(self, fullpath):
        self.__fullpath = Path(fullpath)

    def get_folder(self):
        return self.__fullpath.parent

    def get_filename(self):
        return self.__fullpath.stem

    def get_extension(self):
        return self.__fullpath.suffix

    def get_quality(self):
        ext = self.get_extension()[1:]
        if ext in BAD_QUALITY:
            return "Mala/Baja"
        elif ext in GOOD_QUALITY:
            return "Buena/Media-Alta"
        elif ext in EXCELLENT_QUALITY:
            return "Excelente/Alta"
        else:
            return "Desconocida"

    def get_movie_filename(self):
        return f"{self.get_filename()}{self.get_extension()}"

    def __str__(self):
        return f"{self.get_movie_filename()} ({self.get_quality()})"