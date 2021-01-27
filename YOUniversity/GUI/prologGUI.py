# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
#sys.path.append('C:\\Users\\Cugggino\\YOUniversity\\YOUniversity\\Prolog')
#from mainWindow import ROOT_DIR
from howToReachUsGUI import ROOT_DIR
sys.path.append(ROOT_DIR + '\\YOUniversity\\Prolog')
from prologGianni import ask_KB, new_kb
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Prolog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(701, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(701, 620))
        Dialog.setMaximumSize(QtCore.QSize(701, 620))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setWhatsThis("")
        #Dialog.setModal(True)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 10, 701, 73))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayoutTitle = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayoutTitle.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTitle.setObjectName("horizontalLayoutTitle")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutTitle.addItem(spacerItem)
        self.labelTitleProlog = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        self.labelTitleProlog.setFont(font)
        self.labelTitleProlog.setObjectName("labelTitleProlog")
        self.horizontalLayoutTitle.addWidget(self.labelTitleProlog)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutTitle.addItem(spacerItem1)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 239, 661, 351))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayoutOutput = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayoutOutput.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutOutput.setObjectName("horizontalLayoutOutput")
        self.showOutput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showOutput.setFont(font)
        self.showOutput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.showOutput.setWhatsThis("")
        self.showOutput.setUndoRedoEnabled(False)
        self.showOutput.setReadOnly(True)
        self.showOutput.setPlainText("")
        self.showOutput.setObjectName("showOutput")
        self.horizontalLayoutOutput.addWidget(self.showOutput)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 120, 661, 73))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayoutInput = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayoutInput.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutInput.setObjectName("horizontalLayoutInput")
        self.showInput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showInput.setFont(font)
        self.showInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.showInput.setWhatsThis("")
        self.showInput.setOverwriteMode(False)
        self.showInput.setObjectName("showInput")
        self.horizontalLayoutInput.addWidget(self.showInput)
        self.pushButtonSend = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSend.sizePolicy().hasHeightForWidth())
        self.pushButtonSend.setSizePolicy(sizePolicy)
        self.pushButtonSend.setMaximumSize(QtCore.QSize(49, 49))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSend.setFont(font)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.pushButtonSend.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalLayoutInput.addWidget(self.pushButtonSend)
        self.pushButtonExamples = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.pushButtonExamples.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonExamples.sizePolicy().hasHeightForWidth())
        self.pushButtonExamples.setSizePolicy(sizePolicy)
        self.pushButtonExamples.setMaximumSize(QtCore.QSize(49, 49))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonExamples.setFont(font)
        self.pushButtonExamples.setObjectName("pushButtonExamples")
        self.horizontalLayoutInput.addWidget(self.pushButtonExamples)
        self.labelInput = QtWidgets.QLabel(Dialog)
        self.labelInput.setGeometry(QtCore.QRect(30, 100, 41, 21))
        self.labelInput.setMaximumSize(QtCore.QSize(41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelInput.setFont(font)
        self.labelInput.setObjectName("labelInput")
        self.labelOutput = QtWidgets.QLabel(Dialog)
        self.labelOutput.setGeometry(QtCore.QRect(30, 220, 51, 21))
        self.labelOutput.setMaximumSize(QtCore.QSize(50, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelOutput.setFont(font)
        self.labelOutput.setObjectName("labelOutput")
        
        self.pushButtonSend.clicked.connect(self.sendAndSearch)
        self.pushButtonExamples.clicked.connect(self.showExamples)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #TODOself.showInput.placeholder("Inserisci qui il testo...")
        self.pushButtonGoBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonGoBack.setGeometry(QtCore.QRect(25, 25, 49, 49))
        self.pushButtonGoBack.setMaximumSize(QtCore.QSize(49, 49))
        self.pushButtonGoBack.setObjectName("pushButtonGoBack")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ROOT_DIR + "\\resources\\images\\menu\\goBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGoBack.setStyleSheet("background-color: rgb(55,117,169);")
        self.pushButtonGoBack.setIcon(icon)
        self.pushButtonGoBack.setIconSize(QtCore.QSize(49,49))
        self.pushButtonGoBack.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonGoBack.clicked.connect(Dialog.close) #commenta se effettui il run da questo file
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Interroga il sistema"))
        self.labelTitleProlog.setText(_translate("Dialog", "Interroga il sistema"))
        #self.showInput.setPlainText(_translate("Dialog", ""))
        self.pushButtonSend.setText(_translate("Dialog", "Invio"))
        self.pushButtonExamples.setToolTip(_translate("Dialog", "Mostra degli esempi"))
        self.pushButtonExamples.setText(_translate("Dialog", "?"))
        self.labelInput.setText(_translate("Dialog", "Input:"))
        self.labelOutput.setText(_translate("Dialog", "Console:"))

    def writeInput(self):
        self.showInput.clear()
        
    def sendAndSearch(self):
        query = self.showInput.toPlainText()
        font = QtGui.QFont()
        font.setPointSize(12)
        #font.setBold(True) #inutile metterlo perché il plainText modifica tutto il testo
        self.showOutput.setFont(font)
        self.showOutput.insertPlainText("- Input:\n" + query )
        self.showInput.clear()
        self.showOutput.insertPlainText("\n\n- Output:\n")
        results=ask_KB(new_kb, query)
        for r in results:
            self.showOutput.insertPlainText(r + "\n")
        self.showOutput.insertPlainText('----------------------------------------------------------------------------------------------------\n')
        
        
        
        
    def showExamples(self):
        """#da rimuovere se lascio il plaintext
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        """
        self.showOutput.insertPlainText('\n ESEMPI:\n'+
                                        '\t- insegna(Professore,Materia)\n' +
                                        '\t- in(Aula,Edificio)\n' +
                                        '\t- corso(Professore,Anno_corso)\n' +
                                        '\t- orario(Professore,Ora_inizio,Giorno)\n' +
                                        '\t- lezione(Materia,Ora_inizio,Giorno,Professore)\n' +
                                        '\t- classe(Anno_corso,Aula)\n'+
                                        '\t- luogo(Corso,Palazzo)\n' )
        """
        self.showOutput.setFont(font)
        self.setItalic(False)
        """
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_Prolog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

