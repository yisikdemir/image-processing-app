################################################################################
# Author: Yunus Emre ISIKDEMIR
#
# Date: 11.10.2020
# 
# Description: Auto-generated image processing application layout by Qt designer
################################################################################

# GUI utility libraries
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Layout(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 600)
        MainWindow.setFixedSize(861, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 781, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source_groupbox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.source_groupbox_2.setObjectName("source_groupbox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.source_groupbox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 151, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_folder_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.open_folder_button.setStyleSheet("border: false;")
        self.open_folder_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_folder_button.setIcon(icon)
        self.open_folder_button.setObjectName("open_folder_button")
        self.horizontalLayout_2.addWidget(self.open_folder_button)
        self.clear_screen_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clear_screen_button.setStyleSheet("border: false;")
        self.clear_screen_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/clear_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_screen_button.setIcon(icon1)
        self.clear_screen_button.setIconSize(QtCore.QSize(18, 25))
        self.clear_screen_button.setObjectName("clear_screen_button")
        self.horizontalLayout_2.addWidget(self.clear_screen_button)
        self.horizontalLayout.addWidget(self.source_groupbox_2)
        self.output_groupbox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.output_groupbox_2.setObjectName("output_groupbox_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.output_groupbox_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 151, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 7, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.save_button.setStyleSheet("border: false;")
        self.save_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save_icon_colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setObjectName("save_button")
        self.save_button.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.save_button)
        self.save_as_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.save_as_button.setStyleSheet("border: false;")
        self.save_as_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/save_as_colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_as_button.setIcon(icon3)
        self.save_as_button.setIconSize(QtCore.QSize(25, 16))
        self.save_as_button.setObjectName("save_as_button")
        self.save_as_button.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.save_as_button)
        self.undo_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.undo_button.setStyleSheet("border: false;")
        self.undo_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_button.setIcon(icon4)
        self.undo_button.setObjectName("undo_button")
        self.undo_button.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.undo_button)
        self.redo_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.redo_button.setStyleSheet("border: false;")
        self.redo_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo_button.setIcon(icon5)
        self.redo_button.setObjectName("redo_button")
        self.redo_button.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.redo_button)
        self.horizontalLayout.addWidget(self.output_groupbox_2)
        self.conversion_groupbox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.conversion_groupbox_2.setObjectName("conversion_groupbox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.conversion_groupbox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 131, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rgb_to_gray_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rgb_to_gray_button.setStyleSheet("background-color:rgba(201, 220, 229, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;\n"
"\n"
"")
        self.rgb_to_gray_button.setObjectName("rgb_to_gray_button")
        self.rgb_to_gray_button.setEnabled(False)
        self.verticalLayout_3.addWidget(self.rgb_to_gray_button)
        self.rgb_to_hsv_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rgb_to_hsv_button.setStyleSheet("background-color:rgba(201, 220, 229, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;\n"
"\n"
"")
        self.rgb_to_hsv_button.setObjectName("rgb_to_hsv_button")
        self.rgb_to_hsv_button.setEnabled(False)
        self.verticalLayout_3.addWidget(self.rgb_to_hsv_button)
        self.horizontalLayout.addWidget(self.conversion_groupbox_2)
        self.segmentation_groupbox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.segmentation_groupbox_2.setObjectName("segmentation_groupbox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.segmentation_groupbox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 64))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.otsu_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.otsu_button.setStyleSheet("background-color: rgba(171, 173, 255, 120);;\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;\n"
"\n"
"")
        self.otsu_button.setObjectName("otsu_button")
        self.otsu_button.setEnabled(False)
        self.verticalLayout_2.addWidget(self.otsu_button)
        self.chan_vese_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chan_vese_button.setStyleSheet("background-color: rgba(171, 173, 255, 120);;\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;\n"
"\n"
"")
        self.chan_vese_button.setObjectName("chan_vese_button")
        self.chan_vese_button.setEnabled(False)
        self.verticalLayout_2.addWidget(self.chan_vese_button)
        self.morphological_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.morphological_button.setStyleSheet("background-color: rgba(171, 173, 255, 120);;\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;\n"
"\n"
"")
        self.morphological_button.setObjectName("morphological_button")
        self.morphological_button.setEnabled(False)
        self.verticalLayout_2.addWidget(self.morphological_button)
        self.horizontalLayout.addWidget(self.segmentation_groupbox_2)
        self.edge_detection_groupbox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.edge_detection_groupbox_2.setObjectName("edge_detection_groupbox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.edge_detection_groupbox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 20, 131, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 7, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.roberts_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.roberts_button.setStyleSheet("background-color: rgb(165, 148, 172, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;")
        self.roberts_button.setObjectName("roberts_button")
        self.roberts_button.setEnabled(False)
        self.gridLayout.addWidget(self.roberts_button, 0, 0, 1, 1)
        self.sobel_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sobel_button.setStyleSheet("background-color: rgb(165, 148, 172, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;")
        self.sobel_button.setObjectName("sobel_button")
        self.sobel_button.setEnabled(False)
        self.gridLayout.addWidget(self.sobel_button, 0, 1, 1, 1)
        self.scharr_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.scharr_button.setStyleSheet("background-color: rgb(165, 148, 172, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;")
        self.scharr_button.setObjectName("scharr_button")
        self.scharr_button.setEnabled(False)
        self.gridLayout.addWidget(self.scharr_button, 1, 0, 1, 1)
        self.prewitt_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.prewitt_button.setStyleSheet("background-color: rgb(165, 148, 172, 120);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-radius:10px;\n"
"border-color: gray;")
        self.prewitt_button.setObjectName("prewitt_button")
        self.prewitt_button.setEnabled(False)
        self.gridLayout.addWidget(self.prewitt_button, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.edge_detection_groupbox_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 120, 781, 411))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.source_image_groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_3)
        self.source_image_groupBox.setObjectName("source_image_groupBox")
        self.img_src = QtWidgets.QLabel(self.source_image_groupBox)
        self.img_src.setGeometry(QtCore.QRect(10, 30, 351, 351))
        self.img_src.setText("")
        self.img_src.setObjectName("img_src")
        self.horizontalLayout_3.addWidget(self.source_image_groupBox)
        self.output_image_groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_3)
        self.output_image_groupBox.setObjectName("output_image_groupBox")
        self.img_output = QtWidgets.QLabel(self.output_image_groupBox)
        self.img_output.setGeometry(QtCore.QRect(20, 30, 341, 351))
        self.img_output.setText("")
        self.img_output.setObjectName("img_output")
        self.horizontalLayout_3.addWidget(self.output_image_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setEnabled(False)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")       
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Source = QtWidgets.QAction(MainWindow)
        self.actionOpen_Source.setObjectName("actionOpen_Source")
        self.actionSave_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_Output.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Output.setIcon(icon6)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionSave_as_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_as_Output.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as_Output.setIcon(icon7)
        self.actionSave_as_Output.setObjectName("actionSave_as_Output")
        self.actionEXit = QtWidgets.QAction(MainWindow)
        self.actionEXit.setEnabled(True)
        self.actionEXit.setObjectName("actionEXit")
        self.actionSource = QtWidgets.QAction(MainWindow)
        self.actionSource.setObjectName("actionSource")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionClear_Screen = QtWidgets.QAction(MainWindow)
        self.actionClear_Screen.setEnabled(False)
        self.actionClear_Screen.setObjectName("actionClear_Screen")
        self.actionUndo_Output = QtWidgets.QAction(MainWindow)
        self.actionUndo_Output.setEnabled(False)
        self.actionUndo_Output.setIcon(icon4)
        self.actionUndo_Output.setObjectName("actionUndo_Output")     
        self.actionRedo_Output = QtWidgets.QAction(MainWindow)
        self.actionRedo_Output.setEnabled(False)
        self.actionRedo_Output.setIcon(icon5)
        self.actionRedo_Output.setObjectName("actionRedo_Output")
        self.actionRGB_to_GrayScale = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_GrayScale.setEnabled(False)
        self.actionRGB_to_GrayScale.setObjectName("actionRGB_to_GrayScale")
        self.actionRGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_HSV.setEnabled(False)
        self.actionRGB_to_HSV.setObjectName("actionRGB_to_HSV")
        self.actionMulti_Otsu_Thresholding = QtWidgets.QAction(MainWindow)
        self.actionMulti_Otsu_Thresholding.setEnabled(False)
        self.actionMulti_Otsu_Thresholding.setObjectName("actionMulti_Otsu_Thresholding")
        self.actionChan_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        self.actionChan_Vese_Segmentation.setEnabled(False)
        self.actionChan_Vese_Segmentation.setObjectName("actionChan_Vese_Segmentation")
        self.actionMorphological_Snakes = QtWidgets.QAction(MainWindow)
        self.actionMorphological_Snakes.setEnabled(False)
        self.actionMorphological_Snakes.setObjectName("actionMorphological_Snakes")
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setEnabled(False)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setEnabled(False)
        self.actionSobel.setObjectName("actionSobel")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setEnabled(False)
        self.actionScharr.setObjectName("actionScharr")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setEnabled(False)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.menuExport_As.addAction(self.actionSource)
        self.menuExport_As.addAction(self.actionOutput)
        self.menuFile.addAction(self.actionOpen_Source)
        self.menuFile.addAction(self.actionSave_Output)
        self.menuFile.addAction(self.actionSave_as_Output)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addAction(self.actionEXit)
        self.menuEdit.addAction(self.actionClear_Screen)
        self.menuEdit.addAction(self.actionUndo_Output)        
        self.menuEdit.addAction(self.actionRedo_Output)
        self.menuConversion.addAction(self.actionRGB_to_GrayScale)
        self.menuConversion.addAction(self.actionRGB_to_HSV)
        self.menuSegmentation.addAction(self.actionMulti_Otsu_Thresholding)
        self.menuSegmentation.addAction(self.actionChan_Vese_Segmentation)
        self.menuSegmentation.addAction(self.actionMorphological_Snakes)
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Store the Actions in a list to ease all of them enable or disable
        self.actions_list = [self.actionSave_Output,
                             self.actionSave_as_Output,
                             self.actionSource,
                             self.actionOutput,
                             self.actionClear_Screen,
                             self.menuExport_As,
                             self.actionUndo_Output,
                             self.actionRedo_Output,
                             self.actionRGB_to_GrayScale,
                             self.actionRGB_to_HSV,
                             self.actionMulti_Otsu_Thresholding,
                             self.actionChan_Vese_Segmentation,
                             self.actionMorphological_Snakes,
                             self.actionRoberts,
                             self.actionSobel,
                             self.actionScharr,
                             self.actionPrewitt]
       
       	self.button_list = [self.save_button,
                            self.save_as_button,
                            self.undo_button,
                            self.redo_button,
                            self.rgb_to_gray_button,
                            self.rgb_to_hsv_button,
                            self.otsu_button,
                            self.chan_vese_button,
                            self.morphological_button,
                            self.roberts_button,
                            self.sobel_button,
                            self.scharr_button,
                            self.prewitt_button]
           
        self.actions_list = self.actions_list + self.button_list

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.source_groupbox_2.setStatusTip(_translate("MainWindow", "source"))
        self.source_groupbox_2.setTitle(_translate("MainWindow", "Source"))
        self.open_folder_button.setStatusTip(_translate("MainWindow", "open"))
        self.clear_screen_button.setStatusTip(_translate("MainWindow", "clear screen"))
        self.output_groupbox_2.setStatusTip(_translate("MainWindow", "output"))
        self.output_groupbox_2.setTitle(_translate("MainWindow", "Output"))
        self.save_button.setStatusTip(_translate("MainWindow", "save"))
        self.save_as_button.setStatusTip(_translate("MainWindow", "save as"))
        self.undo_button.setStatusTip(_translate("MainWindow", "undo"))
        self.redo_button.setStatusTip(_translate("MainWindow", "redo"))
        self.conversion_groupbox_2.setStatusTip(_translate("MainWindow", "conversion"))
        self.conversion_groupbox_2.setTitle(_translate("MainWindow", "Conversion"))
        self.rgb_to_gray_button.setStatusTip(_translate("MainWindow", "RGB to Gray"))
        self.rgb_to_gray_button.setText(_translate("MainWindow", "RGB2GRAY"))
        self.rgb_to_hsv_button.setStatusTip(_translate("MainWindow", "RGB to HSV"))
        self.rgb_to_hsv_button.setText(_translate("MainWindow", "RGB2HSV"))
        self.segmentation_groupbox_2.setStatusTip(_translate("MainWindow", "segmentation"))
        self.segmentation_groupbox_2.setTitle(_translate("MainWindow", "Segmentation"))
        self.otsu_button.setStatusTip(_translate("MainWindow", "multi otsu"))
        self.otsu_button.setText(_translate("MainWindow", "Multi Otsu"))
        self.chan_vese_button.setStatusTip(_translate("MainWindow", "chan vese"))
        self.chan_vese_button.setText(_translate("MainWindow", "Chan Vese"))
        self.morphological_button.setStatusTip(_translate("MainWindow", "morphological snakes"))
        self.morphological_button.setText(_translate("MainWindow", "Morph Snakes"))
        self.edge_detection_groupbox_2.setStatusTip(_translate("MainWindow", "edge detection"))
        self.edge_detection_groupbox_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.roberts_button.setStatusTip(_translate("MainWindow", "roberts"))
        self.roberts_button.setText(_translate("MainWindow", "Roberts"))
        self.sobel_button.setStatusTip(_translate("MainWindow", "sobel"))
        self.sobel_button.setText(_translate("MainWindow", "Sobel"))
        self.scharr_button.setStatusTip(_translate("MainWindow", "scharr"))
        self.scharr_button.setText(_translate("MainWindow", "Scharr"))
        self.prewitt_button.setStatusTip(_translate("MainWindow", "prewitt"))
        self.prewitt_button.setText(_translate("MainWindow", "Prewitt"))
        self.source_image_groupBox.setStatusTip(_translate("MainWindow", "source image"))
        self.source_image_groupBox.setTitle(_translate("MainWindow", "Source Image"))
        self.output_image_groupBox.setStatusTip(_translate("MainWindow", "output image"))
        self.output_image_groupBox.setTitle(_translate("MainWindow", "Output Image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.actionOpen_Source.setText(_translate("MainWindow", "Open Source"))
        self.actionOpen_Source.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Output.setText(_translate("MainWindow", "Save Output"))
        self.actionSave_as_Output.setText(_translate("MainWindow", "Save as Output"))
        self.actionEXit.setText(_translate("MainWindow", "Exit"))
        self.actionEXit.setShortcut(_translate("MainWindow", "Shift+F4"))
        self.actionSource.setText(_translate("MainWindow", "Source"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionClear_Screen.setText(_translate("MainWindow", "Clear Screen"))
        self.actionUndo_Output.setText(_translate("MainWindow", "Undo Output"))        
        self.actionUndo_Output.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionRedo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.actionRedo_Output.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionRGB_to_GrayScale.setText(_translate("MainWindow", "RGB to GrayScale"))
        self.actionRGB_to_HSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.actionMulti_Otsu_Thresholding.setText(_translate("MainWindow", "Multi-Otsu Thresholding"))
        self.actionChan_Vese_Segmentation.setText(_translate("MainWindow", "Chan-Vese Segmentation"))
        self.actionMorphological_Snakes.setText(_translate("MainWindow", "Morphological Snakes"))
        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        
    def get_button_list(self):
        return ["open_folder_button",
                "save_button",
                "save_as_button",
                "clear_screen_button",
                "undo_button",
                "redo_button",
                "rgb_to_gray_button",
                "rgb_to_hsv_button",
                "otsu_button",
                "chan_vese_button",
                "morphological_button",
                "roberts_button",
                "sobel_button",
                "scharr_button",
                "prewitt_button"]
    
    def get_action_list(self):
        return ["actionOpen_Source",
                "actionSave_Output",
                "actionSave_as_Output",
                "actionClear_Screen",
                "actionUndo_Output",
                "actionRedo_Output",
                "actionRGB_to_GrayScale",
                "actionRGB_to_HSV",
                "actionMulti_Otsu_Thresholding",
                "actionChan_Vese_Segmentation",
                "actionMorphological_Snakes",
                "actionRoberts",
                "actionSobel",
                "actionScharr",
                "actionPrewitt"]
