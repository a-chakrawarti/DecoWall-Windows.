# Standard Libraries
import os
import ctypes
import socket
from json import load, dump

# 3rd Party Libraries
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from win10toast import ToastNotifier


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def notify(title, msg):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                       msg,
                       icon_path='./favicon.ico',
                       duration=2,
                       threaded=True
                       )


def monitor_resolution():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize


dirs = ['downloaded', 'favourites']


def make_directory():
    for path in dirs:
        if not os.path.exists(os.path.join(os.getcwd(), path)):
            os.mkdir(path)


def image_name():
    image_file_name = []
    if len(dirs) == 0:
        image_file_name.clear()
    else:
        image_file_name.clear()
        for folder in range(len(dirs)):
            for name in os.listdir(dirs[folder]):
                if os.path.isfile(os.path.join(dirs[folder], name)):
                    image_file_name.append(os.path.join(dirs[folder], name))
    return image_file_name


def popup(title, message):
    msg = QMessageBox()
    # msg.setWindowFlag(Qt.FramelessWindowHint)
    msg.setIconPixmap(QPixmap('./favicon.png').scaled(32, 32))
    msg.setWindowTitle(title)
    msg.setText(f"<p align='center'><b>{message}<b></p>")
    msg.setWindowIcon(QIcon(QPixmap('./favicon.png')))
    show = msg.exec_()


def get_config(key):
    """ returns value from settings.json having key """
    with open('config.json', 'r') as file:
        data = load(file)
        return data[f'{key}']


def apply_config(key, value):
    """updates settings.json provide key and value"""
    with open('config.json', 'r') as file:
        data = load(file)
        data[f'{key}'] = value
    with open('config.json', 'w') as file:
        dump(data, file, indent=2)
