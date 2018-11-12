'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import JaSONx
import os
import xCELL
import utility
import configuration
import win32com.shell.shell as shell

'''::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''
'''Administrator permission script'''
'''
ASADMIN = 'asadmin'
if sys.argv[-1] != ASADMIN:
   script = os.path.abspath(sys.argv[0])
   params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
   shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
'''
'''::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''

'''
class actThingCreateInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(actThingCreateInterface, self).__init__(parent)
      
        self.setFixedSize(1050,600)
        self.setWindowTitle("xCELL")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\image.png'))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setFont(font)
        
        
        self.label = QtWidgets.QLabel()
        self.image_label = QtWidgets.QLabel()
        self.label.setText("File Excell Created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap('image\\image.png'))
        
      
        self.button = QtWidgets.QPushButton("Close")
        self.button.setStyleSheet("background-color: green; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
        
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.label)
        
        vbox.addWidget(self.button)
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        self.setCentralWidget(layout)
    
 
    def on_pushButton_clicked(self):
        self.hide()
        
'''

'''Main actTHING Interface'''
class actThingMainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(actThingMainInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setWindowTitle("actTHING")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\image.png'))

        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Activate Things")
        self.button.setStyleSheet("background-color: orange; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''Create list file .json'''
        self.list_file_json = utility.createListFile(JaSONx.jsonPath+JaSONx.name_file_hierarchy[:-4], ".json")
        
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
    
'''______________________________________________________________________________________________________________________________'''

'''Create xCELL Interface'''
class xCellCreateInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(xCellCreateInterface, self).__init__(parent)
      
        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("xCELL - v 1.0")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\image.png'))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Label settings'''
        self.label = QtWidgets.QLabel()
        self.image_label = QtWidgets.QLabel()
        self.label.setText("File Excell Created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap('image\\image.png'))
        
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
    
    '''Button function'''
    def on_pushButton_clicked(self):
        self.hide()
        
'''______________________________________________________________________________________________________________________________'''

'''MAIN xCELL Interface'''
class xCellMainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(xCellMainInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setWindowTitle("xCELL")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\image.png'))

        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Label settings'''
        self.title_label = QtWidgets.QLabel()
        self.site_name_label = QtWidgets.QLabel()
        self.json_folder_label = QtWidgets.QLabel()
        self.json_path_label = QtWidgets.QLabel()
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        '''Label text'''
        self.title_label.setPixmap(QtGui.QPixmap('image\\title2.png'))
        self.site_name_label.setText("Site Name: ")
        self.json_folder_label.setText("Json Folder: ")        
        self.json_path_label.setText(JaSONx.name_file_hierarchy[:JaSONx.name_file_hierarchy.find(".")])
        
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
    
    '''Button function'''    
    def on_pushButton_clicked(self):
        xCELL.setConstantData(self.site_name_text.text(),
                              JaSONx.name_file_hierarchy[:JaSONx.name_file_hierarchy.find(".")]
                              )
        dialog = xCellCreateInterface(self)
        self.hide()
        dialog.show()

'''______________________________________________________________________________________________________________________________'''


'''Create Json Interface'''
class CreateInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CreateInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("JaSONx")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Label settings'''
        self.label = QtWidgets.QLabel()
        self.image_label = QtWidgets.QLabel()
        self.label.setText("Files JSON created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap('image\\logo.png'))
        
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
    
    '''Button main function'''
    def on_pushButton_clicked(self):
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
        
    '''Button excel function'''
    def create_excel(self):
        dialog = xCellMainInterface(self)
        dialog.show()
    
    '''Button activate thing function'''
    def activate_thing(self):
        dialog = actThingMainInterface(self)
        dialog.show()

'''______________________________________________________________________________________________________________________________'''
       
'''View Json Interface'''
class ViewInterface(QtWidgets.QMainWindow):
        
    def __init__(self, parent=None):
        super(ViewInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("JaSONx")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
        
        '''Dict -> {meter_name : {meter_model:val , n_measures_sel:val}}'''
        self.dictmeters = JaSONx.createDictMeters()
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Generate JSON")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
                
        
        
        '''Table settings'''
        self.table = QtWidgets.QTableWidget()   
        self.table.setFont(font)               
        self.table.setRowCount(len(self.dictmeters))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Meter Name', 'Model'])
       
   
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
  
        '''Table population'''
        count = 0  
        for meter, model in self.dictmeters.items():
            self.table.setItem(count,0,QtWidgets.QTableWidgetItem(meter))
            self.table.setItem(count,1,QtWidgets.QTableWidgetItem(model))  
            count +=1
 
        '''Button clicked'''       
        self.button.clicked.connect(self.on_pushButton_clicked)
    
    '''Button function'''    
    def on_pushButton_clicked(self):
        JaSONx.startCreateJSON(self.dictmeters)
        dialog = CreateInterface(self)
        self.hide()
        dialog.show()
        
'''______________________________________________________________________________________________________________________________'''

'''Main Json Interface'''
class MainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setWindowTitle("JaSONx - v 1.1")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
       
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Label settings'''
        self.title_label = QtWidgets.QLabel()
        self.user_name_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.match_group_value_label = QtWidgets.QLabel()
        self.combo_box_hierarchy_label = QtWidgets.QLabel()
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        '''Label text'''
        self.title_label.setPixmap(QtGui.QPixmap('image\\title.png'))
        self.user_name_label.setText("Username: ")
        self.password_label.setText("Password: ")
        self.match_group_value_label.setText("Match group value: ")
        self.combo_box_hierarchy_label.setText("Hierarchy: ")
        
        '''Textbox settings'''
        self.user_name_text = QtWidgets.QLineEdit(self)
        self.password_text = QtWidgets.QLineEdit(self)
        self.match_group_value_text = QtWidgets.QLineEdit(self)  
        
        '''Combobox settings'''
        self.combo_box_hierarchy = QtWidgets.QComboBox()
        self.combo_box_hierarchy.addItems(JaSONx.getListHierarchy())
    
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Send data")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
    
        
        '''Grid layout'''
        grid = QtWidgets.QGridLayout()  
        grid.addWidget(self.user_name_label, 0, 0)
        grid.addWidget(self.user_name_text, 0, 1)  
        grid.addWidget(self.password_label, 1, 0)
        grid.addWidget(self.password_text, 1, 1)
        grid.addWidget(self.match_group_value_label, 2, 0)
        grid.addWidget(self.match_group_value_text, 2, 1)
        grid.addWidget(self.combo_box_hierarchy_label, 3, 0)
        grid.addWidget(self.combo_box_hierarchy, 3, 1)
        
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

        '''Menu settings'''
        '''Configuration Json path'''
        configJsonPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Json Path Configuration', self)        
        configJsonPathAct.setShortcut('Ctrl+J')
        configJsonPathAct.setStatusTip('')
        configJsonPathAct.triggered.connect(self.changePathJsonFile)

        '''Configuration Hierarchy path'''
        configHierarchyPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Hierarchy Path Configuration', self)        
        configHierarchyPathAct.setShortcut('Ctrl+H')
        configHierarchyPathAct.setStatusTip('')
        configHierarchyPathAct.triggered.connect(self.changePathHierarchy)
        
        '''Configuration Excel path'''
        configExcelPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Excel Path Configuration', self)        
        configExcelPathAct.setShortcut('Ctrl+E')
        configExcelPathAct.setStatusTip('')
        configExcelPathAct.triggered.connect(self.changePathExcel)

        '''Add Hierarchy'''
        addHierarchyAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Add New Hierachy', self)        
        addHierarchyAct.setShortcut('Ctrl+N')
        addHierarchyAct.setStatusTip('')
        addHierarchyAct.triggered.connect(self.addHierarchy)

        '''Add Json template'''
        addTemplateAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Add New Template', self)        
        addTemplateAct.setShortcut('Ctrl+T')
        addTemplateAct.setStatusTip('')
        addTemplateAct.triggered.connect(self.addTemplate)
        
        '''Reset paths default'''
        resetPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Reset Path to Default', self)        
        resetPathAct.setShortcut('Ctrl+R')
        resetPathAct.setStatusTip('')
        resetPathAct.triggered.connect(configuration.reset_path)
        
        '''Refresh window'''
        refreshAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Refresh', self)        
        refreshAct.setShortcut('Ctrl+F')
        refreshAct.setStatusTip('')
        refreshAct.triggered.connect(self.refreshWindow)

        '''Add bar menu'''
        self.statusBar()
        menubar = self.menuBar()
        
        '''Menu path population'''
        fileMenu = menubar.addMenu('&Path')
        fileMenu.addAction(configJsonPathAct)
        fileMenu.addAction(configHierarchyPathAct)
        fileMenu.addAction(configExcelPathAct)
        fileMenu.addAction(resetPathAct)       
        
        '''Menu Add population'''
        fileMenu = menubar.addMenu('&Edit')
        fileMenu.addAction(addHierarchyAct)
        fileMenu.addAction(addTemplateAct)
        
        '''Menu Refresh population'''
        fileMenu = menubar.addMenu('&Refresh')
        fileMenu.addAction(refreshAct)

    '''Menu Functions'''
    def addTemplate(self):
        self.dialog = AddJsonTemplateInterface()
        self.dialog.show()
        
    def addHierarchy(self):
        self.dialog = AddHierarchyInterface()
        self.dialog.show()
        
    def changePathHierarchy(self):
        self.dialog = ChangePathHierarchyInterface()
        self.dialog.show()
        
    def changePathExcel(self):
        self.dialog = ChangePathExcelInterface()
        self.dialog.show()
        
    def changePathJsonFile(self):
        self.dialog = ChangePathJsonFileInterface()
        self.dialog.show()    
        
    def refreshWindow(self):
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
        

    '''Button Function'''
    def on_pushButton_clicked(self):
        JaSONx.setConstantData(self.user_name_text.text(), 
                               self.password_text.text(), 
                               self.match_group_value_text.text(), 
                               self.combo_box_hierarchy.currentText(), 
                               )
        dialog = ViewInterface(self)
        self.hide()
        dialog.show()

'''______________________________________________________________________________________________________________________________'''

'''Add Template Interface'''
class AddJsonTemplateInterface(QtWidgets.QWidget):
    path = ""
    def __init__(self):
        super(AddJsonTemplateInterface, self).__init__()
        
        '''Window settings'''
        self.resize(700, 400)
        self.setWindowTitle("Add new Json template")
        self.show()
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button'''
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
        configuration.add_json_template(path)
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Add Hierarchy Interface'''
class AddHierarchyInterface(QtWidgets.QWidget):
    path = ""
    def __init__(self):
        super(AddHierarchyInterface, self).__init__()
        self.resize(700, 400)
        self.setWindowTitle("Add new Hierarchy")
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
   
    '''Tree clicked fucntion'''     
    def on_select(self, index):
        global path
        path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        configuration.add_file_hierarchy(path)
        self.close()
        
'''______________________________________________________________________________________________________________________________'''

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
        configuration.change_hierarchy_path(path)
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
        configuration.change_excel_path(path)
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
        configuration.change_json_path(path)
        self.close()
     
'''Main function'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainInterface()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
       script = os.path.abspath(sys.argv[0])
       params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
       shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
       main()
