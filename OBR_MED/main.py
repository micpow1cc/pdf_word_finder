import torch
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
import pandas as pd
import IPython
import requests
import torchvision
import yaml
import tqdm
import seaborn
import os

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QUrl


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()


class AppDemo(QMainWindow):

    def __init__(self):
        global info, model
        super().__init__()
        self.resize(1200, 600)

        self.listbox_view = ListBoxWidget(self)

        self.btn = QPushButton('Get Value', self)
        self.btn.setGeometry(850, 400, 200, 50)
        self.btn.clicked.connect(lambda: print(self.getSelectedItem()))

        info = self.btn.clicked.connect(lambda: print(self.getSelectedItem()))
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp23/weights/last.pt',
                              force_reload=False)
        #img = info
        #results = model(img)

    def getSelectedItem(self):
        global model

        item = QListWidgetItem(self.listbox_view.currentItem())

        path = item.text()
        if path.endswith('.png'):
            img =path
            results = model(img)
        else:
            print("Zły format pliku")
        return results

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    #print_amount_of_teeth()
    demo.show()

    sys.exit(app.exec_())


