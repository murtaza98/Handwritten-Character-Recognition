import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class recognise(QWidget):
   def __init__(self, parent = None):
      super(recognise, self).__init__(parent)
      
      layout = QVBoxLayout()
      self.btn_img = QPushButton("Select Image")
      self.btn_img.clicked.connect(self.getfile)
      layout.addWidget(self.btn_img)
      
      self.img = QLabel("No Image selected")
      layout.addWidget(self.img)
      
      self.rec = QPushButton("Recognise")
      self.rec.clicked.connect(self.recognise)
      layout.addWidget(self.rec)
      
      self.result = QLabel()
      layout.addWidget(self.result)
      
      self.setLayout(layout)
      self.setWindowTitle("Handwritten Image Recognition")
      
      self.setGeometry(10,10,512,512)

   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif *.png)")
      pixmap = QPixmap(fname)
      self.img.setPixmap(pixmap)
      self.img.setGeometry(10,10,64,64)
      
   def recognise(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      dlg.setFilter("Text files (*.txt)")
      filenames = QStringList()
      
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')

         with f:
            data = f.read()
            self.contents.setText(data)
            
def main():
   app = QApplication(sys.argv)
   ex = recognise()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()      