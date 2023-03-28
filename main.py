#########################################################
# Author: Yunus Emre ISIKDEMIR
#
# Date: 11.10.2020
# 
# Description: Image process application driver code
#########################################################

from ImageProcessor import ImageProcess
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ImageProcess()
    window.show()
    sys.exit(app.exec_())
    
main()