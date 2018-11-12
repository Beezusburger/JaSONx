'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "2.1"
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
import subprocess

'''Main actTHING Interface'''
class ACThingMainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ACThingMainInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setWindowTitle("actTHING")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\acthing.png'))

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
        
        '''Create list file .json'''
        self.list_file_json = utility.createListFile(os.path.join(JaSONx.jsonPath,JaSONx.name_file_hierarchy), ".json")
        
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
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
    
'''______________________________________________________________________________________________________________________________'''

'''Create xCELL Interface'''
class xCellCreateInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(xCellCreateInterface, self).__init__(parent)
      
        '''Window settings'''
        self.setFixedSize(1050,600)
        self.setWindowTitle("xCELL")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\xcell.png'))
        
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
        self.image_label.setPixmap(QtGui.QPixmap('image\\xcell.png'))
        
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
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
        
'''______________________________________________________________________________________________________________________________'''

'''MAIN xCELL Interface'''
class XCellMainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(XCellMainInterface, self).__init__(parent)
        
        '''Window settings'''
        self.setWindowTitle("xCELL")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\xcell.png'))

        
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
        xCELL.setConstantData(self.site_name_text.text(),
                              JaSONx.name_file_hierarchy
                              )
        dialog = xCellCreateInterface(self)
        self.hide()
        dialog.show()
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = MainInterface(self)
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
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
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
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
        
    '''Button excel function'''
    def create_excel(self):
        dialog = XCellMainInterface(self)
        dialog.show()
    
    '''Button activate thing function'''
    def activate_thing(self):
        dialog = ACThingMainInterface(self)
        dialog.show()
        
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = MainInterface(self)
        self.hide()
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
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
        
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
        for meter, model in self.dictmeters.items():
            self.table.setItem(count,0,QtWidgets.QTableWidgetItem(meter))
            self.table.setItem(count,1,QtWidgets.QTableWidgetItem(model))  
            count +=1
 
        '''Button clicked'''       
        self.button.clicked.connect(self.on_pushButton_clicked)
    
    '''Toolbar Function'''
    def returnFirstInterface(self):
        dialog = MainInterface(self)
        self.hide()
        dialog.show()
    
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
        self.setWindowTitle("JaSONx - version 2.2")
        self.setFixedSize(1050,600) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
       
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        fontToolbar = QtGui.QFont()
        fontToolbar.setPointSize(10)
        self.setFont(font)
        
        '''Label settings'''
        self.title_label = QtWidgets.QLabel()
        self.user_name_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.match_group_value_label = QtWidgets.QLabel()
        self.combo_box_hierarchy_label = QtWidgets.QLabel()
        self.gateway_id_label = QtWidgets.QLabel()
        self.combo_box_environment_prefix_label = QtWidgets.QLabel()
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        '''Label text'''
        self.title_label.setPixmap(QtGui.QPixmap('image\\title.png'))
        self.user_name_label.setText("Username: ")
        self.password_label.setText("Password: ")
        self.combo_box_hierarchy_label.setText("Hierarchy: ")
        self.gateway_id_label.setText("Gateway id: ") 
        self.combo_box_environment_prefix_label.setText("Environment prefix: ")
        
        '''Textbox settings'''
        self.user_name_text = QtWidgets.QLineEdit(self)
        self.password_text = QtWidgets.QLineEdit(self) 

        
        '''Combobox settings'''
        self.combo_box_hierarchy = QtWidgets.QComboBox()
        self.combo_box_hierarchy.addItems(utility.getListHierarchy())
        
        self.combo_box_environment_prefix = QtWidgets.QComboBox()
        self.combo_box_environment_prefix.addItems(utility.readFileJSON(os.path.join(os.path.realpath (''), "configuration\\environmentPrefixConfiguration.json")))
    
        self.combo_box_gateway_id = QtWidgets.QComboBox()
        self.combo_box_gateway_id.addItems(utility.readFileJSON(os.path.join(os.path.realpath (''), "configuration\\gatewayIdConfiguration.json")))
    
    
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
        grid.addWidget(self.gateway_id_label, 2, 0)
        grid.addWidget(self.combo_box_gateway_id, 2, 1)
        grid.addWidget(self.combo_box_environment_prefix_label, 3, 0)
        grid.addWidget(self.combo_box_environment_prefix, 3, 1)
        grid.addWidget(self.combo_box_hierarchy_label, 4, 0)
        grid.addWidget(self.combo_box_hierarchy, 4, 1)
        
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
        
        '''TOOLBAR'''
        toolbar = self.addToolBar('Toolbar')
        toolbar.setMovable(False)
        toolbar.setIconSize(QtCore.QSize(40,40))
        toolbar.setFont(fontToolbar)
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        '''Icon toolbar'''
        '''Exit application'''
        exit_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","exiticon.png")), 'Close', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Close application')
        
        '''Add Hierarchy xml'''
        add_xml_hierarchy_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","xmlicon.png")), 'Add Hierarchy', self)
        add_xml_hierarchy_act.setShortcut('Ctrl+H')
        add_xml_hierarchy_act.setStatusTip('Add Hierarchy XML')
        
        '''Add template json'''
        add_json_template_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","jsonicon.png")), 'Add Template', self)
        add_json_template_act.setShortcut('Ctrl+T')
        add_json_template_act.setStatusTip('Add JSON Template')
        
        '''Refresh application'''
        refresh_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","refreshicon.png")), 'Refresh', self)
        refresh_act.setShortcut('Ctrl+R')
        refresh_act.setStatusTip('Refresh application')
        
        '''Add evironment prefix'''
        add_environment_prefix_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","addlisticon.png")), 'Add environment prefix', self)
        add_environment_prefix_act.setShortcut('Ctrl+P')
        add_environment_prefix_act.setStatusTip('Add environment prefix')
        
        '''Add gateway id'''
        add_gateway_id_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "icon","addlisticon.png")), 'Add gateway id', self)
        add_gateway_id_act.setShortcut('Ctrl+Y')
        add_gateway_id_act.setStatusTip('Add gateway id')
        
        
        '''xCELL'''
        xCell_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "xcell.png")), 'xCell', self)
        xCell_act.setShortcut('Ctrl+L')
        xCell_act.setStatusTip('Open xCELL Interface')
        
        '''acThing'''
        acThing_act = QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.realpath(''), "image", "acthing.png")), 'acThing', self)
        acThing_act.setShortcut('Ctrl+I')
        acThing_act.setStatusTip('Open acThing Interface')
        
        '''ACTION TOOLBAR'''
        toolbar.addAction(exit_act)
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addAction(add_xml_hierarchy_act)  
        toolbar.addAction(add_json_template_act)
        toolbar.addAction(add_environment_prefix_act)
        toolbar.addAction(add_gateway_id_act)
        toolbar.addAction(refresh_act)
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addAction(xCell_act)
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addAction(acThing_act)
        
        
        '''TOOOLBAR TRIGGERED'''
        exit_act.triggered.connect(self.closeFunction)
        add_xml_hierarchy_act.triggered.connect(self.addHierarchy)
        add_json_template_act.triggered.connect(self.addJsonTemplate)
        refresh_act.triggered.connect(self.refreshWindow)
        add_environment_prefix_act.triggered.connect(self.addEnvironmentPrefix)
        add_gateway_id_act.triggered.connect(self.addGatewayId)
        xCell_act.triggered.connect(self.openXcellInterface) 
        acThing_act.triggered.connect(self.openAcThingInterface)
        
        
        '''MENU SETTINGS'''
        '''Configuration Json path'''
        configJsonPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Json Path Configuration', self)        
        configJsonPathAct.setShortcut('Ctrl+J')
        configJsonPathAct.setStatusTip('')
        configJsonPathAct.triggered.connect(self.changePathJsonFile)

        '''Configuration Hierarchy path'''
        configHierarchyPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Hierarchy Path Configuration', self)        
        configHierarchyPathAct.setShortcut('Ctrl+X')
        configHierarchyPathAct.setStatusTip('')
        configHierarchyPathAct.triggered.connect(self.changePathHierarchy)
        
        '''Configuration Excel path'''
        configExcelPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Excel Path Configuration', self)        
        configExcelPathAct.setShortcut('Ctrl+E')
        configExcelPathAct.setStatusTip('')
        configExcelPathAct.triggered.connect(self.changePathExcel)
        
        '''Reset paths default'''
        resetPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Reset Path to Default', self)        
        resetPathAct.setShortcut('Ctrl+D')
        resetPathAct.setStatusTip('')
        resetPathAct.triggered.connect(self.resetDefaultPath)
        
        '''Refresh template configuration'''
        refreshTemplateConfigAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Refresh template configuration', self)        
        refreshTemplateConfigAct.setShortcut('Ctrl+C')
        refreshTemplateConfigAct.setStatusTip('')
        refreshTemplateConfigAct.triggered.connect(self.refreshTemplateConfiguration)
        
        '''User Guide'''
        UserGuideAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Open User Guide', self)        
        UserGuideAct.setShortcut('Ctrl+G')
        UserGuideAct.setStatusTip('')
        UserGuideAct.triggered.connect(self.openUserGuide)

        '''Add bar menu'''
        menubar = self.menuBar()
        
        '''Menu path population'''
        fileMenu = menubar.addMenu('&Change Path')
        fileMenu.addAction(configJsonPathAct)
        fileMenu.addAction(configHierarchyPathAct)
        fileMenu.addAction(configExcelPathAct)
        fileMenu.addAction(resetPathAct) 
        
        '''Menu template configuration'''
        fileMenu2 = menubar.addMenu('&Refresh Template Configuration')
        fileMenu2.addAction(refreshTemplateConfigAct)
        
        '''Menu Info - User Guide'''
        fileMenu3 = menubar.addMenu('&Info')
        fileMenu3.addAction(UserGuideAct)

    '''Toolbar Functions'''
    def closeFunction(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Close application?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:      
            self.close()
        
    def addJsonTemplate(self):
        self.dialog = AddJsonTemplateInterface()
        self.dialog.show()
            
    def addHierarchy(self):
        self.dialog = AddHierarchyInterface()
        self.dialog.show()
            
    def refreshWindow(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Refresh application?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:            
            dialog = MainInterface(self)
            self.hide()
            dialog.show()
    
    def openXcellInterface(self):
        self.dialog = XCellMainInterface()
        self.hide()
        self.dialog.show()
        
    def openAcThingInterface(self):
        self.dialog = ACThingMainInterface()
        self.hide()
        self.dialog.show()
    
    '''Menu Functions'''
    def changePathHierarchy(self):
        self.dialog = ChangePathHierarchyInterface()
        self.dialog.show()
            
    def changePathExcel(self):
        self.dialog = ChangePathExcelInterface()
        self.dialog.show()
            
    def changePathJsonFile(self):
        self.dialog = ChangePathJsonFileInterface()
        self.dialog.show()  
        
    def resetDefaultPath(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Reset default path?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:   
            configuration.reset_path()
            
    def refreshTemplateConfiguration(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Refresh template configuration?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:   
            utility.refreshTemplateConfiguration() 
            
    def addEnvironmentPrefix(self):
        dialog = AddEnvironmentPrefixInterface(self)
        dialog.show()
        
    def addGatewayId(self):
        dialog = AddGatewayIdInterface(self)
        dialog.show()
        
    def openUserGuide(self):
        subprocess.Popen(os.path.join(os.path.realpath(''), "User Guide.pdf"),shell=True)
        
            
    '''Button Function'''
    def on_pushButton_clicked(self):
        JaSONx.setConstantData(self.user_name_text.text(), 
                               self.password_text.text(),                
                               self.combo_box_hierarchy.currentText(), 
                               self.combo_box_gateway_id.currentText(),
                               self.combo_box_environment_prefix.currentText()
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
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add JSON Template in json_file directory?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_json_template(path)
            if(response == True):
                msgBox.about(self, "Add template json", "Template added!") 
            else: 
                msgBox.critical(self, "Add template json", "Error!")
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
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add XML Hierarchy in hierarchy directory?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_file_hierarchy(path)
            if(response == True):
                msgBox.about(self, "Add hierarchy xml", "File added!") 
            else:
                msgBox.critical(self, "Add hierarchy xml", "Error!")              
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
   
'''______________________________________________________________________________________________________________________________'''
     
'''Change Excel path Interface'''
class AddEnvironmentPrefixInterface(QtWidgets.QMainWindow):
    path = ""
    
    def __init__(self, parent=None):
        super(AddEnvironmentPrefixInterface, self).__init__(parent)
        self.resize(700, 400)
        self.setWindowTitle("Add evironment prefix")
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Add")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        
        '''Label'''
        self.environment_prefix_label = QtWidgets.QLabel()
        self.environment_prefix_label.setText("Environment prefix")
        
        '''Textbox'''
        self.environment_prefix_text = QtWidgets.QLineEdit()
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.environment_prefix_label)
        vbox.addWidget(self.environment_prefix_text)
        vbox.addWidget(self.button)
        
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
        self.setCentralWidget(layout)
        
        self.button.clicked.connect(self.on_button_clicked)
        
                
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add environment prefix?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_environment_prefix(self.environment_prefix_text.text())
            if(response == True):
                msgBox.about(self, "JaSONx", "Environment prefix added!")            
        self.close()
        
     
'''______________________________________________________________________________________________________________________________'''

'''______________________________________________________________________________________________________________________________'''
     
'''Change Excel path Interface'''
class AddGatewayIdInterface(QtWidgets.QMainWindow):
    path = ""
    
    def __init__(self, parent=None):
        super(AddGatewayIdInterface, self).__init__(parent)
        self.resize(700, 400)
        self.setWindowTitle("Add gateway id")
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Add")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        
        '''Label'''
        self.gateway_id_label = QtWidgets.QLabel()
        self.gateway_id_label.setText("Gateway id")
        
        '''Textbox'''
        self.gateway_id_text = QtWidgets.QLineEdit()
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.gateway_id_label)
        vbox.addWidget(self.gateway_id_text)
        vbox.addWidget(self.button)
        
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
        self.setCentralWidget(layout)
        
        self.button.clicked.connect(self.on_button_clicked)
        
                
    '''Button clicked function'''
    def on_button_clicked(self):
        global path
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add gateway id?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_gateway_id(self.gateway_id_text.text())
            if(response == True):
                msgBox.about(self, "JaSONx", "Gateway id added!")            
        self.close()
        
     
'''______________________________________________________________________________________________________________________________'''
        
     
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
