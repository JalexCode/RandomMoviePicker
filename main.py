from feature.movie_collector import MovieCollector


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

if __name__ == '__main__':
    app()