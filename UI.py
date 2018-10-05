from PyQt5.QtCore import Qt, QSize

import UIHelper
import FileHelper


def ui_look(self):
    self.all_buttons += [UIHelper.create_button(self, self.create_tab,
                                                "Create New File",
                                                icon="New.png",
                                                shortcut="Ctrl + N")]
    self.all_buttons += [UIHelper.create_button(self, self.load_file,
                                                "Load File",
                                                icon="open-file.png",
                                                shortcut="Ctrl + O")]
    self.all_buttons += [UIHelper.create_button(self, self.file_save,
                                                "Save File",
                                                icon="save.png",
                                                shortcut="Ctrl + S")]
    # TabWidget Settings
    self.tabWidget.setObjectName("tabWidget")
    self.create_tab("Welcome in My Editor to Write Daedalus Scripts \n"
                    "Created by Verus", filename="StartSite")
    self.tabWidget.tabCloseRequested.connect(self.remove_tab)
    # Tollbar Action added
    self.toolbar.addAction(self.all_buttons[0])
    self.toolbar.insertSeparator(self.all_buttons[1])
    self.toolbar.addAction(self.all_buttons[1])
    self.toolbar.insertSeparator(self.all_buttons[2])
    self.toolbar.addAction(self.all_buttons[2])
    self.toolbar.setAllowedAreas(Qt.RightToolBarArea |
                                 Qt.RightToolBarArea)
    self.toolbar.setMovable(False)
    self.toolbar.setIconSize(QSize(42, 42))
    self.addToolBar(self.toolbar)
    # MainWindow Look and size
    self.resize(800, 600)
    self.setCentralWidget(self.tabWidget)
    self.setWindowIcon(FileHelper.get_image("Daedalus_Logo_128x128.png"))
    self.setWindowTitle("DEdit")
    self.show()
