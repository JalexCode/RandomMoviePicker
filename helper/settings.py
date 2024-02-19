from PyQt5 import QtCore

settings = QtCore.QSettings('JalexCode', 'RandomMoviePicker')

def add_dirs_to_settings(value:str):
    settings.setValue('dirs', value)

def add_last_movie_to_settings(value:str):
    settings.setValue('last_movie', value)

def get_dirs():
    return settings.value('dirs')

def get_last_movie():
    return settings.value('last_movie')