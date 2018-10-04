from os import path

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QAction


def get_tab_object(tab):
    return tab.currentWidget()


def get_tab_index(tab):
    return tab.indexOf(get_tab_object(tab))


def get_tab_name(tab):
    return tab.tabText(get_tab_index())


def check_exist_filename(self, name):
    if self.fullname.count(name) == 1:
        return True
    else:
        return False


def find_way_to_file(file):
    return path.abspath(path.join(path.dirname(__file__), file))


def get_image(name, size=None):
    icon = QIcon()
    icon.addPixmap(QPixmap(find_way_to_file("Images") + "\\" + name), QIcon.Normal, QIcon.Off)
    if size is not None:
        icon.pixmap(QSize(size, size))
    return icon


def create_button(self, func_name, name_button, icon_size, icon="", shortcut=""):
    icon_btn = get_image(icon, icon_size)

    button = QAction(icon_btn, name_button, self)
    button.setIcon(icon_btn)
    button.setShortcut(shortcut)
    button.triggered.connect(func_name)
    return button

