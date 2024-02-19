import threading
from sys import argv

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from qtpy import uic

from data.model import MovieFile
from feature.movie_collector import MovieCollector
from threads.task import Task
from threads.thread import SubTaskThread


class RandomMoviePicker(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ui/main.ui", self)
        #
        self.doItButton.clicked.connect(self.do_it_function)
        self.actionConfigurar.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        #
        self.movie_collector = MovieCollector()

    def do_it_function(self):
        self.movie_collector.del_all()
        #
        dirs_text = self.movieListEditText.toPlainText().strip()
        dirs = dirs_text.split("\n")
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
        self.movieFileLineEdit.setText("Título:\n" + movie.get_movie_filename())
        self.qualityLabel.setText("Calidad:\n" + movie.get_quality())
        #
        if image:
            pixmap = QPixmap(image)
            pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)

            # Establecer la imagen en el QLabel
            self.imageLabel.setPixmap(pixmap)
        #
        self.stackedWidget.setCurrentIndex(1)

def main():
    app = QApplication(argv)
    window = RandomMoviePicker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
