from pathlib import Path

from feature.movie_collector import MovieCollector
from helper.util import get_extension, IMG
import os

def app():
    movie_collector = MovieCollector()
    movie_collector.add_movie_dir("D:\!!!!DUKTO")
    movie_collector.add_movie_dir("D:\Filmes wenorros")
    movie_collector.add_movie_dir("D:\PELIS")
    movie_collector.add_movie_dir("E:\Datos\Dukto")
    movie_collector.add_movie_dir("G:\!!!!!!Dukto")
    movie_collector.add_movie_dir("G:\Pelis")
    movie_collector.add_movie_dir("H:\Datos\PELIS")
    movie_collector.add_movie_dir("I:\!!!!JAVIER\Pelis")
    movie_collector.add_movie_dir("K:\Pelis")
    movie_collector.add_movie_dir("D:\Filmes wenorros")
    #
    # movie_collector.print_movie_dirs()
    #
    movie_collector.add_files_from_movies_dir()
    #
    # movie_collector.print_movies()
    #
    print("HOY VERÁS:", end=" ")
    random_movie, img = movie_collector.pick_random_dir()
    print(random_movie)

def test():
    best_quality_image = ("", 0)
    for path, dirs, files in os.walk("D:\Filmes wenorros\Pelis\CAPTAIN HARLOCK [2014]"):
        print(Path("D:\Filmes wenorros\Pelis\CAPTAIN HARLOCK [2014]\esd.jpg").parent)
        for file in files:
            file_fullpath = os.path.join(path, file)
            print(get_extension(file_fullpath).lower())
            if get_extension(file_fullpath)[1:].lower() in IMG:
                file_size = os.path.getsize(file_fullpath)
                print(file_size)
                if file_size > best_quality_image[1]:
                    best_quality_image = (file_fullpath, file_size)
    print(best_quality_image[0])

if __name__ == '__main__':
    test()