'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import os
import XCell
import MainInterface
import ViewInterface
import XCellMainInterface
import ActThingMainInterface


'''Create Json Interface'''
class CreateInterface(QtWidgets.QMainWindow):
    def __init__(self, obj, parent=None):
        super(CreateInterface, self).__init__(parent)
        
        self.obj = obj

        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("JaSONx - version 3.0.0.0")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "logo.png")))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
        self.setFont(font)
        
        '''Label settings'''
        self.label = QtWidgets.QLabel()
        self.image_label = QtWidgets.QLabel()
        self.label.setText("Files JSON created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap(os.path.join(os.path.realpath(''), "image", "logo.png")))
        
        '''Button settings'''
        self.buttonMain = QtWidgets.QPushButton("Main")
        self.buttonMain.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.buttonMain.setFont(font)
        self.buttonMain.clicked.connect(self.on_pushButton_clicked)
        
        self.buttonActivateThing = QtWidgets.QPushButton("Activate Things")
        self.buttonActivateThing.setStyleSheet("background-color: orange; color: white; height:50; border-radius:10")
        self.buttonActivateThing.setFont(font)
        self.buttonActivateThing.clicked.connect(self.activate_thing)
        
        self.buttonExcel = QtWidgets.QPushButton("Create file Excel")
        self.buttonExcel.setStyleSheet("background-color: green; color: white; height:50; border-radius:10")
        self.buttonExcel.setFont(font)
        self.buttonExcel.clicked.connect(self.create_excel)
        
        '''Horizontal layout'''
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.buttonExcel)
        hbox.addWidget(self.buttonActivateThing)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.buttonMain)
        
        '''Layout QWidget'''
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
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
    
    '''Button main function'''
    def on_pushButton_clicked(self):
        dialog = MainInterface.MainInterface(self)
        self.hide()
        dialog.show()
        
    '''Button excel function'''
    def create_excel(self):
        dialog = XCellMainInterface.XCellMainInterface(self.obj, self)
        dialog.show()
    
    '''Button activate thing function'''
    def activate_thing(self):
        dialog = ActThingMainInterface.ActThingMainInterface(self.obj, self)
        dialog.show()
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = ViewInterface.ViewInterface(self.obj, self)
        self.hide()
        dialog.show()