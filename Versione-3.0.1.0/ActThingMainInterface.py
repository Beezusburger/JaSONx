'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui
import os
import utility

'''Main actTHING Interface'''
class ActThingMainInterface(QtWidgets.QMainWindow):
    def __init__(self, obj, parent=None):
        super(ActThingMainInterface, self).__init__(parent)
        self.obj = obj

        '''Window settings'''
        self.setWindowTitle("actTHING")
        self.setFixedSize(1050,600) 
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.realpath(''), "image" , "acthing.png")))

        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Activate Things")
        self.button.setStyleSheet("background-color: orange; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        

        if(type(obj) != list):
            '''Create list file .json'''
            self.list_file_json = utility.createFileList(os.path.join(self.obj.json_files_path, self.obj.name_hierarchy), ".json")
        else:
            self.list_file_json = obj
            
        '''Layout settings'''
        grid = QtWidgets.QGridLayout()   
        self.table = QtWidgets.QTableWidget()   
        self.table.setFont(font)               
        self.table.setRowCount(len(self.list_file_json))
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["File JSON"])
        self.table.setColumnWidth(0,1000)

        '''Grid Layout'''
        grid.addWidget(self.table, 0, 0)
        grid.addWidget(self.button, 1, 0)
        
        '''Layout QWidget'''
        layout = QtWidgets.QWidget()
        layout.setLayout(grid)
        
        '''Layout QMainWindow'''
        self.setCentralWidget(layout)

        '''Table settings'''
        count = 0
        for file in self.list_file_json:
            self.table.setItem(count,0,QtWidgets.QTableWidgetItem(file))
            count +=1
            
        '''Button clicked'''
        self.button.clicked.connect(self.on_pushButton_clicked)
    
    '''Button function'''    
    def on_pushButton_clicked(self):
        ''''''
        