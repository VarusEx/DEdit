from PyQt5.QtCore import Qt, QRegExp, QFileInfo
from PyQt5.QtWidgets import QHBoxLayout, QTextEdit, QAction, QApplication, QFileDialog,\
    QMainWindow, QMessageBox, qApp, QDockWidget
from PyQt5.QtGui import QFont ,QIcon, QPixmap, QColor, QSyntaxHighlighter, QTextCharFormat
from os import path



class Editer(QMainWindow, QTextEdit):
    def __init__(self, parent=None):
        okno = Editer
        super(okno,self).__init__(parent)
        self.dialog = Settings_App(self)
        self.interfejs()
        self.editor()


    def interfejs(self):

        layout = QHBoxLayout()

        self.basepath = path.dirname(__file__)
        self.filepath = path.abspath(path.join(self.basepath, "Images"))


        #Button Open
        iconOp = QIcon()
        iconOp.addPixmap(QPixmap(self.filepath+"\\"+"open-file.png"), QIcon.Normal, QIcon.Off)

        buttonOp = QAction(QIcon(iconOp),'Open',self)
        buttonOp.setIcon(iconOp)
        buttonOp.setShortcut('Ctrl+O')
        buttonOp.triggered.connect(self.file_open)

        #Button Exit
        iconEx = QIcon()
        iconEx.addPixmap(QPixmap(self.filepath+"\\"+"Door-exit.png"), QIcon.Normal, QIcon.Off)

        buttonEx = QAction(QIcon(iconEx),'Exit',self)
        buttonEx.setIcon(iconEx)
        buttonEx.setShortcut('Ctrl+Q')
        buttonEx.triggered.connect(self.close_application)

        #Button Save
        iconSa = QIcon()
        iconSa.addPixmap(QPixmap(self.filepath+"\\"+"Save.png"), QIcon.Normal, QIcon.Off)

        buttonSa = QAction(QIcon(iconSa),'Save',self)
        buttonSa.setIcon(iconSa)
        buttonSa.setShortcut('Ctrl+S')
        buttonSa.triggered.connect(self.file_save)

        #Button New
        iconNe = QIcon()
        iconNe.addPixmap(QPixmap(self.filepath+"\\"+"New.png"), QIcon.Normal, QIcon.Off)

        buttonNe = QAction(QIcon(iconNe),'New',self)
        buttonNe.setIcon(iconNe)
        buttonNe.setShortcut('Ctrl+N')
        buttonNe.triggered.connect(self.newFile)

        #Toolbar
        iconLang = QIcon()
        iconLang.addPixmap(QPixmap(self.filepath+"\\"+"translate.png"), QIcon.Normal,QIcon.Off)

        buttonLang = QAction(QIcon(iconLang),"Language", self)
        buttonLang.triggered.connect(qApp.quit)

        iconLight = QIcon()
        iconLight.addPixmap(QPixmap(self.filepath+"\\"+"light.png"), QIcon.Normal,QIcon.Off)

        buttonLight = QAction(QIcon(iconLight),"Syntax Highlighting", self)
        buttonLight.triggered.connect(qApp.quit)




        #Toolbar
        self.toolbar = self.addToolBar('ToolBar')
        self.toolbar.addAction(buttonNe)
        self.toolbar.addAction(buttonOp)
        self.toolbar.addAction(buttonSa)
        self.toolbar.addAction(buttonLang)
        self.toolbar.addAction(buttonLight)
        self.toolbar.addAction(buttonEx)
        self.setGeometry(300, 300, 0, 0)
        self.show()

        self.toolbar.setStyleSheet("border-bottom-style:solid;"
                                   "border-width:1px;"
                                   "border-color:black;"
                                   "padding:2px;"
                                   )
        self.toolbar.setFloatable(True)


        #Background
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        self.setLayout(layout)
        self.resize(1200,800)
        self.setWindowIcon(QIcon(self.filepath+"\\"+"Daedalus_Logo_256x256.png"))
        self.setWindowTitle("DEdit")
        self.show()

    def editor(self):

            self.textEdit = QTextEdit()
            self.textEdit.toPlainText().encode("utf-8").decode("ansi")

            self.textEdit.setStyleSheet("color: rgb(255,255,255);"
                                        "background-color: rgb(50,65,74);"
                                        "font-size: 18px;"
                                        "font-family: Courier;")
            self.setCentralWidget(self.textEdit)
            self.highlighter = Highlighter(self.textEdit.document())

    def setcurrentFileName(self, fileName=''):
        self.fileName = fileName
        self.textEdit.document().setModified(False)

        if not  fileName:
            shownName = 'Untiled.d'
        else:
            shownName = QFileInfo(fileName).fileName()

        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "DEdit")))
        self.setWindowModified(False)

    def newFile(self):
            self.textEdit.clear()
            self.setcurrentFileName()

    def file_open(self):
        try:
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', '\\*.d', "Daedalus (*.d)",
                                                            options=QFileDialog.DontUseNativeDialog)
            file = open(name, 'r')
            self.editor()
            with file:
                text = file.read()
                self.textEdit.setText(text)
        except FileNotFoundError:
            print("Nie znaleziono pliku")

    def file_save(self):
        try:
            name, _ = QFileDialog.getSaveFileName(self, 'Save File', '\\*.d', "Daedalus (*.d)" ,
                                                            options=QFileDialog.DontUseNativeDialog)
            file = open(name, "w")
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        except FileNotFoundError:
            print("Nie znaleziono pliku!!")
        except PermissionError:
            print("Nie mam prawa zapisywać tego tu!!")

    def close_application(self):
        choice = QMessageBox.question(self, "Close",
                                                "Really you want close?",
                                                QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()

class Settings_App(QMainWindow):
    def __init__(self, parent=None):
        super(Settings_App, self).__init__(parent)

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(46,137,229))
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["[Vv][Oo][Ii][Dd]\s","[Ff][Uu][Nn][Cc]","[Ii][Nn][Ss][Tt][Aa][Nn][Cc][Ee]","[Cc][Oo][Nn][Ss][Tt]","[Vv][Aa][Rr]\s","[Ii][Nn][Tt]\s"
                          , "[Ss][Tt][Rr][Ii][Nn][Gg]", "[Ff][Ll][Oo][Aa][Tt]", "[Ii][Ff]", "[Ee][Ll][Ss][Ee]","[Pp][Rr][Oo][Tt][Oo][Tt][Yy][Pp][Ee]"
                          , "[Cc][Ll][Aa][Ss][Ss]","[Ww][Hh][Ii][Ll][Ee]","[Rr][Ee][Tt][Uu][Rr][Nn]","[Aa][Ii]_[Oo][Uu][Tt][Pp][Uu][Tt]","[Tt][Rr][Uu][Ee]"
                          ,"[Ff][Aa][Ll][Ss][Ee]","[Bb]_[Gg][Ii][Vv][Ee][Ii][Nn][Vv][Ii][Tt][Ee][Mm][Ss]"]



        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                        for pattern in keywordPatterns]


        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.magenta)
        self.highlightingRules.append((QRegExp("Q[A-Za-z]"),
                                        classFormat))

        veriable = QTextCharFormat()
        veriable.setForeground(QColor(89,136,250))
        self.highlightingRules.append((QRegExp("\\([^)]*\\)"),
                                               veriable))

        symbolsFormat = QTextCharFormat()
        symbolsFormat.setFontWeight(QFont.Bold)
        symbolsFormat.setForeground(QColor(255,182,0))
        self.highlightingRules.append((QRegExp("[(+*-/%&=;,.?!{})]"),
                                    symbolsFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor(27,148,22))
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                                               singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QColor(25,120,255))
        self.highlightingRules.append((QRegExp("[A-Za-z0-9_]+(?=\\()"),
                                               functionFormat))

        self.commentStartExpression = QRegExp("/*\\")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text,index+length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if  endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

                self.setFormat(startIndex, commentLength,
                        self.multiLineCommentFormat)
                startIndex = self.commentStartExpression.indexIn(text,
                           startIndex + commentLength)



if __name__ == '__main__':
     import sys

     app = QApplication(sys.argv)
     okno = Editer()
     sys.exit(app.exec_())

