# Main Python Modules
import sys
import os

# PyQT5 and others Outside Modules
from PyQt5.QtWidgets import QTextEdit, QToolBar, QTabWidget, QMainWindow,\
    QApplication, QFileDialog, QMessageBox, QDockWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt, QRegExp
import qdarkstyle

# My Private Modules
import syntax
import UI
import Helpers
import FileHelper
import UIHelper
import xml_read


class Editer(QMainWindow, QTextEdit):
    def __init__(self, parent=None):
        super(Editer, self).__init__(parent)
        # Created all Tables
        self.all_buttons = []
        self.fullname = []
        self.all_tree_items = []

        # All Class Definitions
        self.tabWidget = QTabWidget(self)
        self.toolbar = QToolBar()
        self.struc = self.create_subwindow("Structure")
        self.instance = self.create_subwindow("Gothic Instance")

        # Attributes
        self.highlight = None
        self.Gothic2Root = xml_read.xml_basic[0][0]
        self.load_scripts()
        # Call my UI
        UI.ui_look(self)

    def create_tab(self, content="", filename="New", mode=1, style=0):
        result = Helpers.check_exist_filename(self, filename)
        if mode is 1:
            choice = self.tab_type()
        else:
            choice = style
        if result is True:
            if filename is "New":
                self.create_tab(content="", filename="New " + str(len(self.fullname) - 1), mode=0, style=choice)
            else:
                self.create_msg("Exist", "You have open this file on tab ")
        elif result is False:
            # Add Tab
            tab = QTextEdit()
            self.tabWidget.addTab(tab, filename)
            tab.setStyleSheet("color: rgb(255,255,255);"
                              "font-size: 18px;"
                              "font-family: Courier;")
            tab.setAcceptDrops(False)
            try:
                if choice == 1:
                    tab.setText(UIHelper.npc_form)
                elif choice == 2:
                    tab.setText(UIHelper.dialog_form)
                elif choice == 3:
                    tab.setText("")
                else:
                    tab.setText(content)
            except TypeError:
                pass
            self.highlight = syntax.Highlighter(tab.document())
            self.fullname.append(filename)
            self.tabWidget.setCurrentWidget(tab)
            self.tabWidget.setTabIcon(Helpers.get_tab_index(self.tabWidget), FileHelper.get_image('file.png'))
            self.tabWidget.setTabsClosable(True)

    def create_msg(self, title, text):
        msg = QMessageBox()
        msg.information(self, title, text, msg.Yes)

    def load_file(self):
        try:
            type_to_load = "Daedalus (*.d) ;; ModelScript (*.mds);; Source Scripts(*src)"
            qfiledialog = QFileDialog()
            name, _ = qfiledialog.getOpenFileName(self, 'Open File', self.Gothic2Root, type_to_load, options=None)
            self.Gothic2Root = os.path.join(self.Gothic2Root, name)
            file = open(name, 'r')
            temp = os.path.splitext(name)[0]

            with file:
                text = file.read()
                self.create_tab(text, os.path.basename(temp), mode=0)

        except FileNotFoundError:
            pass
        except TypeError:
            pass

    def file_save(self):
        try:
            type_to_save = "Daedalus (*.d) ;; ModelScript (*.mds);; Source Scripts(*src)"
            qfiledialog = QFileDialog()
            name, _ = qfiledialog.getSaveFileName(self, 'Save File', self.Gothic2Root, type_to_save, options=None)
            self.Gothic2Root = os.path.join(self.Gothic2Root, name)
            file = open(name, "w")
            tab = Helpers.get_tab_object(self.tabWidget)
            text = tab.toPlainText()
            file.write(text)
            file.close()
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    def close_application(self):
        msg = QMessageBox()
        choice = msg.question(self, "Close", "Really you want close?", msg.Yes | msg.No)
        if choice == msg.Yes:
            sys.exit()
        else:
            pass

    def remove_tab(self, index):
        try:
            self.fullname.remove(self.tabWidget.tabText(index))
            self.tabWidget.removeTab(index)
        except ValueError:
            pass

    def create_subwindow(self, name):
        dock = QDockWidget(name, self)
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dock.setWidget(tree)
        dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        return dock

    def load_scripts(self):
        path = os.path.join(self.Gothic2Root, "_Work\\data\\Scripts")
        list = FileHelper.find(path)
        widget = self.struc.widget()
        widget.setColumnCount(1)
        head = QTreeWidgetItem(widget)
        cos = path.split("\\")
        head.setText(0, cos[len(cos)-1])
        head.setIcon(0, FileHelper.get_image("cabinet.png"))
        UIHelper.create_items(self, "folder.png", head, list[0][1])
        count = 0
        for c in range(0, len(self.all_tree_items)):
            path = os.path.join(self.Gothic2Root, "_Work\\data\\Scripts", self.all_tree_items[c].text(0))
            cos = FileHelper.find(path)
            UIHelper.create_items(self, "folder.png", self.all_tree_items[c], cos[0][1])
            if len(cos[0][2]) > 1:
                count += len(cos[0][2])
                UIHelper.create_items(self, "file_icon.png", self.all_tree_items[c], cos[0][2])
        widget.addTopLevelItem(head)

    @staticmethod
    def tab_type():
        msg = QMessageBox()
        msg.setWindowTitle("What type Script?")
        msg.setWindowIcon(FileHelper.get_image("Daedalus_Logo_128x128.png"))
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore)
        button_npc = msg.button(QMessageBox.Yes)
        button_npc.setText("Npc")
        button_dialog = msg.button(QMessageBox.Ignore)
        button_dialog.setText("Dialog")
        button_script = msg.button(QMessageBox.No)
        button_script.setText("Custom Script")
        msg.exec()
        if msg.clickedButton() is button_npc:
            return 1
        elif msg.clickedButton() is button_dialog:
            return 2
        elif msg.clickedButton() is button_script:
            return 3
        pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()

    def dragEnterEvent(self, event):

        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path_to_file = url.toLocalFile()
            if os.path.isfile(path_to_file):
                FileHelper.load_text_from_file(self, path_to_file)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myclass = Editer()
    sys.exit(app.exec_())
