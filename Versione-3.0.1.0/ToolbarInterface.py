'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui
import os
import utility
import configuration
import ActThingMainInterface


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