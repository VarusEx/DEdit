import sys

from PyQt5.QtCore import QSize, Qt

from PyQt5.QtWidgets import QTextEdit, QToolBar, QTabWidget, QMainWindow,\
    QApplication, QFileDialog, QMessageBox
import qdarkstyle
import api
import syntax


class Editer(QMainWindow, QTextEdit):
    def __init__(self, parent=None):
        myclass = Editer
        super(myclass, self).__init__(parent)
        # Created all Tables
        self.all_buttons = []
        self.fullname = ["Start"]
        self.pointforobject = ["Start"]

        # All Class Definitions
        self.tabWidget = QTabWidget(self)
        self.toolbar = QToolBar()

        self.main_look()

    def main_look(self):

        self.all_buttons += [api.create_button(self, self.create_tab,
                                               80,
                                               icon="New.png",
                                               shortcut="Ctrl + N")]
        self.all_buttons += [api.create_button(self, self.load_file,
                                               80,
                                               icon="open-file.png",
                                               shortcut="Ctrl + O")]
        self.all_buttons += [api.create_button(self, self.file_save,
                                               80,
                                               icon="save.png",
                                               shortcut="Ctrl + S")]
        # TabWidget Settings
        self.tabWidget.setObjectName("tabWidget")
        self.create_tab("Welcome in My Editor to Write Daedalus Scripts \n"
                        "Created by Verus", filename="StartSite")

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
        self.setWindowIcon(api.return_image("Daedalus_Logo_128x128.png"))
        self.setWindowTitle("DEdit")
        self.show()

    def create_tab(self, content="", filename="New"):
        result = api.check_exist_filename(self, filename)
        if result is True:
            self.create_msg("Exist", "You have open this file on tab ")
        elif result is False:
            # Add Tab
            tab = QTextEdit()
            self.tabWidget.addTab(tab, filename)
            tab.setStyleSheet("color: rgb(255,255,255);"
                              "background-color: rgb(50,65,74);"
                              "font-size: 18px;"
                              "font-family: Courier;")
            try:
                tab.setText(content)
            except TypeError:
                pass
            self.highlight = syntax.Highlighter(tab.document())
            self.fullname.append(filename)
            self.pointforobject.append(str(tab))
            self.tabWidget.setCurrentWidget(tab)

    def create_msg(self, title, text):
        msg = QMessageBox
        msg.information(self, title, text, msg.Yes)

    def load_file(self):
        try:
            type_to_load = "Daedalus (*.d) ;; ModelScript (*.mds);; Source Scripts(*src)"
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', '\\*.d', type_to_load)
            file = open(name, 'r')

            with file:
                text = file.read()
                self.create_tab(text, name)

        except FileNotFoundError:
            pass
        except TypeError:
            pass

    def file_save(self):
        try:
            type_to_save = "Daedalus (*.d) ;; ModelScript (*.mds);; Source Scripts(*src)"
            name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', type_to_save)
            file = open(name, "w")
            tab = api.get_tab_object(self.tabWidget)
            text = tab.toPlainText()
            file.write(text)
            file.close()
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()

    def close_application(self):
        msg = QMessageBox
        choice = msg.question(self, "Close", "Really you want close?", msg.Yes | msg.No)
        if choice == msg.Yes:
            sys.exit()
        else:
            pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myclass = Editer()
    sys.exit(app.exec_())
