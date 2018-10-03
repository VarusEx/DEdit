from os import path

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QAction


def get_tab_object( tab):
    current = tab.currentWidget()
    return current


def get_tab_index(self, tab):
    index = tab.indexOf(self.get_tab_object())
    return index


def get_tab_name(self, tab):
    name = tab.tabText(self.get_tab_index())
    return name


def check_exist_filename(self, name):
    if self.fullname.count(name) == 1:
        return True
    else:
        return False


def find_way_to_file(file):
    base = path.abspath(path.join(path.dirname(__file__), file))
    return base


def return_image(name, size=None):
    icon = QIcon()
    icon.addPixmap(QPixmap(find_way_to_file("Images") + "\\" + name), QIcon.Normal, QIcon.Off)
    if size is not None:
        icon.pixmap(QSize(size, size))
    return icon


def create_button(self, func_name, icon_size, icon="", shortcut=""):
    icon_btn = return_image(icon, icon_size)

    button = QAction(icon_btn, 'Exit', self)
    button.setIcon(icon_btn)
    button.setShortcut(shortcut)
    button.triggered.connect(func_name)
    return button

