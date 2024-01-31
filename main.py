import sys
import io

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from io import BytesIO
from PIL import Image
import requests

ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1124</width>
    <height>867</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Яндекс карты</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1121</width>
      <height>831</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1124</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui)
        uic.loadUi(f, self)
        self.w, self.h = 1121, 831
        self.resize(self.w, self.h)
        self.map_api_server = "http://static-maps.yandex.ru/1.x/"
        self.lon = "37.40551"
        self.lat = "69.12412"
        self.delta = "0.002"

        self.map_params = {
            "ll": ",".join([self.lon, self.lat]),
            "spn": ",".join([self.delta, self.delta]),
            "l": "map"
        }

        self.response = requests.get(self.map_api_server, params=self.map_params)
        self.im = Image.open(BytesIO(self.response.content))
        self.im.save('maps.png')
        self.pix = QtGui.QPixmap('maps.png')
        self.image.setPixmap(self.pix)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
