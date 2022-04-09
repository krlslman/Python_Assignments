# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Rock_Pap_Scis.ui'

from cgitb import text
from json.tool import main
from re import X
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice

class Ui_MainWindow(object):

    def __init__(self):  # variable'ları initialize etmek için en başa yazılır. Aşağılarda kullanabilmek için.
        self.score_user_sh = 0
        self.score_cpu_sh = 0


    def setupUi(self, MainWindow):
        # path_ = str("C:\\Users\koral\\Desktop\\CLARUSWAY\For GitHub\\Assigments & SelfProjects\\220221_RockPaperScissors\\")
        global path_
        path_ = r"C:/Users/koral/Desktop/CLARUSWAY/For GitHub/Assigments & SelfProjects/220221_RockPaperScissors/"


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 446)
        MainWindow.setFixedSize(825, 446)
        MainWindow.setStyleSheet("background-color: rgb(141, 91, 145);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pic_p1 = QtWidgets.QLabel(self.centralwidget)
        self.pic_p1.setGeometry(QtCore.QRect(50, 0, 261, 261))
        self.pic_p1.setText("")
        self.pic_p1.setPixmap(QtGui.QPixmap(path_ + "q_mark.png"))
        self.pic_p1.setScaledContents(True)
        self.pic_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_p1.setObjectName("pic_p1")

        self.pic_p2 = QtWidgets.QLabel(self.centralwidget)
        self.pic_p2.setGeometry(QtCore.QRect(530, 0, 261, 261))
        self.pic_p2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pic_p2.setText("")
        self.pic_p2.setPixmap(QtGui.QPixmap(path_ + "q_mark.png"))
        self.pic_p2.setScaledContents(True)
        self.pic_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_p2.setObjectName("pic_p2")

        self.pbttn_rock = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clicked_rock())
        self.pbttn_rock.setGeometry(QtCore.QRect(280, 330, 91, 51))
        self.pbttn_rock.setStyleSheet("background-color: rgb(221, 72, 112)")
        self.pbttn_rock.setObjectName("pbttn_rock")

        self.pbttn_paper = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clicked_paper())
        self.pbttn_paper.setGeometry(QtCore.QRect(370, 330, 91, 51))
        self.pbttn_paper.setStyleSheet("background-color: rgb(255, 221, 85);")
        self.pbttn_paper.setObjectName("pbttn_paper")

        self.pbttn_scissors = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clicked_scissors())
        self.pbttn_scissors.setGeometry(QtCore.QRect(460, 330, 91, 51))
        self.pbttn_scissors.setStyleSheet("background-color: rgb(115, 218, 225);")
        self.pbttn_scissors.setObjectName("pbttn_scissors")

        self.lbl_whowin = QtWidgets.QLabel(self.centralwidget)
        self.lbl_whowin.setGeometry(QtCore.QRect(300, 110, 241, 100))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.lbl_whowin.setFont(font)
        self.lbl_whowin.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_whowin.setObjectName("lbl_whowin")

        self.lbl_namep1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_namep1.setGeometry(QtCore.QRect(60, 250, 241, 41))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.lbl_namep1.setFont(font)
        self.lbl_namep1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_namep1.setObjectName("lbl_namep1")

        self.lbl_namep2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_namep2.setGeometry(QtCore.QRect(540, 250, 241, 41))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        
        self.lbl_namep2.setFont(font)
        self.lbl_namep2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_namep2.setObjectName("lbl_namep2")

        self.lbl_score = QtWidgets.QLabel(self.centralwidget)
        self.lbl_score.setGeometry(QtCore.QRect(380, 260, 81, 41))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.lbl_score.setFont(font)
        self.lbl_score.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_score.setObjectName("lbl_score")

        self.lbl_score_p1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_score_p1.setGeometry(QtCore.QRect(320, 260, 51, 41))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.lbl_score_p1.setFont(font)
        self.lbl_score_p1.setStyleSheet("background-color: rgb(168, 255, 130);")
        self.lbl_score_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_score_p1.setObjectName("lbl_score_p1")
        self.lbl_score_p2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_score_p2.setGeometry(QtCore.QRect(470, 260, 51, 41))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.lbl_score_p2.setFont(font)
        self.lbl_score_p2.setStyleSheet("background-color: rgb(255, 152, 152);")
        self.lbl_score_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_score_p2.setObjectName("lbl_score_p2")

        self.pbttn_reset = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset_button())
        self.pbttn_reset.setGeometry(QtCore.QRect(750, 350, 51, 31))
        self.pbttn_reset.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"border-color: rgb(7, 7, 7);\n" 
"color: rgb(255, 255, 255);")
        self.pbttn_reset.setObjectName("pbttn_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #-------------------GAME CONTROLS------------------------------------

    def clicked_rock(self):  # runs when clicked to ROCK push button
        global clickedname
        clickedname = "R"
        self.the_round()
    def clicked_paper(self):  # runs when clicked to PAPER push button
        global clickedname
        clickedname = "P"
        self.the_round()
    def clicked_scissors(self): # runs when clicked to SCISSORS push button
        global clickedname
        clickedname = "S"
        self.the_round()

    def reset_button(self):  # runs when clicked to RESET push button
        self.score_user_sh = 0
        self.score_cpu_sh = 0
        self.pic_p2.setPixmap(QtGui.QPixmap(path_ + "q_mark.png"))
        self.pic_p1.setPixmap(QtGui.QPixmap(path_ + "q_mark.png"))
        self.update_labels()

    def update_labels(self):
        self.lbl_whowin.setText("Let's see \nwho will win!")  # Title
        self.lbl_score_p1.setText(str(self.score_user_sh))  # User Score
        self.lbl_score_p2.setText(str(self.score_cpu_sh))  # CPU Score

    def the_round(self):
        # ------------------------CPU Player--------------------
        cpu_choice = choice(["R","P","S","R","P","S","R","P","S","R","P","S","R","P","S","R","P","S","R","P","S","R","P","S","R","P","S","R","P","S"])

        if cpu_choice == "R":
            self.pic_p2.setPixmap(QtGui.QPixmap(str(path_) + "rock.png"))  # set ROCK image if R is pressed
        elif cpu_choice == "P":
            self.pic_p2.setPixmap(QtGui.QPixmap(str(path_) + "paper.png"))  # set PAPER image if R is pressed
        elif cpu_choice == "S":
            self.pic_p2.setPixmap(QtGui.QPixmap(str(path_) + "scissors.png")) # set SCISSORS image if R is pressed
        else:
            print("Error 113,   cpu_choice : ", cpu_choice," clickedname : ",clickedname)

        # -----------------------PLAYER 1-----------------
        
        if clickedname == "R":
            self.pic_p1.setPixmap(QtGui.QPixmap(str(path_) + "rock.png"))  # set ROCK image if R is pressed
        elif clickedname == "P":
            self.pic_p1.setPixmap(QtGui.QPixmap(str(path_) + "paper.png"))  # set PAPER image if R is pressed
        elif clickedname == "S":
            self.pic_p1.setPixmap(QtGui.QPixmap(str(path_) + "scissors.png"))  # set SCISSORS image if R is pressed
        else:
            print("Error 114,   cpu_choice : ", cpu_choice," clickedname : ",clickedname)

        #--------------------SCORES AND TITLES-------------
        

        #CALCULATIONS ::

        # DRAWN
        if clickedname == cpu_choice:  
            self.lbl_whowin.setText("It's drawn!")
            self.lbl_score_p1 .setText(str(self.score_user_sh))
            self.lbl_score_p2 .setText(str(self.score_cpu_sh))
        else:
            # YOU WİN
            if (clickedname == "R" and cpu_choice =="S") or (clickedname == "P" and cpu_choice =="R") or (clickedname == "S" and cpu_choice =="P"):  
                self.score_user_sh += 1
                self.lbl_score_p1.setText(str(self.score_user_sh))
                self.lbl_whowin.setText("You win!")
                
            # YOU LOST
            elif (clickedname == "R" and cpu_choice =="P") or (clickedname == "P" and cpu_choice =="S") or (clickedname == "S" and cpu_choice =="R"):
                self.score_cpu_sh += 1
                self.lbl_score_p2.setText(str(self.score_cpu_sh))
                self.lbl_whowin.setText("You lost!")
                
            else: #debugger
                print("Error 115,   cpu_choice : ", cpu_choice," clickedname : ",clickedname)
            print(str(path_)+"rock.png")
            print(type(path_))

    
         

    """ TO DO
        v   Score hesapla; İki sonuç eşitse değişmez, kim yendiğini bul ve +1 yap
        v   Pencere boyutu sabit olsun
        v   path_'ler variable'lara tanımlanıp def ile image atamalar yapılabilir
            Score'u 10'a ulaşan olunca "Player X win the game" yazsın, RESET butonu yerine "Play Again" yazsın
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock - Paper - Scissors Game   by Koral"))
        self.pbttn_rock.setText(_translate("MainWindow", "ROCK"))
        self.pbttn_paper.setText(_translate("MainWindow", "PAPER"))
        self.pbttn_scissors.setText(_translate("MainWindow", "SCISSORS"))
        self.lbl_whowin.setText(_translate("MainWindow", "Let's see who\n will win!"))
        self.lbl_namep1.setText(_translate("MainWindow", "You"))
        self.lbl_namep2.setText(_translate("MainWindow", "NPC"))
        self.lbl_score.setText(_translate("MainWindow", "Score"))
        self.lbl_score_p1.setText(_translate("MainWindow", "0"))
        self.lbl_score_p2.setText(_translate("MainWindow", "0"))
        self.pbttn_reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

