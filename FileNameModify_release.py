"""
2021-01-13 10点20分 初步完成，下一步增加一个初始化界面得操作，目前只能修改一次
2021-02-07 11点56分 可以进入到其他路径下进行文件名称的重命名批量修改，但是若再次进去其他路径下，得全部关闭重新来才可以

"""
from Window_UI import mainWindow as ui #从ui文件夹导入
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os


# targetPath = r"D:\1Desktop\Python_project\FileNameModify\testFiles"
targetPath =  r"D:\Google download\google download\MP3"
oldstring = "" #myfreemp3.vip
newstring = ""

def ReadFileName(spath):
    path = spath
    files = os.listdir(path)  # 得到文件夹下的所有文件名称 是 list类型
    # print(files)
    return files


class MyMainForm(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.Initialize()# 初始化设置，含初始化默认参数
         self.Function()  # 添加登录按钮信号和槽。注意display函数不加小括号()


    def Initialize(self):
        print('窗口初始化')
        self.tableWidget.horizontalHeader().resizeSection(1, 600)  # 设置第2列的宽度为200
        self.TargetPath = targetPath
        self.lineEditFilePath.setText(self.TargetPath)




    def Function(self):
        print("Function")
        self.pushButtonPathOK.clicked.connect(self.PathOK)
        self.pushButtonCopyAllName.clicked.connect(self.copyName)
        self.pushButtonOK.clicked.connect(self.ok)
        self.pushButtonReplace.clicked.connect(self.replace)

    def PathOK(self):
        print("PathOK")
        # self.tableWidget.clear()
        self.TargetPath = self.lineEditFilePath.text()
        self.oldListFiles = ReadFileName( self.lineEditFilePath.text() ) # 旧的名称列表
        #初始化参数
        self.newListFiles = []  #存放名称
        self.lineEditOldString.setText(oldstring)
        self.lineEditNewString.setText(newstring)
        # 把路径名称都写到 表格第0列当中
        for i in self.oldListFiles:
            rowNo = self.tableWidget.rowCount() #返回行号
            self.tableWidget.insertRow(rowNo) #插入一行i
            self.tableWidget.setItem(rowNo, 0, QTableWidgetItem(i))

    def copyName(self):
        # print("copyName")
        # #重新更新旧字符串————————————————————————————
        # self.tableWidget.clear()
        # self.oldListFiles = ReadFileName(targetPath)  # 旧的名称列表
        # for i in self.oldListFiles:
        #     rowNo = self.tableWidget.rowCount() #返回行号
        #     self.tableWidget.insertRow(rowNo) #插入一行i
        #     self.tableWidget.setItem(rowNo, 0, QTableWidgetItem(i))
        #再copy————————————————————————————
        row = self.tableWidget.rowCount() # 获取表格中当前总行数
        for one in range(0,row):
            text = self.tableWidget.item(one,0).text()
            # print(text)
            self.newListFiles.append(text)
            self.tableWidget.setItem(one,1,QTableWidgetItem(text))

    def replace(self):
        print("replace")
        if self.tableWidget.item(1,1) == None:
            QMessageBox.warning(self, "警告", "新名称为空，请赋值", QMessageBox.Yes)
            return
        newlist = []
        tempOldString = self.lineEditOldString.text()
        tempNewString = self.lineEditNewString.text()
        for i in self.newListFiles:
            i = i.replace(tempOldString, tempNewString)
            newlist.append(i)
        # print(newlist)
        # 把修改后的字符串重新赋值
        for one in range(0, self.tableWidget.rowCount()):
            self.tableWidget.setItem(one, 1, QTableWidgetItem(newlist[one]))
        self.newListFiles = newlist

    def ok(self):
        print("ok函数")
        os.chdir(self.TargetPath) #进入到当前路径
        for i in range(0, self.tableWidget.rowCount()):
            try:
                tempOldString = self.oldListFiles[i]
                tempNewString = self.tableWidget.item(i,1).text()
                os.rename(tempOldString, tempNewString)  # 重命名
                print("重命名完毕")
            except(FileNotFoundError):
                print("目录不存在")







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainForm()   #初始化
    window.show()       #将窗口控件显示在屏幕上
    sys.exit(app.exec_())  #程序运行，sys.exit方法确保程序完整退出