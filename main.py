from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt,QTimer
import sys
import os
from pages.start_work import Start_Work
from pages.end_work import End_Work
from pages.find_in_base import Find_in_Base
from pages.Print_BD import Print_BD
from lib.baselib import Database
import openpyxl

class MainWindow(QMainWindow):
    def __init__(self):
 
        super(MainWindow,self).__init__()
        

        self.setWindowTitle("Учет кадров")
        self.setGeometry(300,250,700,400)
        self.setFixedSize(800,400)

    #label
    #    self.lbl = QtWidgets.QLabel(self)
     #   self.lbl.setText("test")
      #  self.lbl.setFont(QFont('Arial', 30))
       # self.lbl.move(0,0)
        #self.lbl.adjustSize()

        self.hbox = QVBoxLayout()
    #PushButton
        self.btn_start_work = QtWidgets.QPushButton(self)
        self.btn_start_work.setText("Устроить на работу")
        self.btn_start_work.move(0,0)
        self.btn_start_work.setFixedSize(385,100)
        self.hbox.addWidget(self.btn_start_work)
        self.btn_start_work.clicked.connect(self.switch_Start_work)
        self.btn_end_work = QtWidgets.QPushButton(self)
        self.btn_end_work.setText("Уволить с работы")
        self.btn_end_work.move(0,100)
        self.btn_end_work.setFixedSize(385,100)
        
        self.hbox.addWidget(self.btn_end_work)

        self.btn_end_work.clicked.connect(self.switch_End_work)
        self.btn_find_in_base = QtWidgets.QPushButton(self)
        self.btn_find_in_base.setText("Поиск по базе")
        self.btn_find_in_base.setFixedSize(385,100)
        self.btn_find_in_base.move(0,200)
        self.btn_find_in_base.setFixedSize(385,100)
        self.hbox.addWidget(self.btn_find_in_base)
        self.btn_find_in_base.clicked.connect(self.switch_Find_in_Base)

        # self.btn_print_base = QtWidgets.QPushButton(self)
        # self.btn_print_base.setText("Вывод базы")
        # self.btn_print_base.move(0,300)
        # self.btn_print_base.setFixedSize(385,100)
        # self.hbox.addWidget(self.btn_print_base)
        # self.btn_print_base.clicked.connect(self.switch_print_bd)

        self.btn_print_clear = QtWidgets.QPushButton(self)
        self.btn_print_clear.setText("Распечатать договор")
        self.btn_print_clear.setFixedSize(385,100)
        self.btn_print_clear.move(0,300)
        self.hbox.addWidget(self.btn_print_clear)
        self.btn_print_clear.clicked.connect(self.print_clear)

        # self.btn_print_excel = QtWidgets.QPushButton(self)
        # self.btn_print_excel.setText("Вывод в Excel")
        # self.btn_print_excel.setFixedSize(385,100)
        # self.btn_print_excel.move(0,500)
        # self.hbox.addWidget(self.btn_print_excel)
        # self.btn_print_excel.clicked.connect(self.print_excel)        
        

    
    
        self.lbl = QLabel(self)
        self.lbl.setText("История")
        self.lbl.move(385+150,0)
        self.lbl.resize(600,25)
        
        #table
        self.table = QTableWidget(self)  # Create a table
        self.table.move(385,25)
        self.table.setFixedSize(450,380)
        
        self.table.setColumnCount(4) 
        self.table.setHorizontalHeaderLabels(["дата",
            "                 ФИО                "
                                              , "       Должность      "
                                              , "    Статус    "])
        
        self.table.horizontalHeaderItem(0).setToolTip("Date")
        self.table.horizontalHeaderItem(1).setToolTip("FIO")
        self.table.horizontalHeaderItem(2).setToolTip("work")
        self.table.horizontalHeaderItem(3).setToolTip("status")
        

        self.update_data(self.table)
                        

        
        # Do the resize of the columns by content
        
    

    def print_clear(self):
        os.startfile(os.path.abspath('../coursevisualka/Clear.docx'),'print')

    def update_data(self,table):
        self.check = Database.print_hist(self) 
       
        check = Database.print_hist(self)    
        cnt = self.table.rowCount()
        for i in range(len(self.check)):
            if self.table.rowCount() < len(self.check):
                self.table.insertRow(self.table.rowCount())                                        
            for j in range(4):
                item = QTableWidgetItem(self.check[i][j])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable) 
                self.table.setItem(i, j, item)  

    # def print_excel(self):
    #     wb = openpyxl.load_workbook("Check.xlsx")
    #     ws = wb['Лист1']
    #     alf = ['A','B','C','D','E','F','G','H','I']
    #     check = Database.print_db(self)
    #     print(check)
    #     z = 0
    #     print(check)    
    #     rows = self.table.rowCount() 
    #     for i in range(rows):
    #         for j in range(len(alf)):
    #             value = self.table.itemAt(i, j).text()
    #             ws[alf[j]+str(i+2)].value = value
    #     wb.save("Check.xlsx")
    
    def switch_Start_work(self):        
        self.mainwindow = Start_Work(self.update_data,self.table)
        self.mainwindow.show()
    def switch_End_work(self):        
        self.mainwindow = End_Work(self.update_data,self.table)
        self.mainwindow.show()
    def switch_Find_in_Base(self):        
        self.mainwindow = Find_in_Base()
        self.mainwindow.show()
    def switch_print_bd(self):
        self.mainwindow = Print_BD()
        self.mainwindow.show()

    






        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style/style.css", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    mainwindow = MainWindow()    
    mainwindow.show()
    app.exec()
    