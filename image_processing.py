
import os , re , cv2 , pytesseract
import numpy as np
from googletrans import Translator
from gtts import gTTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QIcon ,QPixmap
from langdetect import detect

class Ui_Image_Reader(object):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'

    def setupUi(self, Image_Reader):
        Image_Reader.setObjectName("Image_Reader")
        Image_Reader.resize(1154, 689)
        Image_Reader.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Image_Reader.setAutoFillBackground(False)
        Image_Reader.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"    background-color:rgb(200,200,200);\n"

"     background-position: center; /* Center the image */\n"
"     background-repeat: no-repeat;\n"  
"}\n"
"\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"      border-color: black;\n"
"      border-width: 1px 1px 1px 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Image_Reader)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(600, 10, 501, 451))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setObjectName("textEdit")
        self.buttonGetImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetImage.setGeometry(QtCore.QRect(40, 580, 81, 41))
        self.buttonGetImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGetImage.setObjectName("buttonGetImage")
        self.buttonExtractText = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText.setGeometry(QtCore.QRect(140, 580, 111, 41))
        self.buttonExtractText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonExtractText.setObjectName("buttonExtractText")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(700, 470, 131, 111))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_7.setObjectName("radioButton_7")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(10, 10, 571, 451))
        self.labelImage.setAutoFillBackground(False)
        self.labelImage.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.labelImage.resize(571, 451)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 590, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 470, 161, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.radioButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_6.setObjectName("radioButton_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(870, 480, 181, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.radioButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_9.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.radioButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_10.setObjectName("radioButton_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 610, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 580, 231, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        Image_Reader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Image_Reader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 21))
        self.menubar.setObjectName("menubar")
        Image_Reader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Image_Reader)
        self.statusbar.setObjectName("statusbar")
        Image_Reader.setStatusBar(self.statusbar)



        self.buttonGetImage.clicked.connect(self.getImage)
        self.radioButton.toggled.connect(self.checked)
        self.radioButton_5.toggled.connect(self.checked)
        self.radioButton_6.toggled.connect(self.checked)
        self.buttonExtractText.clicked.connect(self.extractText)

        self.pushButton.clicked.connect(self.submit)
        self.radioButton_3.toggled.connect(self.submit_dest)
        self.radioButton_2.toggled.connect(self.submit)
        self.radioButton_7.toggled.connect(self.submit)
        self.radioButton_4.toggled.connect(self.submit)
        self.pushButton_2.clicked.connect(self.work_space)


    ###  disable buttons at the start ####

        self.buttonGetImage.setEnabled(False)
        self.buttonExtractText.setEnabled(False)
        self.groupBox.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.groupBox_3.setEnabled(False)

        self.textEdit.setEnabled(False)
        self.labelImage.setEnabled(False)
        self.groupBox_2.setEnabled(False)

        self.retranslateUi(Image_Reader)
        QtCore.QMetaObject.connectSlotsByName(Image_Reader)

    def retranslateUi(self, Image_Reader):
        _translate = QtCore.QCoreApplication.translate
        Image_Reader.setWindowTitle(_translate("Image_Reader", "Image_Reader"))
        self.buttonGetImage.setText(_translate("Image_Reader", "Load Image"))
        self.buttonExtractText.setText(_translate("Image_Reader", "Extract Text"))
        self.groupBox.setTitle(_translate("Image_Reader", "choose action"))
        self.radioButton_2.setText(_translate("Image_Reader", "Clear"))
        self.radioButton_3.setText(_translate("Image_Reader", "Translate"))
        self.radioButton_4.setText(_translate("Image_Reader", "Listen To"))
        self.radioButton_7.setText(_translate("Image_Reader", "Save"))
        self.pushButton.setText(_translate("Image_Reader", "Submit"))
        self.groupBox_2.setTitle(_translate("Image_Reader", "choose original language"))
        self.radioButton.setText(_translate("Image_Reader", "Arabic"))
        self.radioButton_5.setText(_translate("Image_Reader", "English"))
        self.radioButton_6.setText(_translate("Image_Reader", "Frensh"))
        self.groupBox_3.setTitle(_translate("Image_Reader", "Choose destination language"))
        self.radioButton_8.setText(_translate("Image_Reader", "Arabic"))
        self.radioButton_9.setText(_translate("Image_Reader", "English"))
        self.radioButton_10.setText(_translate("Image_Reader", "Frensh"))
        self.pushButton_2.setText(_translate("Image_Reader", "Choose Your Work Space"))




### ---the user fisrt choose a folder to as its work space 

    def work_space(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.workSpace = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.textEdit_2.setText(self.workSpace)
        self.pushButton_2.setEnabled(False)
        self.textEdit_2.setEnabled(False)
        self.textEdit.setEnabled(True)
        self.labelImage.setEnabled(True)
        self.groupBox_2.setEnabled(True)


### checked(self) ---- if the user choose the image language --> enable the load image button  ---- ###

    def checked(self):
        self.buttonGetImage.setEnabled(True)        


    ''' getImage (self)
     browse to the image path with only the image filters
     make a copy of the image with th frame dim to display it 
     pass the resized image to set image to be displayed 
    
    '''

    def getImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(options=options)
        img = cv2.imread(self.fileName)
        dim=(571, 451)
        img2=cv2.resize(img,dim)
        yy = self.textEdit_2.toPlainText()+"\img2.jpg"
        cv2.imwrite(yy,img2)

        
        if self.fileName:
            print(self.fileName)
            pattern = ".(jpg|png|jpeg|bmp|jpe|tiff|JPG|PNG|JPEG|BMP|JPE|TIFF)$"
            if re.search(pattern,self.fileName):
                self.setImage(yy)

    '''
    setImage(self,fileName) --> display the image in the frame and enable the extract button
    '''
    def setImage(self,fileName):

        self.labelImage.setPixmap(QPixmap(fileName))
        print(fileName)
        self.buttonExtractText.setEnabled(True)


    '''
    extractText(self) 
    transform the image to gray scale and prieform threshold on it 
    based on the original languaage choosen the text will be extracted 
    the text is written in the text edit area
    '''

    def extractText(self):
        config_arabic = ('-l ara --psm 6')
        config_english = ('-l eng --oem 1 --psm 3')
        config_french = ('-l fra --oem 1 --psm 3')

        img = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        if  self.radioButton.isChecked() :  
            text = pytesseract.image_to_string(thresh, config=config_arabic)

        elif self.radioButton_5.isChecked() :
            text = pytesseract.image_to_string(thresh, config=config_english)

        elif self.radioButton_6.isChecked():
            text = pytesseract.image_to_string(thresh, config=config_french)

        self.textEdit.append(text)
        self.groupBox.setEnabled(True)

    '''
    submit_dest (self) 
    after the text is extracted we enable the action options
    '''

    def submit_dest (self):
        self.groupBox_3.setEnabled(True)
        self.radioButton_8.setChecked(True)
        if self.radioButton_8.isChecked() or self.radioButton_9.isChecked() or self.radioButton_10.isChecked()  :
            self.pushButton.setEnabled(True)


    '''
    submit (self) 
    the user can profom 4 actions 
    1- translate the text by choosing translate and choose the destination languae and click submit to translate 
    2- clear the text in the text area 
    3- save the text in a text file by chooseing the file name and path
    4- save the text as mp3 by chooseing the file name and path
    '''

    def submit(self):
        #self.pushButton.setEnabled(True)
        if self.radioButton_3.isChecked(): ## translate 
            #self.groupBox_3.setEnabled(True)
            dest = ""
            trans = Translator()
            text = self.textEdit.toPlainText()
            text =  text.replace("\n"," ")
            text =  text.replace(" ","  ")
            self.textEdit.clear()
            self.textEdit.setText(str(text))
            text = self.textEdit.toPlainText()

            if  self.radioButton_8.isChecked()  :
                dest ='ar'

            elif  self.radioButton_9.isChecked() :
                dest ='en'

            elif  self.radioButton_10.isChecked()  :
                dest ='fr'

            if  self.radioButton.isChecked()  :
               src ='ar'

            elif  self.radioButton_5.isChecked()  :
                src ='en'

            elif  self.radioButton_6.isChecked() :
                src ='fr'

            text = trans.translate(text , src = src, dest = dest)

            self.textEdit.setText(str(text.text))

        elif self.radioButton_7.isChecked(): ## save 
            self.groupBox_3.setEnabled(False)
            self.pushButton.setEnabled(False)
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(options=options)
            if fileName:
                print(fileName)
                file = open(fileName+ ".txt",'w', encoding="utf-8")
                text = self.textEdit.toPlainText()
                file.write(text)
                file.close()

        elif self.radioButton_2.isChecked(): ## clear 
            self.textEdit.clear()
            self.groupBox_3.setEnabled(False)
            self.pushButton.setEnabled(False)

        if self.radioButton_4.isChecked(): ## speaking  
            self.pushButton.setEnabled(False)
            self.groupBox_3.setEnabled(False)
            text = self.textEdit.toPlainText()
            lang = detect(text)
            tts = gTTS(text=text, lang=lang, slow=False) 
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(options=options)
            if fileName:
                tts.save(fileName+".mp3")









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image_Reader = QtWidgets.QMainWindow()
    ui = Ui_Image_Reader()
    ui.setupUi(Image_Reader)
    Image_Reader.show()
    sys.exit(app.exec_())
