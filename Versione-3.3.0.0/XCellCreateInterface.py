'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import os
import XCell
import CreateInterface
import XCellMainInterface

'''Create xCELL Interface'''
class XCellCreateInterface(QtWidgets.QMainWindow):
    def __init__(self, obj, parent=None):
        super(XCellCreateInterface, self).__init__(parent)
        
        self.obj = obj
        
        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("xCELL")
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
        self.label.setText("File Excel created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap(os.path.join(os.path.realpath(''), "image", "xcell.png")))
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Close")
        self.button.setStyleSheet("background-color: green; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
        
        '''Vertical Layout settings'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        
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
    
    '''Button function'''
    def on_pushButton_clicked(self):
        self.hide()
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = XCellMainInterface.XCellMainInterface(self.obj, self)
        self.hide()
        dialog.show()