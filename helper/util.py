import subprocess
from pathlib import Path
import os

IMG = ['ani', 'bmp', 'gif', 'ico', 'jpe', 'jpeg', 'jpg', 'pcx', 'png', 'psd', 'tga', 'tif', 'tiff', 'wmf']
VIDEO = ['3g2', '3gp', '3gp2', '3gpp', 'amr', 'amv', 'asf', 'avi', 'bdmv', 'bik', 'd2v', 'divx', 'drc', 'dsa', 'dsm',
         'dss', 'dsv', 'evo', 'f4v', 'flc', 'fli', 'flic', 'flv', 'hdmov', 'ifo', 'ivf', 'm1v', 'm2p', 'm2t', 'm2ts',
         'm2v', 'm4b', 'm4p', 'm4v', 'mkv', 'mp2v', 'mp4', 'mp4v', 'mpe', 'mpeg', 'mpg', 'mpls', 'mpv2', 'mpv4', 'mov',
         'mts', 'ogm', 'ogv', 'pss', 'pva', 'qt', 'ram', 'ratdvd', 'rm', 'rmm', 'rmvb', 'roq', 'rpm', 'smil', 'smk',
         'swf', 'tp', 'tpr', 'ts', 'vob', 'vp6', 'webm', 'wm', 'wmp', 'wmv']
BAD_QUALITY = ['3gp', 'avi', 'mpeg', 'mpg', 'vob']
GOOD_QUALITY = ['webm', 'mp4', 'rmvb', 'divx', 'flv', 'mov', 'ts']
EXCELLENT_QUALITY = ['mkv']


def get_extension(path: str) -> str:
    fullpath = Path(path)
    return fullpath.suffix


def open_file_folder(file_path, folder=False):
    try:
        print(file_path)
        CREATE_NO_WINDOW = 0x08000000
        if folder:
            file_path = file_path.replace("/", "\\")
            subprocess.Popen(['explorer.exe', '/select,', file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False,
                             creationflags=CREATE_NO_WINDOW)
        else:
            subprocess.Popen(['cmd', '/C', 'start', file_path, file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False,
                             creationflags=CREATE_NO_WINDOW)

    except Exception as e:
        self.error("Abriendo archivo descargado", e.args)
