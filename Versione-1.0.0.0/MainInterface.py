'''
@author = "Jury Francia, Simone Olivieri"
@version = "1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it"
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import JaSONx
import os

'''CREATE JSON FILES'''
class CreateInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CreateInterface, self).__init__(parent)
        
        '''window'''
        self.setFixedSize(1050,400)
        self.setWindowTitle("JaSONx - v 1.0")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
        
        '''Font'''
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setFont(font)
        
        '''Label'''
        self.label = QtWidgets.QLabel()
        self.image_label = QtWidgets.QLabel()
        self.label.setText("Files JSON created!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap('image\\logo.png'))
        
        '''Button'''
        self.button = QtWidgets.QPushButton("Close")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
        
        '''Vertical Layout'''
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.label)
        
        vbox.addWidget(self.button)
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        self.setCentralWidget(layout)
    
    '''Button function'''
    def on_pushButton_clicked(self):
        exit()
        
'''VIEW METERS DETAILS'''
class ViewInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ViewInterface, self).__init__(parent)
        
        '''Window'''
        self.setFixedSize(1050,400)
        self.setWindowTitle("JaSONx - v 1.0")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))
        
        '''Dict -> {meter_name : {meter_model:val , n_measures_sel:val}}'''
        dictmeters = JaSONx.createDictMeters()
        
        '''Font'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Button'''
        self.button = QtWidgets.QPushButton("Generate JSON")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
                
        '''Layout'''
        grid = QtWidgets.QGridLayout()   
        self.table = QtWidgets.QTableWidget()   
        self.table.setFont(font)               
        self.table.setRowCount(len(dictmeters))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Meter Name', 'Model', 'Measures'])
        self.table.setColumnWidth(0,430)
        self.table.setColumnWidth(1,325)
        self.table.setColumnWidth(2,200)

        grid.addWidget(self.table, 0, 0)
        grid.addWidget(self.button, 1, 0)
        layout = QtWidgets.QWidget()
        layout.setLayout(grid)
        self.setCentralWidget(layout)
   
  
        '''Table settings'''
        count = 0
        for key in dictmeters:
            self.table.setItem(count,0,QtWidgets.QTableWidgetItem(key))
            self.table.setItem(count,1,QtWidgets.QTableWidgetItem(dictmeters[key]["meter_model"]))
            self.table.setItem(count,2,QtWidgets.QTableWidgetItem(str(dictmeters[key]["n_measures_sel"])))
            count +=1
      
    '''Button function'''    
    def on_pushButton_clicked(self):
        JaSONx.startCreateJSON()
        dialog = CreateInterface(self)
        self.hide()
        dialog.show()
             
'''MAIN'''
class MainInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainInterface, self).__init__(parent)
        
        '''Window'''
        self.setWindowTitle("JaSONx - v 1.0")
        self.setFixedSize(1050,450) 
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'image\\logo.png'))

        
        '''Font'''
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        
        '''Label'''
        self.title_label = QtWidgets.QLabel()
        self.user_name_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.match_group_value_label = QtWidgets.QLabel()
        self.combo_box_hierarchy_label = QtWidgets.QLabel()
        self.combo_box_prefix_mgvalue_label = QtWidgets.QLabel()
        
        '''Testo Label'''
        self.title_label.setPixmap(QtGui.QPixmap('image\\title.png'))
        self.user_name_label.setText("Username: ")
        self.password_label.setText("Password: ")
        self.match_group_value_label.setText("Match group value: ")
        self.combo_box_hierarchy_label.setText("Hierarchy: ")
        self.combo_box_prefix_mgvalue_label.setText("Prefix mgvalue: ")
        
        '''Textbox'''
        self.user_name_text = QtWidgets.QLineEdit(self)
        self.password_text = QtWidgets.QLineEdit(self)
        self.match_group_value_text = QtWidgets.QLineEdit(self)  
        
        '''Combobox'''
        self.combo_box_hierarchy = QtWidgets.QComboBox()
        self.combo_box_hierarchy.addItems(JaSONx.getListHierarchy())

        self.combo_box_prefix_mgvalue = QtWidgets.QComboBox()
        self.combo_box_prefix_mgvalue.addItems(JaSONx.getListPrefix_mgvalue())
    
        '''Button'''
        self.button = QtWidgets.QPushButton("Send data")
        self.button.setStyleSheet("background-color: #8b0000; color: white; height:50; border-radius:10")
        self.button.setFont(font)
        self.button.clicked.connect(self.on_pushButton_clicked)
    
        '''Layout'''
        vbox = QtWidgets.QVBoxLayout()
        
        grid = QtWidgets.QGridLayout()  
        grid.addWidget(self.user_name_label, 0, 0)
        grid.addWidget(self.user_name_text, 0, 1)  
        grid.addWidget(self.password_label, 1, 0)
        grid.addWidget(self.password_text, 1, 1)
        grid.addWidget(self.match_group_value_label, 2, 0)
        grid.addWidget(self.match_group_value_text, 2, 1)
        grid.addWidget(self.combo_box_hierarchy_label, 3, 0)
        grid.addWidget(self.combo_box_hierarchy, 3, 1)
        grid.addWidget(self.combo_box_prefix_mgvalue_label, 4, 0)
        grid.addWidget(self.combo_box_prefix_mgvalue, 4, 1) 
        grid.addWidget(self.button, 5, 1)
        
        vbox.addWidget(self.title_label)
        vbox.addLayout(grid)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        layout = QtWidgets.QWidget()
        layout.setLayout(vbox)
        
        self.setCentralWidget(layout)
    
    '''Button function'''    
    def on_pushButton_clicked(self):
        JaSONx.setConstantData(self.user_name_text.text(), 
                               self.password_text.text(), 
                               self.match_group_value_text.text(), 
                               self.combo_box_hierarchy.currentText(), 
                               self.combo_box_prefix_mgvalue.currentText()
                               )
        dialog = ViewInterface(self)
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