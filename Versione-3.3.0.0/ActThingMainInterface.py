'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui
import os
import utility
import activation
import ActThingViewInterface

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
        
        '''Label settings'''
        self.account_label = QtWidgets.QLabel()
        self.api_id_label = QtWidgets.QLabel()

        self.account_label.setText("Account ")
        self.api_id_label.setText("API Id: ")

        '''Combo box settings'''
        self.combo_box_account = QtWidgets.QComboBox()
        self.combo_box_account.addItems(utility.readJsonFile(os.path.join(os.path.realpath(''), "configuration", "accountConfiguration.json")))

        self.combo_box_api_id = QtWidgets.QComboBox()
        self.combo_box_api_id.addItems(utility.readJsonFile(os.path.join(os.path.realpath(''), "configuration", "apiIdConfiguration.json")))

        '''Button settings'''
        self.button = QtWidgets.QPushButton("Activate Things")
        self.button.setStyleSheet("background-color: orange; color: white; height:50; border-radius:10")
        self.button.setFont(font)

        if(type(obj) != list):
            '''Create list file .json'''
            self.list_file_json = utility.createFileList(os.path.join(self.obj.json_files_path, self.obj.name_hierarchy), ".json")
        else:
            self.list_file_json = obj
            
        vbox = QtWidgets.QVBoxLayout()

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
        
        vbox.addLayout(grid)
        vbox.addWidget(self.account_label)
        vbox.addWidget(self.combo_box_account)
        vbox.addWidget(self.api_id_label)
        vbox.addWidget(self.combo_box_api_id)
        vbox.addWidget(self.button)

        '''Layout QWidget'''
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
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
        dict_response = activation.initializeActivations(self.obj.name_hierarchy, self.list_file_json, self.combo_box_account.currentText(), self.combo_box_api_id.currentText())
