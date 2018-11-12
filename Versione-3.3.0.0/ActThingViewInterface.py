'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import os
import ActThingMainInterface

'''Act Thing View Interface Interface'''
class ActThingViewInterface(QtWidgets.QMainWindow): 
    def __init__(self, dict_response, parent=None):
        super(ActThingViewInterface, self).__init__(parent)
        
        self.dict_response = dict_response

        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("actTHING")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "acthing.png")))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
      
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Send Report")
        self.button.setStyleSheet("background-color: orange; color: white; height:50; border-radius:10")
        self.button.setFont(font)
                       
        '''Table settings'''
        self.table = QtWidgets.QTableWidget()   
        self.table.setFont(font)               
        self.table.setRowCount(len(self.dict_response))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Status', 'Message'])
        
        self.table.setColumnWidth(0,500)
        self.table.setColumnWidth(1,500)

        '''Table triggers'''
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        '''Grid layout'''
        grid = QtWidgets.QGridLayout()  
        grid.addWidget(self.table, 0, 0)
        grid.addWidget(self.button, 1, 0)
        
        '''Layout QWidget'''
        layout = QtWidgets.QWidget()
        layout.setLayout(grid)
        
        '''Layout QMainWindow'''
        self.setCentralWidget(layout)
        
        '''Toolbar'''
        toolbar = self.addToolBar('Toolbar')
        toolbar.setMovable(False)
        toolbar.setIconSize(QtCore.QSize(40,40))
        toolbar.setFont(fontToolbar)
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        '''Icon toolbar'''
        '''Back application'''
        back_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","backicon.png")), 'Back', self)
        back_act.setShortcut('Ctrl+B')
        back_act.setStatusTip('Return to main Interface')
        
        '''Act toolbar'''
        toolbar.addAction(back_act)
        
        '''Toolbar triggered'''
        back_act.triggered.connect(self.returnFirstInterface)
  
        '''Table population'''
        count = 0  
        for status, message in self.dict_response.items():
            self.table.setItem(count,0,QtWidgets.QTableWidgetItem(status))
            self.table.setItem(count,1,QtWidgets.QTableWidgetItem(message))  
            count +=1
 
        '''Button clicked'''       
        self.button.clicked.connect(self.on_pushButton_clicked)
    
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = ActThingMainInterface.ActThingMainInterface(self)
        self.hide()
        dialog.show()
    
    '''Button function'''    
    def on_pushButton_clicked(self):
        ''''''