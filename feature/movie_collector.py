import random
import os

from data.model import MovieFile
from helper.util import get_extension, VIDEO, IMG


class MovieCollector:
    def __init__(self):
        self.__movies_dirs = []
        self.__all_files = []
    #
    def add_movie_dir(self, path):
        if path not in self.__movies_dirs:
            self.__movies_dirs.append(path)
    #
    def edit_movie_dir(self, index, new_path):
        self.__movies_dirs[index] = new_path

    def del_movie_dir(self, index:int):
        self.__movies_dirs.pop(index)

    def del_all(self):
        self.__movies_dirs.clear()
    #
    def pick_random_dir(self):
        assert len(self.__all_files) > 0
        selected_movie = random.choice(self.__all_files)
        image = self.get_image_from_folder(selected_movie)
        return selected_movie, image
    #
    def add_files_from_movies_dir(self, on_progress=None, on_finish=None):
        for index, movie_dir in enumerate(self.__movies_dirs):
            for path, dirs, files in os.walk(movie_dir):
                for file in files:
                    file_fullpath = os.path.join(path, file)
                    if get_extension(file_fullpath)[1:].lower() in VIDEO:
                        movie = MovieFile(file_fullpath)
                        #
                        self.__all_files.append(movie)
            if on_progress:
                on_progress.emit((index + 1) * 100 // len(movie_dir))
        if on_finish:
            on_finish.emit()
    #
    def get_image_from_folder(self, movie:MovieFile) -> str:
        best_quality_image = ("", 0)
        files = os.listdir(movie.get_folder())
        for file in files:
            file_fullpath = os.path.join(movie.get_folder(), file)
            if os.path.isfile(file_fullpath):
                if get_extension(file_fullpath)[1:].lower() in IMG:
                    file_size = os.path.getsize(file_fullpath)
                    if file_size > best_quality_image[1]:
                        best_quality_image = (file_fullpath, file_size)
        return best_quality_image[0]

    def print_movie_dirs(self):
        print("LISTA DE CARPETAS AGREGADAS\n==============================\n\n")
        for dir in self.__movies_dirs:
            print(dir)

    def print_movies(self):
        print("LISTA DE PELIS\n==============================\n\n")
        for movie in self.__all_files:
            print(movie)