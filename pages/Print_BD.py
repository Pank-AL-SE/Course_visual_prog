from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
from lib.baselib import Database

class Print_BD(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вывод базы")
        self.setGeometry(300,250,729,300)
        self.setFixedSize(729,300)

        self.table = QTableWidget(self)
        self.table.move(0,0)
        self.table.setFixedSize(729,300)
        self.table.setColumnCount(9) 
        self.table.setHorizontalHeaderLabels(["ФИО", "Серия паспорта", "Номер паспорта",
                                               "Дата выдачи", "Кем выдан",
                                                 "Прописка", "Должность",
                                                   "Оклад", "Наличие мед.книжки"])
        
        self.table.horizontalHeaderItem(0).setToolTip("FIO")
        self.table.horizontalHeaderItem(1).setToolTip("ser_pas")
        self.table.horizontalHeaderItem(2).setToolTip("num_pas")
        self.table.horizontalHeaderItem(3).setToolTip("date_pas")
        self.table.horizontalHeaderItem(4).setToolTip("place_pas")
        self.table.horizontalHeaderItem(5).setToolTip("place_live")
        self.table.horizontalHeaderItem(6).setToolTip("work")
        self.table.horizontalHeaderItem(7).setToolTip("price")
        self.table.horizontalHeaderItem(8).setToolTip("med")

        
        
        self.table.resizeColumnsToContents()


        self.check = Database.print_db(self)             
        cnt = self.table.rowCount()
        for i in range(len(self.check)):
            self.table.insertRow(self.table.rowCount())                                        
            for j in range(9):
                item = QTableWidgetItem(self.check[i][j])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable) 
                if j == 8 and self.check[i][j] == '1':
                    self.table.setItem(cnt+i, j, QTableWidgetItem("+"))
                elif j == 8 and self.check[i][j] == '0':
                    self.table.setItem(cnt+i, j, QTableWidgetItem("-"))
                else:
                    self.table.setItem(cnt+i, j, item)
                        