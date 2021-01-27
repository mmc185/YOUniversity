# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from howToReachUsGUI import ROOT_DIR
sys.path.append(ROOT_DIR + '\\YOUniversity\\BayesianNetwork')

from bayesianNetwork import gradeBayesianInference
import numpy as np
from pgmpy.extern import tabulate # da rimuovere se nn funziona tabulate

class Ui_Dialog_predMark(object):
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
        #Dialog.setModal(True)
        
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        font.setBold(True)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 69, 681, 441))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        
        font.setPointSize(12)      
        #Creazione stackedWidget (che permette di cambiare pagina, passando a quella che mostra il contenuto)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget_7)
        self.stackedWidget.setObjectName("stackedWidget")
        #Creazione prima pagina
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
          
        self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        #self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(140, 530, 421, 71))
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setAutoDefault(False)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 10, 701, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayoutTitle = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayoutTitle.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTitle.setObjectName("horizontalLayoutTitle") 
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.labelTitlePredVoto = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.labelTitlePredVoto.setFont(font)
        self.labelTitlePredVoto.setObjectName("labelTitlePredVoto")
        self.horizontalLayoutTitle.addItem(spacerItem)        
        self.horizontalLayoutTitle.addWidget(self.labelTitlePredVoto)
        self.horizontalLayoutTitle.addItem(spacerItem1)
        
        font.setBold(False)        
        self.groupBoxQuestions = QtWidgets.QGroupBox(self.page_1)
        #self.groupBoxQuestions.setGeometry(QtCore.QRect(-10, 0, 601, 439))
        #self.groupBoxQuestions.setGeometry(QtCore.QRect(20, 10, 547, 421)) #left, top, width and height
        self.groupBoxQuestions.setGeometry(QtCore.QRect(0, 10, 601, 439))
        self.groupBoxQuestions.setFont(font)
        self.groupBoxQuestions.setTitle("")
        self.groupBoxQuestions.setObjectName("groupBoxQuestions")
        
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 390, 541, 31))
        self.horizontalLayoutWidget_5.setFont(font)
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(spacerItem2)
        
        #Creazione label relative alle domande
        font.setPointSize(14)
        #font.setItalic(False)
        self.labelFreeTime = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelFreeTime.setGeometry(QtCore.QRect(10, 5, 561, 31))
        self.labelFreeTime.setFont(font)
        self.labelFreeTime.setObjectName("labelFreeTime")
        self.labelStudyHard = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelStudyHard.setGeometry(QtCore.QRect(10, 90, 561, 41))
        self.labelStudyHard.setFont(font)
        self.labelStudyHard.setObjectName("labelStudyHard")
        self.labelAptitude = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelAptitude.setGeometry(QtCore.QRect(10, 190, 561, 21))
        self.labelAptitude.setFont(font)
        self.labelAptitude.setObjectName("labelAptitude")
        self.labelDifficulty = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelDifficulty.setGeometry(QtCore.QRect(10, 280, 561, 20))
        self.labelDifficulty.setFont(font)
        self.labelDifficulty.setObjectName("labelDifficulty")
        self.labelEmoFactor = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelEmoFactor.setGeometry(QtCore.QRect(10, 360, 561, 20))
        self.labelEmoFactor.setFont(font)
        self.labelEmoFactor.setObjectName("labelEmoFactor")
        
        
        #Creazione bottoni relativi alle domande
        font.setPointSize(12)  
        #font.setItalic(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 541, 31))
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rbFreeTime0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime0.setFont(font)
        self.rbFreeTime0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime0.setObjectName("rbFreeTime0")
        self.rbFreeTime1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime1.setFont(font)
        self.rbFreeTime1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime1.setObjectName("rbFreeTime1")
        self.rbFreeTime2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime2.setFont(font)
        self.rbFreeTime2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime2.setObjectName("rbFreeTime2")
        self.rbFreeTime3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime3.setFont(font)
        self.rbFreeTime3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime3.setObjectName("rbFreeTime3")
        self.rbFreeTime4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime4.setFont(font)
        self.rbFreeTime4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime4.setObjectName("rbFreeTime4")
        self.rbFreeTime5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFreeTime5.setFont(font)
        self.rbFreeTime5.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbFreeTime5.setObjectName("rbFreeTime5")
        
        #Raggruppo i radio buttons
        self.groupRBfreeTime = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.groupRBfreeTime.setContentsMargins(0, 0, 0, 0)
        self.groupRBfreeTime.setObjectName("groupRBfreeTime")
        self.groupRBfreeTime.addWidget(self.rbFreeTime0)
        self.groupRBfreeTime.addWidget(self.rbFreeTime1)
        self.groupRBfreeTime.addWidget(self.rbFreeTime2)
        self.groupRBfreeTime.addWidget(self.rbFreeTime3)
        self.groupRBfreeTime.addWidget(self.rbFreeTime4)
        self.groupRBfreeTime.addWidget(self.rbFreeTime5)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 541, 31))
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.rbStudyHard0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbStudyHard0.setFont(font)
        self.rbStudyHard0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbStudyHard0.setObjectName("rbStudyHard0")
        self.rbStudyHard1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbStudyHard1.setFont(font)
        self.rbStudyHard1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbStudyHard1.setObjectName("rbStudyHard1")
        self.rbStudyHard2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbStudyHard2.setFont(font)
        self.rbStudyHard2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbStudyHard2.setObjectName("rbStudyHard2")
        self.rbStudyHard3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbStudyHard3.setFont(font)
        self.rbStudyHard3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbStudyHard3.setObjectName("rbStudyHard3")
        #Raggruppo i radio buttons
        self.groupRBstudyHard = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.groupRBstudyHard.setContentsMargins(0, 0, 0, 0)
        self.groupRBstudyHard.setObjectName("groupRBstudyHard")
        self.groupRBstudyHard.addWidget(self.rbStudyHard0)
        self.groupRBstudyHard.addWidget(self.rbStudyHard1)
        self.groupRBstudyHard.addWidget(self.rbStudyHard2)
        self.groupRBstudyHard.addWidget(self.rbStudyHard3)
       
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 220, 541, 31))
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.rbAptitude0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbAptitude0.setFont(font)
        self.rbAptitude0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbAptitude0.setObjectName("rbAptitude0")
        self.rbAptitude1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbAptitude1.setFont(font)
        self.rbAptitude1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbAptitude1.setObjectName("rbAptitude1")
        self.rbAptitude2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbAptitude2.setFont(font)
        self.rbAptitude2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbAptitude2.setObjectName("rbAptitude2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 310, 541, 31))
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        #Raggruppo i radio buttons
        self.groupRBAptitude = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.groupRBAptitude.setContentsMargins(0, 0, 0, 0)
        self.groupRBAptitude.setObjectName("groupRBAptitude")
        self.groupRBAptitude.addWidget(self.rbAptitude0)
        self.groupRBAptitude.addWidget(self.rbAptitude1)
        self.groupRBAptitude.addWidget(self.rbAptitude2)
        
        self.rbDifficulty0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbDifficulty0.setFont(font)
        self.rbDifficulty0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDifficulty0.setObjectName("rbDifficulty0")
        self.rbDifficulty1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbDifficulty1.setFont(font)
        self.rbDifficulty1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDifficulty1.setObjectName("rbDifficulty1")
        self.rbDifficulty2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbDifficulty2.setFont(font)
        self.rbDifficulty2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDifficulty2.setObjectName("rbDifficulty2")
        self.rbDifficulty3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbDifficulty3.setFont(font)
        self.rbDifficulty3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDifficulty3.setObjectName("rbDifficulty3")
        #Raggruppo i radio buttons
        self.groupRBDifficulty = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.groupRBDifficulty.setContentsMargins(0, 0, 0, 0)
        self.groupRBDifficulty.setObjectName("groupRBDifficulty")
        self.groupRBDifficulty.addWidget(self.rbDifficulty0)
        self.groupRBDifficulty.addWidget(self.rbDifficulty1)
        self.groupRBDifficulty.addWidget(self.rbDifficulty2)
        self.groupRBDifficulty.addWidget(self.rbDifficulty3)
      
        self.rbEmoFactor0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.rbEmoFactor0.setFont(font)
        self.rbEmoFactor0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbEmoFactor0.setObjectName("rbEmoFactor0")
        self.rbEmoFactor1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.rbEmoFactor1.setFont(font)
        self.rbEmoFactor1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbEmoFactor1.setObjectName("rbEmoFactor1")
        self.rbEmoFactor2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.rbEmoFactor2.setFont(font)
        self.rbEmoFactor2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbEmoFactor2.setObjectName("rbEmoFactor2")
        #self.horizontalLayout.addWidget(self.groupBoxQuestions)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        #Raggruppo i radio buttons
        self.groupRBEmoFactor = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.groupRBEmoFactor.setContentsMargins(0, 0, 0, 0)
        self.groupRBEmoFactor.setObjectName("groupRBEmoFactor")
        self.groupRBEmoFactor.addWidget(self.rbEmoFactor0)
        self.groupRBEmoFactor.addWidget(self.rbEmoFactor1)
        self.groupRBEmoFactor.addWidget(self.rbEmoFactor2)
        
        #Imposto "non specificato" come scelta di default
        self.rbFreeTime0.setChecked(True)
        self.rbStudyHard0.setChecked(True)
        self.rbAptitude0.setChecked(True)
        self.rbEmoFactor0.setChecked(True)
        self.rbDifficulty0.setChecked(True)
              
       
        #Pagina 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.showResults = QtWidgets.QPlainTextEdit(self.page_2)
        self.showResults.setGeometry(QtCore.QRect(20, 10, 547, 321))
        #self.showResults.setGeometry(QtCore.QRect(20, 10, 547, 421))
        #self.showResults.setGeometry(QtCore.QRect(20, 10, 547, 241))
        #self.showResults.setGeometry(QtCore.QRect(20, 10, 320, 240))
        font.setFamily('Consolas')
        font.setPointSize(16)
        self.showResults.setFont(font)
        self.showResults.setReadOnly(True)       
        self.showResults.setObjectName("showResults")
        self.labelLegendTitle = QtWidgets.QLabel(self.page_2)
        self.labelLegendTitle.setGeometry(QtCore.QRect(30, 350, 191, 21))
        font.setFamily('MS Shell Dlg 2')
        font.setPointSize(13)
        self.labelLegendTitle.setFont(font)
        self.labelLegendTitle.setObjectName("labelLegendTitle")
        self.labelLegend = QtWidgets.QLabel(self.page_2)
        self.labelLegend.setGeometry(QtCore.QRect(30, 370, 521, 71))
        font.setPointSize(10)
        self.labelLegend.setFont(font)
        self.labelLegend.setObjectName("labelLegend")
        
                
        """
        self.showResults = QtWidgets.QTextEdit(self.page_2)
        self.showResults.setGeometry(QtCore.QRect(20, 10, 547, 421))
        self.showResults.setReadOnly(True)
        """
        font.setFamily('MS Shell Dlg 2')
        font.setPointSize(14)
        font.setBold(True)
        self.pushButtonGoBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonGoBack.hide()
        self.pushButtonGoBack.setGeometry(QtCore.QRect(140, 530, 421, 71))
        self.pushButtonGoBack.setFont(font)
        self.pushButtonGoBack.setAutoDefault(False)
        self.pushButtonGoBack.setObjectName("pushButtonGoBack")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.pushButtonGoBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonGoBack.setGeometry(QtCore.QRect(15, 15, 40, 40))
        self.pushButtonGoBack.setMaximumSize(QtCore.QSize(49, 49))
        self.pushButtonGoBack.setObjectName("pushButtonGoBack")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ROOT_DIR + "\\resources\\images\\menu\\goBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGoBack.setStyleSheet("background-color: rgb(55,117,169);")
        self.pushButtonGoBack.setIcon(icon)
        self.pushButtonGoBack.setIconSize(QtCore.QSize(49,49))
        self.pushButtonGoBack.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonGoBack.clicked.connect(Dialog.close) #commenta se effettui il run da questo file
        

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0) #Seleziona la prima pagina da mostrare
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButtonCalculate.clicked.connect(self.predVoto)
        self.pushButtonGoBack.clicked.connect(self.goBack)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Predizione del voto"))
        self.pushButtonCalculate.setText(_translate("Dialog", "Quale potrebbe essere l\'esito dell\'esame?"))
        self.labelTitlePredVoto.setText(_translate("Dialog", "Predizione del voto - Calcolo "))
        self.labelFreeTime.setText(_translate("Dialog", "- Quanto tempo libero hai al giorno da dedicare allo studio?"))
        self.rbFreeTime0.setText(_translate("Dialog", "non specificato"))
        self.rbFreeTime1.setText(_translate("Dialog", "un\'ora"))
        self.rbFreeTime2.setText(_translate("Dialog", "2 ore"))
        self.rbFreeTime3.setText(_translate("Dialog", "3 ore"))
        self.rbFreeTime4.setText(_translate("Dialog", "4 ore"))
        self.rbFreeTime5.setText(_translate("Dialog", "5 ore o più"))
        self.labelStudyHard.setText(_translate("Dialog", "- Quante ore al giorno dedichi effettivamente allo studio?"))
        self.rbStudyHard0.setText(_translate("Dialog", "non specificato"))
        self.rbStudyHard1.setText(_translate("Dialog", "meno di 2 ore"))
        self.rbStudyHard2.setText(_translate("Dialog", "tra 2 e 4 ore"))
        self.rbStudyHard3.setText(_translate("Dialog", "più di 4 ore"))
        self.labelAptitude.setText(_translate("Dialog", "- Ti senti portato per questa materia?"))
        self.rbAptitude0.setText(_translate("Dialog", "non specificato"))
        self.rbAptitude1.setText(_translate("Dialog", "no"))
        self.rbAptitude2.setText(_translate("Dialog", "sì"))
        self.rbDifficulty0.setText(_translate("Dialog", "non specificato"))
        self.rbDifficulty1.setText(_translate("Dialog", "facile"))
        self.rbDifficulty2.setText(_translate("Dialog", "medio"))
        self.rbDifficulty3.setText(_translate("Dialog", "difficile"))
        self.labelDifficulty.setText(_translate("Dialog", "- Seleziona la difficoltà dell\'esame:"))
        self.rbEmoFactor0.setText(_translate("Dialog", "non specificato"))
        self.rbEmoFactor1.setText(_translate("Dialog", "no"))
        self.rbEmoFactor2.setText(_translate("Dialog", "sì"))
        self.labelEmoFactor.setText(_translate("Dialog", "- Sei una persona ansiosa durante gli esami?"))
        self.pushButtonCalculate.setText(_translate("Dialog", "Quale potrebbe essere l\'esito dell\'esame?"))
        self.showResults.setPlainText(_translate("Dialog", ""))
        self.labelLegendTitle.setText(_translate("Dialog", "Legenda"))
        self.labelLegend.setText(_translate("Dialog", 
                                            "- Voto(0): Voto compreso tra 18 e 23\n"
                                            "- Voto(1): Voto compreso tra 24 e 27\n"
                                            "- Voto(2): Voto compreso tra 28 e 30L\n"
                                            "- phi(Voto): probabilità che abbia preso un voto appartenente a quel range"))
        
        
        
    # in base alle scelte effettuate, calcola il voto
    def predVoto(self):
        self.labelTitlePredVoto.setText("Predizione del voto - Risultati ")
        self.stackedWidget.setCurrentIndex(1) #Mostra la pagina dei risultati
        self.pushButtonCalculate.hide()
        self.pushButtonGoBack.show()
        d_freeTime = {  self.rbFreeTime1: 0, 
                        self.rbFreeTime2: 1, 
                        self.rbFreeTime3: 2,
                        self.rbFreeTime4: 3,
                        self.rbFreeTime5: 4 }
        
        d_studiedHard =   { self.rbStudyHard1: 0, 
                          self.rbStudyHard2: 1, 
                          self.rbStudyHard3: 2  }
        
        d_aptitude =      { self.rbAptitude1: 0,
                          self.rbAptitude2: 1   }
        
        d_emoFactor =     { self.rbEmoFactor1: 0,
                          self.rbEmoFactor2: 1  }
            
        d_difficulty =    { self.rbDifficulty1: 0, 
                          self.rbDifficulty2: 1, 
                          self.rbDifficulty3: 2 }
                        
        evidences = {} #dizionario contenente le stringhe
      
        #in base alle scelte, aggiorna evidences
        for i in d_freeTime:    #Tempo libero
            if i.isChecked():
                evidences.update({'Tempo libero': d_freeTime[i]})
                
            
        for i in d_studiedHard: #Studiato molto
            if i.isChecked():
                evidences.update({'Studiato molto': d_studiedHard[i]})
               
        for i in d_aptitude:    #Attitudine
            if i.isChecked(): 
                evidences.update({'Attitudine': d_aptitude[i]})
                
      
        for i in d_emoFactor:   #Fattore emotivo
            if i.isChecked():
                evidences.update({'Fattore Emotivo': d_emoFactor[i]})
      
        for i in d_difficulty:  #Difficolta
            if i.isChecked():
                evidences.update({'Difficolta': d_difficulty[i]})
        #votoOffer.get_value(Voto=0)
        if bool(evidences) == False:
            self.showResults.setPlainText('Errore.\nPer poter ottenere una predizione, tornare indietro e selezionare almeno uno dei parametri.')
        else:
            self.res = gradeBayesianInference(evidences)
            self.showResults.setPlainText( str(gradeBayesianInference(evidences)) )
        
        #print('Evidenze: ')
        #print(evidences)    
        #esempio: {'Tempo libero': 4, 'Studiato molto': 2, 'Attitudine': 1, 'Fattore Emotivo': 0, 'Difficolta': 0}
        #self.showResults.setPlainText( str(gradeBayesianInference(evidences)) )
        #print(gradeBayesianInference(evidences))
        
        
    def goBack(self):
        self.labelTitlePredVoto.setText("Predizione del voto - Calcolo ")
        self.pushButtonCalculate.show()
        self.pushButtonGoBack.hide()
        
        self.stackedWidget.setCurrentIndex(0) #Torna alla pagina delle domande
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_predMark()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
