import sys

from PyQt5.QtCore import QRegExp

from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

import xml_read

# Return Formated Text with attributes

def format(color, style=''):

    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format

xml_read.read_style_from_xml()

array_color = []
array_color.extend(xml_read.xml_color[0])

STYLES = {
    'keyword': format(array_color[0]),
    'operator': format(array_color[1]),
    'comment': format(array_color[2]),
    'function': format(array_color[3]),
    'string': format(array_color[4]),
    'numbers': format(array_color[5])
}


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        xml_read.read_keywords_from_xml(self)

        array_from_xml = xml_read.xml_data

        self.rules = []

        self.rules += [(QRegExp(r'\b%s\b' % keyword, 0), STYLES['keyword'])for keyword in
                       array_from_xml[0]]
        self.rules += [(QRegExp(r'%s' % operator, 0), STYLES['operator']) for operator in
                       array_from_xml[1]]
        self.rules += [(QRegExp(r'\b%s\b' % func, 0), STYLES['function'])for func in
                       array_from_xml[2]]
        self.rules += [(QRegExp(r'"[^"\\]*(\\.[^"\\]*)*"', 0), STYLES['string']),
                       (QRegExp(r"'[^'\\]*(\\.[^'\\]*)*'", 0), STYLES['string']),
                       (QRegExp(r'//[^\n]*', 0), STYLES['comment']),
                       (QRegExp(r'\b[+-]?[0-9]+[lL]?\b', 0), STYLES['numbers']),
                       (QRegExp(r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0), STYLES['numbers']),
                       (QRegExp(r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0), STYLES['numbers'])]
        # Multi-Line to repair don't set color
        self.commentStartExpression = QRegExp("/*\\")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index+length)

        self.setCurrentBlockState(0)

        startindex = 0
        if self.previousBlockState() != 1:
            startindex = self.commentStartExpression.indexIn(text)

        while startindex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startindex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentlenght = len(text) - startindex
            else:
                commentlenght = endIndex - startindex + self.commentEndExpression.matchedLength()

                self.setFormat(startindex, commentlenght,
                        self.multiLineCommentFormat)
                startindex = self.commentStartExpression.indexIn(text,
                           startindex + commentlenght)
