import Ui_test
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import dlib
if __name__ == '__main__':
  app = QApplication(sys.argv)
  mainWindow = QDialog()
  ui = Ui_test.Ui_Dialog()
  ui.setupUi(mainWindow)
  mainWindow.show()
  sys.exit(app.exec_()) 