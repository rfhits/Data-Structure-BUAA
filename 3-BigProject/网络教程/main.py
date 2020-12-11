from PyQt5 import QtWidgets
from srs import Ui_SRS

class mywindow(QtWidgets.QWidget, Ui_SRS):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())