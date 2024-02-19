import threading
from sys import argv

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel
from qtpy import uic

from feature.movie_collector import MovieCollector
from helper.settings import add_dirs_to_settings, add_last_movie_to_settings, get_dirs, get_last_movie
from helper.util import open_file_folder
from threads.task import Task
from threads.thread import SubTaskThread


class RandomMoviePicker(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ui/main.ui", self)
        #
        self.load_config()
        #
        self.doItButton.clicked.connect(self.do_it_function)
        self.actionConfigurar.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        #
        self.movie_collector = MovieCollector()
        #
        self.statusBar().addWidget(QLabel("Desarrollado por @JalexCode"))
        QMessageBox.warning(self,
                            "IMPORTANTE",
                            "LA ÚNICA REGLA PARA USAR ESTE PROGRAMA ES QUE:\nSEA CUAL SEA LA PELÍCULA SELECCIONADA, TIENES QUE VERLA\n¡¡¡ESTA REGLA NO SE PUEDE VIOLAR!!!\n(from me, to myself)")

    def load_config(self):
        saved_dirs = get_dirs()
        self.movieListEditText.setPlainText(saved_dirs)
        #
        last_movie = get_last_movie()
        self.set_last_movie(last_movie)

    def do_it_function(self):
        #
        self.movie_collector.del_all()
        #
        dirs_text = self.movieListEditText.toPlainText().strip()
        dirs = dirs_text.split("\n")
        #
        add_dirs_to_settings(dirs_text)
        #
        for dir in dirs:
            self.movie_collector.add_movie_dir(dir)
        #
        sub_task = SubTaskThread()
        sub_task.progress_signal.connect(lambda progress: self.set_progress(progress))
        sub_task.finish_signal.connect(self.success)
        task = Task(sub_task)
        thread = threading.Thread(target=task.do_it, args=(self.movie_collector,))
        thread.start()

    def set_progress(self, percent: int):
        self.progressBar.setValue(percent)

    def success(self):
        self.progressBar.setValue(100)
        #
        movie, image = self.movie_collector.pick_random_dir()
        #
        add_last_movie_to_settings(movie.get_movie_filename())
        #
        self.movieFileLineEdit.setText("Título:\n" + movie.get_filename())
        self.qualityLabel.setText("Calidad de imagen:\n" + movie.get_quality())
        #
        if not image:
            image = "res/no_image.jpeg"
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)

        # Establecer la imagen en el QLabel
        self.imageLabel.setPixmap(pixmap)
        #
        self.openFileButton.clicked.connect(lambda: open_file_folder(movie.fullpath))
        self.openFolderButton.clicked.connect(lambda: open_file_folder(movie.fullpath, folder=True))
        #
        self.stackedWidget.setCurrentIndex(1)
        #
        self.set_last_movie(movie.get_movie_filename(), save=True)

    def set_last_movie(self, last_movie, save=False):
        if save: add_last_movie_to_settings(last_movie)
        self.lastMovieLabel.setText("Última selección: " + last_movie)

def main():
    app = QApplication(argv)
    window = RandomMoviePicker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
