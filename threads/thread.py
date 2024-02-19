from PyQt5.QtCore import QObject, pyqtSignal

class SubTaskThread(QObject):
    progress_signal = pyqtSignal(object)
    finish_signal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)