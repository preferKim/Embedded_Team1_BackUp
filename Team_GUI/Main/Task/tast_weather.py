import sys
import urllib.request
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from news_scrap import naver_weather,naver_current_weather_Icon # 함수 불러오기

class weatherWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(weatherWindow, self).__init__(parent)
        uic.loadUi("Task/task_weather.ui", self)
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("Weather") # 윈도우 타이틀 설정        
        self.show()

        self.btn_back.clicked.connect(self.backToMainWindow)
        self.btn_back.setStyleSheet("color: #000000; border-style: solid; border-width: 2px; border-color: #000000; border-radius: 10px; font:bold;")

        self.label_text.setStyleSheet("color: #000000; border-style: solid; border-width: 2px; border-color: #000000; border-radius: 10px; font:bold;")
        self.label_text.setFont(QFont("나눔", 15))
        self.label_text.setText(naver_weather())
        
        
        
        # 날씨 아이콘
        wt = naver_current_weather_Icon()
        url = f"https://ssl.pstatic.net/static/weather/image/icon_weather/{wt}.svg"
        image = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(180 , 180)
        self.label_icon1.setPixmap(pixmap)




    def backToMainWindow(self):
        self.close()