# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEdit.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from os import path, walk, environ

from  xml.dom import minidom

from PyQt5.QtCore import QSize, Qt, QMetaObject, pyqtSignal

from PyQt5.QtGui import QIcon, QPixmap, QSyntaxHighlighter, QColor, QTextCharFormat

from PyQt5.QtWidgets import QFrame, QWidget, QGridLayout, QTextEdit, QHBoxLayout, QProgressBar\
                            , QLabel, QLayout, QSizePolicy, QSpacerItem, QPushButton, QTabWidget\
                            , QFormLayout, QMainWindow, QApplication, QFileDialog, QMessageBox
import api

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):

        self.basepath = path.dirname(__file__)
        self.filepath = path.abspath(path.join(self.basepath, "Images"))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 873)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QSize(1012, 47))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        #Credits
        self.label = QLabel(self.frame_3)
        self.label.setStyleSheet("font: 12pt \"Rockwell\";")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label.setText("Created By Piotr\"Verus\"Jasiński")
        self.horizontalLayout_2.addWidget(self.label)

        self.gridLayout.addWidget(self.frame_3, 3, 1, 1, 1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QSize(60, 80))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(191, -1, 200, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # Button New
        self.btn_new = QPushButton(self.frame)
        self.btn_new.setMaximumSize(QSize(80, 50))
        self.btn_new.setText("")
        self.btn_new.setObjectName("btn_new")
        self.btn_new.setIcon(self.return_image("New.png", 40))
        self.btn_new.clicked.connect(self.new_file)
        self.horizontalLayout.addWidget(self.btn_new)
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        # Button Open
        self.btn_open = QPushButton(self.frame)
        self.btn_open.setMaximumSize(QSize(80, 50))
        self.btn_open.setText("")
        self.btn_open.setObjectName("btn_open")
        self.btn_open.setIcon(self.return_image("open-file.png", 40))
        self.btn_open.clicked.connect(self.load_file)
        self.horizontalLayout.addWidget(self.btn_open)
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        # Button Save
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setMaximumSize(QSize(80, 50))
        self.btn_save.setText("")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setIcon(self.return_image("save.png", 40))
        self.btn_save.clicked.connect(self.file_save)
        self.horizontalLayout.addWidget(self.btn_save)
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        # Button On/Off Highlihte
        self.btn_light = QPushButton(self.frame)
        self.btn_light.setMaximumSize(QSize(80, 50))
        self.btn_light.setText("")
        self.btn_light.setObjectName("btn_light")
        self.btn_light.setIcon(self.return_image("light.png", 40))
        self.horizontalLayout.addWidget(self.btn_light)
        spacerItem4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)

        # Button Change Leangue
        self.btn_lang = QPushButton(self.frame)
        self.btn_lang.setMaximumSize(QSize(80, 50))
        self.btn_lang.setText("")
        self.btn_lang.setObjectName("btn_lang")
        self.btn_lang.setIcon(self.return_image("translate.png", 40))
        self.horizontalLayout.addWidget(self.btn_lang)

        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1, Qt.AlignTop)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QTabWidget(self.frame_2)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(900, 600))
        self.tabWidget.setMaximumSize(QSize(0, 0))
        self.tabWidget.setBaseSize(QSize(0, 0))
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QTextEdit()
        self.tab.setObjectName("New 1")
        self.tabWidget.addTab(self.tab, "New 1")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tabWidget)
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        spacerItem6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 1)
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 2, 1, 1)
        spacerItem9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)

        # Create Arrays
        self.fullname = ["New 1"]
        self.pointforobject = ["New 1"]
        self.xmldata = []

        # Call Init function
        self.read_keywords_from_xml()


    def new_file(self):
        tab = QTextEdit()
        filename = str(len(self.fullname) + 1)
        self.tabWidget.addTab(tab, "New " + filename)
        self.fullname.append(filename)
        self.pointforobject.append(str(tab))
        self.tabWidget.setCurrentWidget(tab)


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

    def load_file(self):
        try:
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', '\\*.d', "Daedalus (*.d) ;; "
                                                                              "ModelScript (*.mds)"     
                                                                              ";; Source Scripts(*src)")
            file = open(name, 'r')

            with file:
                text = file.read()
                self.create_tab(text, name)

        except FileNotFoundError:
            pass
        except TypeError:
            pass

    def create_tab(self, content, filename):
        result = api.check_exist_filename(self, filename)
        if result is True:
            self.create_msg("Exist", "You have open this file on tab ")
        elif result is False:
            # Add Tab
            tabs = QTextEdit()
            self.tabWidget.addTab(tabs, filename)
            tabs.setText(content)
            self.fullname.append(filename)
            self.pointforobject.append(str(tabs))
            self.tabWidget.setCurrentWidget(tabs)
        return

    def create_msg(self, title, text):
        msg = QMessageBox
        msg.information(self, title, text, msg.Yes)

    def return_image(self, name, size):
        icon = QIcon()
        icon.addPixmap(QPixmap(self.filepath + "\\" + name), QIcon.Normal, QIcon.Off)
        icon.pixmap(QSize(size, size))
        return icon

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

    def read_keywords_from_xml(self):
        way = api.find_way_to_file(self,"keywords.xml")
        xml_doc = minidom.parse(way)

        self.xmldata.append([])
        # While to takes elements from xml file
        for item in xml_doc.getElementsByTagName('keywords')[0].getElementsByTagName("item"):
            self.xmldata[0].append(item.attributes["word"].value)
        self.xmldata.append([])
        for item in xml_doc.getElementsByTagName('opertors')[0].getElementsByTagName("item"):
            self.xmldata[1].append(item.attributes["symbol"].value)
        self.xmldata.append([])
        for item in xml_doc.getElementsByTagName('braces')[0].getElementsByTagName("item"):
            self.xmldata[2].append(item.attributes["key"].value)
        self.xmldata.append([])
        for item in xml_doc.getElementsByTagName('function')[0].getElementsByTagName("item"):
            self.xmldata[3].append(item.attributes["func"].value)
        self.xmldata.append([])

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

