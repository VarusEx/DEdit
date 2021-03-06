import os

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


def find_way_to_file(file):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))


def get_image(name, size=None):
    icon = QIcon()
    icon.addPixmap(QPixmap(find_way_to_file("Images") + "\\" + name), QIcon.Normal, QIcon.Off)
    if size is not None:
        icon.pixmap(QSize(size, size))
    return icon


def load_text_from_file(self, path):
    file = open(path, 'r')
    with file:
        text = file.read()
        self.create_tab(self, text, os.path.basename(path), mode=0)


def find(path):
    list = []
    for root, dir, files in os.walk(path):
            list.append([root, dir, files])
    return list
