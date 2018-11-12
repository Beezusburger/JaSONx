'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import os
import utility
import configuration
import ActThingMainInterface
import ExcelAppend


'''Add Template Interface'''
class AddJsonTemplateInterface(QtWidgets.QWidget):
    def __init__(self):
        super(AddJsonTemplateInterface, self).__init__()    

        self.path = ""

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
        self.treeView.header().resizeSection(0, 300)
        self.treeView.setAnimated(True)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
     
    '''Tree clicked function'''
    def on_select(self, index):
        self.path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add JSON Template in json_file directory?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.addJsonTemplate(self.path)
            if(response == True):
                msgBox.about(self, "Add template json", "Template added!") 
            else: 
                msgBox.critical(self, "Add template json", "Error!")
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Add Hierarchy Interface'''
class AddHierarchyInterface(QtWidgets.QWidget):
    
    def __init__(self):
        super(AddHierarchyInterface, self).__init__()

        self.path = ""

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
        self.treeView.header().resizeSection(0, 300)
        self.treeView.setAnimated(True)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
   
    '''Tree clicked fucntion'''     
    def on_select(self, index):
        self.path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add XML Hierarchy in hierarchy directory?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_file_hierarchy(self.path)
            if(response == True):
                msgBox.about(self, "Add hierarchy xml", "File added!") 
            else:
                msgBox.critical(self, "Add hierarchy xml", "Error!")              
        self.close()

'''Change Excel path Interface'''
class AddEnvironmentPrefixInterface(QtWidgets.QMainWindow):
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
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add environment prefix?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_environment_prefix(self.environment_prefix_text.text())
            if(response == True):
                msgBox.about(self, "JaSONx", "Environment prefix added!")            
        self.close()


'''______________________________________________________________________________________________________________________________'''
     
'''Change Excel path Interface'''
class AddGatewayIdInterface(QtWidgets.QMainWindow):
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
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add gateway id?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_gateway_id(self.gateway_id_text.text())
            if(response == True):
                msgBox.about(self, "JaSONx", "Gateway id added!")            
        self.close()
        
     
'''______________________________________________________________________________________________________________________________'''

'''Open ActThing Interface'''
class ActThingToolbarInterface(QtWidgets.QWidget):
    def __init__(self, obj):
        super(ActThingToolbarInterface, self).__init__()

        self.obj = obj

        self.path = ""

        self.resize(700, 400)
        self.setWindowTitle("Select json folder")
        self.show()      
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Select")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''TreeView'''
        self.treeView = QtWidgets.QTreeView()
        
        '''File System'''
        self.fileSystemModel = QtWidgets.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel.setRootPath(os.path.realpath(''))
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.header().resizeSection(0, 300)
        self.treeView.setAnimated(True)
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.treeView)
        vbox.addWidget(self.button)
         
        '''Tree and Button clicked'''
        self.treeView.clicked.connect(self.on_select)
        self.button.clicked.connect(self.on_button_clicked)
   
    '''Tree clicked fucntion'''     
    def on_select(self, index):
        self.path = self.sender().model().filePath(index)
   
    '''Button clicked function'''
    def on_button_clicked(self):
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Select json files in this folder?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = utility.createFileList(self.path, ".json")
            dialog = ActThingMainInterface.ActThingMainInterface(response, self.obj)  
            dialog.show()           
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Change measures set'''
class ChangeMeasuresSetInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ChangeMeasuresSetInterface, self).__init__(parent)
        self.resize(700, 400)
        self.setWindowTitle("Change measures set")
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Save")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)       

        self.dict_measures_id = utility.readJsonFile(os.path.join(os.path.realpath(''), "configuration", "trendIdConfiguration.json"))

        self.lista = []
        for measure_id in self.dict_measures_id.keys():
            self.lista.append(QtWidgets.QCheckBox(measure_id, self)) 
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox_check = QtWidgets.QVBoxLayout()

        for check_box in self.lista:
            if(self.dict_measures_id[check_box.text()]["active"] == True):
                vbox_check.addWidget(check_box)
                check_box.setChecked(True)
            else:
                vbox_check.addWidget(check_box)
                check_box.setChecked(False)      
        
        widget = QtWidgets.QWidget()
        widget.setLayout(vbox_check)
        widget.setStyleSheet("width:500")
        widget.adjustSize()

        '''Scroll'''
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(widget)
        
        vbox.addWidget(scroll)
        vbox.addWidget(self.button)

        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        self.setCentralWidget(layout)

        self.button.clicked.connect(self.on_button_clicked)

    '''Button clicked function'''
    def on_button_clicked(self, state):
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Save changes?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            for check_box in self.lista:
                self.dict_measures_id[check_box.text()]["active"] = check_box.isChecked()  
            response = utility.saveJsonFile(os.path.join(os.path.realpath(''), "configuration", "trendIdConfiguration.json"), self.dict_measures_id)
            if(response == True):
                msgBox.about(self, "JaSONx", "Measures set saved successfully!")           
        self.close()

'''______________________________________________________________________________________________________________________________'''
     
'''Add Trend Id'''
class AddTrendIdInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AddTrendIdInterface, self).__init__(parent)
        self.resize(700, 400)
        self.setWindowTitle("Add Trend Id")
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Add")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        
        '''Label'''
        self.trend_id_label = QtWidgets.QLabel()
        self.trend_id_label.setText("Trend ID")

        self.channel_label = QtWidgets.QLabel()
        self.channel_label.setText("Channel")

        self.multipler_label = QtWidgets.QLabel()
        self.multipler_label.setText("Multipler")
        
        '''Textbox'''
        self.trend_id_text = QtWidgets.QLineEdit()
        self.channel_text = QtWidgets.QLineEdit()
        self.multipler_text = QtWidgets.QLineEdit()
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.trend_id_label)
        vbox.addWidget(self.trend_id_text)
        vbox.addWidget(self.channel_label)
        vbox.addWidget(self.channel_text)
        vbox.addWidget(self.multipler_label)
        vbox.addWidget(self.multipler_text)
        vbox.addWidget(self.button)
        
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
        self.setCentralWidget(layout)
        
        self.button.clicked.connect(self.on_button_clicked)
                
    '''Button clicked function'''
    def on_button_clicked(self):
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Add Trend ID?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = configuration.add_trend_id(self.trend_id_text.text(), self.channel_text.text(), self.multipler_text.text())
            if(response == True):
                msgBox.about(self, "JaSONx", "Trend ID added!")            
        self.close()

'''______________________________________________________________________________________________________________________________'''

'''Excel Append set'''
class ExcelAppendInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ExcelAppendInterface, self).__init__(parent)
        self.resize(700, 400)
        self.setWindowTitle("Excel Append")

        self.dict_config = utility.readJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"))
        
        '''Font settings'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)

        '''Label'''
        self.file_name_label = QtWidgets.QLabel()
        self.file_name_label.setText("Inserisci nome file")

        '''Textbox'''
        self.file_name_text = QtWidgets.QLineEdit()
        
        '''Button settings'''
        self.button = QtWidgets.QPushButton("Append")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)       

        self.list_file = utility.createFileList(self.dict_config["excel_files_path"], ".xlsx")

        self.list_check = []
        for file_name in self.list_file:
            self.list_check.append(QtWidgets.QCheckBox(file_name, self)) 
        
        '''Vertical layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox_check = QtWidgets.QVBoxLayout()

        for check_box in self.list_check:
            vbox_check.addWidget(check_box)
    
        widget = QtWidgets.QWidget()
        widget.setLayout(vbox_check)
        widget.setStyleSheet("width:500")
        widget.adjustSize()

        '''Scroll'''
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(widget)
        
        vbox.addWidget(scroll)
        vbox.addWidget(self.file_name_label)
        vbox.addWidget(self.file_name_text)
        vbox.addWidget(self.button)

        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        self.setCentralWidget(layout)

        self.button.clicked.connect(self.on_button_clicked)

    '''Button clicked function'''
    def on_button_clicked(self, state):   
        msgBox = QtWidgets.QMessageBox()
        buttonReply = msgBox.question(self, 'JaSONx', "Append Excel files?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            response = ExcelAppend.createExcel(self.dict_config, self.list_check, self.file_name_text.text()) 
            if(response == True):
                msgBox.about(self, "JaSONx", "File Excel created successfully!")           
        self.close()