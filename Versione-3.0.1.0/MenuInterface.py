'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui
import os
import configuration

'''Change Hierarchy path Interface'''
class ChangePathHierarchyInterface(QtWidgets.QWidget):
    path = ""
    def __init__(self):
        super(ChangePathHierarchyInterface, self).__init__()
        self.resize(700, 400)
        self.setWindowTitle("Change Hierarchy path")
        self.show()
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Save")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''TreeView'''
        self.treeView = QtWidgets.QTreeView()
        
        '''File System'''
        self.fileSystemModel = QtWidgets.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel.setRootPath(os.path.realpath(''))
        self.treeView.setModel(self.fileSystemModel)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
      
    '''Tree clicked function'''
    def on_select(self, index):
        global path
        path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Change hierarchy path?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.change_hierarchy_path(path)
            if(response == True):
                msgBox.about(self, "Change hierarchy path", "Changed path!")   
            else:
                msgBox.critical(self, "Change hierarchy path", "Error!")
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Change Excel path Interface'''
class ChangePathExcelInterface(QtWidgets.QWidget):
    path = ""
    def __init__(self):
        super(ChangePathExcelInterface, self).__init__()
        self.resize(700, 400)
        self.setWindowTitle("Change Excel path")
        self.show()
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Save")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''TreeView'''
        self.treeView = QtWidgets.QTreeView()
        
        '''File System'''
        self.fileSystemModel = QtWidgets.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel.setRootPath(os.path.realpath(''))
        self.treeView.setModel(self.fileSystemModel)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
      
    '''Tree clicked function'''
    def on_select(self, index):
        global path
        path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Change excel_files path?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.change_excel_path(path)
            if(response == True):
                msgBox.about(self, "Change excel_files path", "Changed path!")      
            else:
                msgBox.critical(self, "Change excel_files path", "Error")
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Change json path file'''
class ChangePathJsonFileInterface(QtWidgets.QWidget):
    path = ""
    def __init__(self):
        super(ChangePathJsonFileInterface, self).__init__()
        self.resize(700, 400)
        self.setWindowTitle("Change Json path")
        self.show()
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Save")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''TreeView'''
        self.treeView = QtWidgets.QTreeView()
        
        '''File System'''
        self.fileSystemModel = QtWidgets.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel.setRootPath(os.path.realpath(''))
        self.treeView.setModel(self.fileSystemModel)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
    
    '''Tree clicked function'''
    def on_select(self, index):
        global path
        path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Change json_files path?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.change_json_path(path)
            if(response == True):
                msgBox.about(self, "Change json_files path", "Changed path!")   
            else:
                msgBox.critical(self, "Change json_files path", "Error!")
        self.close()
   