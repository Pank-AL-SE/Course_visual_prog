from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
from lib.baselib import Database

class End_Work(QWidget):
    def __init__(self,foo,table):
        super().__init__()
       
        self.foo = foo
        self.tab = table
        
        self.setWindowTitle("Увольнение с работы")
        self.setGeometry(300,250,600,300)
        self.setFixedSize(600,300)
        self.pass_info = QVBoxLayout()
        self.work_info = QVBoxLayout()

        self.FIO = QLineEdit(self)
        self.FIO.move(75, 25)
        self.FIO.resize(500,25)
        self.FIO.setPlaceholderText("ФИО")
        self.pass_info.addWidget(self.FIO)

        self.ser_pass = QLineEdit(self)
        self.ser_pass.move(75, 75)
        self.ser_pass.resize(102,25)
        self.ser_pass.setPlaceholderText("Серия паспорта")
        self.pass_info.addWidget(self.ser_pass)

        self.num_pass = QLineEdit(self)
        self.num_pass.move(200, 75)
        self.num_pass.resize(100,25)
        self.num_pass.setPlaceholderText("Номер паспорта")
        self.pass_info.addWidget(self.num_pass)

        self.date_pass = QLineEdit(self)
        self.date_pass.move(325, 75)
        self.date_pass.resize(75,25)
        self.date_pass.setPlaceholderText("Дата выдачи(хх.хх.хххх)")
        self.pass_info.addWidget(self.date_pass)

        self.place_pass = QLineEdit(self)
        self.place_pass.move(425, 75)
        self.place_pass.resize(150,100)
        self.place_pass.setPlaceholderText("Кем выдан")
        self.pass_info.addWidget(self.place_pass)

        self.place_live = QLineEdit(self)
        self.place_live.move(75, 125)
        self.place_live.resize(325,50)
        self.place_live.setPlaceholderText("Прописка")
        self.pass_info.addWidget(self.place_live)

        self.work = QLineEdit(self)
        self.work.move(75, 200)
        self.work.resize(400,25)
        self.work.setPlaceholderText("Должность")
        self.work_info.addWidget(self.work)

        self.reason = QLineEdit(self)
        self.reason.move(75, 250)
        self.reason.resize(300,25)
        self.reason.setPlaceholderText("Причина увальнения")
        self.work_info.addWidget(self.reason)

        self.lbl_med = QLabel(self)
        self.lbl_med.move(410,230)
        self.lbl_med.resize(75,20)
        self.lbl_med.setText("Мед.Кн.")
        self.work_info.addWidget(self.lbl_med)

        self.med_yes = QCheckBox('Да', self) 
        self.med_yes.move(400,250)
        self.work_info.addWidget(self.med_yes)

        self.med_no = QCheckBox('Нет', self) 
        self.med_no.move(450,250)
        self.work_info.addWidget(self.med_no)

        #check on yes and no
        self.btn_save = QPushButton(self)
        self.btn_save.setText("Уволить\n с работы")
        self.btn_save.move(500,200)
        self.btn_save.resize(75,75)
        self.btn_save.clicked.connect(self.catch_data)

    
    
    def catch_data(self):
        self.a = self.FIO.text()
        if len(self.a) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите ФИО')
            return 0
        
        self.b = self.ser_pass.text()
        if len(self.b) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите серию паспорта')
            return 0
        
        try:
            self.b = int(self.b)
            
        except:
            QMessageBox.warning(self, 'Warning', 'Серия не число')
            return 0

        self.c = self.num_pass.text()
        if len(self.c) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите номер паспорта')
            return 0
        
        try:
            self.c = int(self.c)
        except:
            QMessageBox.warning(self, 'Warning', 'Номер не число')
            return 0
        self.d = self.date_pass.text()
        if len(self.d) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите дату выдачи паспорта')
            return 0
        self.e = self.place_pass.text()
        if len(self.e) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите место выдачи паспорта')
            return 0
        self.f = self.place_live.text()
        if len(self.f) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите прописку')
            return 0
        self.g = self.work.text()
        if len(self.g) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите должность')
            return 0
        self.h = self.reason.text()
        if len(self.h) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите причину')
            return 0
        if self.med_yes.isChecked() and self.med_no.isChecked() :
            QMessageBox.warning(self, 'Warning', 'Вы ввели да и нет в выборе мед.книжки')
            return 0
        elif self.med_yes.isChecked():
            self.i = 1
        elif self.med_no.isChecked():
            self.i = 0
        else:
            QMessageBox.warning(self, 'Warning', 'Выберите вариант с мед.книжкой')
            return 0
        qm = QMessageBox()
        ret = qm.question(self,'', "Вы уверены, что зотите удалить данного пользователя?", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            try:
                today = datetime.datetime.today()
                Database.save_end(self,today.strftime("%d.%m.%Y"),self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i)
                QMessageBox.information(self, 'Success', 'Данные успешно сохранены')
                self.foo(self.tab)
                return 0
            except:
                QMessageBox.warning(self, 'Warning', 'Данные не сохранены')
                return 0
        else:
            QMessageBox.warning(self, 'Warning', 'Данные не сохранены')
        
        
        



        

        





        
    
    