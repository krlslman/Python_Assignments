from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pytube import YouTube
import sys

class Window(QMainWindow): # Window = Pencere
	def __init__(self):
		super().__init__()
		self.userinterface_set()

	def userinterface_set(self):  # setUI
		self.settings() 
		#UI
		self.menu()		
		self.show()

	def menu(self):
		widget = QWidget()
		h_box = QHBoxLayout()

		#Main Elements
		text = QLabel("<b>Enter YouTube link :</b>")
		self.link.setPlaceholderText("https://")
		self.link = QLineEdit() #?
		button = QPushButton("DOWNLOAD")
		##############

		button.clicked.connect(self.download)
		h_box.addWidget(text)
		h_box.addWidget(self.link)
		h_box.addWidget(button)

		widget.setLayout(h_box)   #??????
		self.setCentralWidget(widget)

	def download(self):
		url =self.link.text()
		YouTube(url).streams.get_highest_resolution().download()

	def settings(self):  # ustAyarlar
		self.setWindowTitle("My Youtube Downloader v.1.0")
		self.setWindowIcon(QIcon("downloadicon.png"))

		# Size Settings
		self.setGeometry(250,250,600,80)
		self.setMaximumSize(900,80)
		self.setMinimumSize(610,90)

if __name__ == "__main__" :
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())

