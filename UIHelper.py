from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

import FileHelper


def create_button(self, func_name, name_button, icon="", shortcut=""):
    icon_btn = FileHelper.get_image(icon)

    button = QAction(QIcon(icon_btn), name_button, self)
    button.setIcon(icon_btn)
    button.setShortcut(shortcut)
    button.triggered.connect(func_name)
    return button
