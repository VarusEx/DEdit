from os import path
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


def find_way_to_file(file):
    return path.abspath(path.join(path.dirname(__file__), file))


def get_image(name, size=None):
    icon = QIcon()
    icon.addPixmap(QPixmap(find_way_to_file("Images") + "\\" + name), QIcon.Normal, QIcon.Off)
    if size is not None:
        icon.pixmap(QSize(size, size))
    return icon
