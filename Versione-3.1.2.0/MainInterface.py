'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import JaSONx
import os
import utility
import configuration
import webbrowser
import ViewInterface
import ToolbarInterface
import MenuInterface
import XCellMainInterface

'''Main Json Interface'''
class MainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainInterface, self).__init__(parent)
        
        '''Configuration path'''
        dict_configuration_path = utility.getConfigurationPath()
        self.json_templates_path = dict_configuration_path["json_templates_path"]
        self.excel_templates_path = dict_configuration_path["excel_templates_path"]
        self.json_files_path = dict_configuration_path["json_files_path"]
        self.excel_files_path = dict_configuration_path["excel_files_path"]
        self.hierarchy_path = dict_configuration_path["hierarchy_path"]
        
        '''Window settings'''
        self.setWindowTitle("JaSONx - version 3.1.2.0")
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
        self.user_name_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.match_group_value_label = QtWidgets.QLabel()
        self.combo_box_hierarchy_label = QtWidgets.QLabel()
        self.gateway_id_label = QtWidgets.QLabel()
        self.combo_box_environment_prefix_label = QtWidgets.QLabel()
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        '''Label text'''
        self.title_label.setPixmap(QtGui.QPixmap(os.path.join(os.path.realpath(''), "image", "title.png")))
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
        self.combo_box_hierarchy.addItems(utility.createFileList(self.hierarchy_path, ".xml"))
        
        self.combo_box_environment_prefix = QtWidgets.QComboBox()
        self.combo_box_environment_prefix.addItems(utility.readJsonFile(os.path.join(os.path.realpath (''), "configuration", "environmentPrefixConfiguration.json")))
    
        self.combo_box_gateway_id = QtWidgets.QComboBox()
        self.combo_box_gateway_id.addItems(utility.readJsonFile(os.path.join(os.path.realpath (''), "configuration", "gatewayIdConfiguration.json")))
    
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
        toolbar.addAction(acThing_act)
        
        '''TOOOLBAR TRIGGERED'''
        exit_act.triggered.connect(self.closeFunction)
        add_xml_hierarchy_act.triggered.connect(self.addHierarchy)
        add_json_template_act.triggered.connect(self.addJsonTemplate)
        refresh_act.triggered.connect(self.refreshWindow)
        add_environment_prefix_act.triggered.connect(self.addEnvironmentPrefix)
        add_gateway_id_act.triggered.connect(self.addGatewayId)
        acThing_act.triggered.connect(self.openActThingInterface)
        
        '''MENU SETTINGS'''
        '''Configuration Json path'''
        configJsonPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Json output', self)        
        configJsonPathAct.setShortcut('Ctrl+J')
        configJsonPathAct.setStatusTip('')
        configJsonPathAct.triggered.connect(self.changePathJsonFile)

        '''Configuration Hierarchy path'''
        configHierarchyPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Hierarchy', self)        
        configHierarchyPathAct.setShortcut('Ctrl+X')
        configHierarchyPathAct.setStatusTip('')
        configHierarchyPathAct.triggered.connect(self.changePathHierarchy)

        '''Configuration Template path'''
        configTemplatePathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Template', self)        
        configTemplatePathAct.setShortcut('Ctrl+L')
        configTemplatePathAct.setStatusTip('')
        configTemplatePathAct.triggered.connect(self.changePathTemplate)
        
        '''Configuration Excel path'''
        configExcelPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Excel output', self)        
        configExcelPathAct.setShortcut('Ctrl+E')
        configExcelPathAct.setStatusTip('')
        configExcelPathAct.triggered.connect(self.changePathExcel)
        
        '''Reset paths default'''
        resetPathAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Reset Path to Default', self)        
        resetPathAct.setShortcut('Ctrl+D')
        resetPathAct.setStatusTip('')
        resetPathAct.triggered.connect(self.resetDefaultPath)
        
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
        fileMenu.addAction(configTemplatePathAct)
        fileMenu.addAction(configExcelPathAct)
        fileMenu.addAction(resetPathAct) 
        
        '''Menu Info - User Guide'''
        fileMenu2 = menubar.addMenu('&Info')
        fileMenu2.addAction(UserGuideAct)

    '''Toolbar Functions'''
    def closeFunction(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Close application?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:      
            self.close()
        
    def addJsonTemplate(self):
        self.dialog = ToolbarInterface.AddJsonTemplateInterface()
        self.dialog.show()
            
    def addHierarchy(self):
        self.dialog = ToolbarInterface.AddHierarchyInterface()
        self.dialog.show()
            
    def refreshWindow(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Refresh application?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:            
            dialog = MainInterface(self)
            self.hide()
            utility.refreshTemplateConfiguration()
            dialog.show()
        
    def openActThingInterface(self):
        self.dialog = ToolbarInterface.ActThingToolbarInterface(self)
        self.dialog.show()
    
    '''Menu Functions'''
    def changePathHierarchy(self):
        self.dialog = MenuInterface.ChangePathHierarchyInterface()
        self.dialog.show()

    def changePathTemplate(self):
        self.dialog = MenuInterface.ChangePathTemplateInterface()
        self.dialog.show()
            
    def changePathExcel(self):
        self.dialog = MenuInterface.ChangePathExcelInterface()
        self.dialog.show()
            
    def changePathJsonFile(self):
        self.dialog = MenuInterface.ChangePathJsonFileInterface()
        self.dialog.show()  
        
    def resetDefaultPath(self):
        buttonReply = QtWidgets.QMessageBox.question(self, 'JaSONx', "Reset default path?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No,  QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:   
            configuration.reset_path()
            
    def addEnvironmentPrefix(self):
        dialog = ToolbarInterface.AddEnvironmentPrefixInterface(self)
        dialog.show()
        
    def addGatewayId(self):
        dialog = ToolbarInterface.AddGatewayIdInterface(self)
        dialog.show()
        
    def openUserGuide(self):
        webbrowser.open_new(os.path.join(os.path.realpath(''), "User Guide.pdf"))      
            
    '''Button Function'''
    def on_pushButton_clicked(self):
        obj = JaSONx.Jasonx(self.user_name_text.text(), 
                               self.password_text.text(),                
                               self.combo_box_hierarchy.currentText(), 
                               self.combo_box_gateway_id.currentText(),
                               self.combo_box_environment_prefix.currentText()
                               )
        dialog = ViewInterface.ViewInterface(obj, self)
        self.hide()
        dialog.show()   

'''Main function'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainInterface()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()