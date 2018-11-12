'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import os
import CreateInterface
import XCellCreateInterface
import XCell


'''MAIN xCELL Interface'''
class XCellMainInterface(QtWidgets.QMainWindow):
    def __init__(self, obj, parent=None):
        super(XCellMainInterface, self).__init__(parent)
        
        self.obj = obj

        '''Window settings'''
        self.setWindowTitle("xCELL")
        self.setFixedSize(1050,600) 
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "logo.png")))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
        self.setFont(font)
        
        '''Label settings'''
        self.title_label = QtWidgets.QLabel()
        self.site_name_label = QtWidgets.QLabel()
        self.json_folder_label = QtWidgets.QLabel()
        self.json_path_label = QtWidgets.QLabel()
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        '''Label text'''
        self.title_label.setPixmap(QtGui.QPixmap(os.path.join(os.path.realpath(''), "image", "title2.png")))
        self.site_name_label.setText("Site Name: ")
        self.json_folder_label.setText("Json Folder: ")        
        self.json_path_label.setText(self.obj.name_hierarchy)
        
        '''Textbox settings'''
        self.site_name_text = QtWidgets.QLineEdit(self) 
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Create Excel")
        self.button.setStyleSheet("background-color: green; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
    
        '''Grid layout'''
        grid = QtWidgets.QGridLayout()  
        grid.addWidget(self.site_name_label, 0, 0)
        grid.addWidget(self.site_name_text, 0, 1)  
        grid.addWidget(self.json_folder_label, 1, 0)
        grid.addWidget(self.json_path_label, 1, 1)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addLayout(grid)
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
        objXCell = XCell.XCell(self.site_name_text.text(), self.obj.name_hierarchy, self.obj.environment_prefix, self.obj.dict_meters)
        dialog = XCellCreateInterface.XCellCreateInterface(self.obj, self)
        self.hide()
        dialog.show()
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = CreateInterface.CreateInterface(self.obj, self)
        self.hide()
        dialog.show()