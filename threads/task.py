from feature.movie_collector import MovieCollector


class Task:
    def __init__(self, sub_task):
        self.sub_task = sub_task

    def do_it(self, movie_collector:MovieCollector):
        movie_collector.add_files_from_movies_dir(self.sub_task.progress_signal, self.sub_task.finish_signal)