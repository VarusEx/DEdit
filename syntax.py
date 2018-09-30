import sys

from PyQt5.QtCore import QRegExp, Qt

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


STYLES = {
    'keyword': format('darkBlue'),
    'operator': format('red'),
    'comment': format('darkGreen'),
    'brace': format('darkGray'),
    'function': format('yellow'),
    'string': format('green'),
    'numbers': format('blue')
}


class Highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        array_from_xml = xml_read.xmldata
        rules = []

        rules += [(QRegExp(pattern), STYLES['keyword'])for pattern in
                  array_from_xml[0]]

        rules += [(QRegExp(func), STYLES['function'])for func in
                  array_from_xml[4]]

        rules += [(QRegExp(operator), STYLES['operator'])for operator in
                  array_from_xml[1]]

        rules.append((QRegExp("//[^\n]*"), STYLES['comment']))

        rules += [
        # Numeric light
        (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
        (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
        (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]
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

        startindex = 0
        if self.previousBlockState() != 1:
            startindex = self.commentStartExpression.indexIn(text)

        while startindex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startindex)

            if  endIndex == -1:
                self.setCurrentBlockState(1)
                commentlenght = len(text) - startindex
            else:
                commentlenght = endIndex - startindex + self.commentEndExpression.matchedLength()

                self.setFormat(startindex, commentlenght,
                        self.multiLineCommentFormat)
                startindex = self.commentStartExpression.indexIn(text,
                           startindex + commentlenght)
