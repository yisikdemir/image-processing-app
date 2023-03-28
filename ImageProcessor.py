#########################################################
# Author: Yunus Emre ISIKDEMIR
#
# Date: 11.10.2020
# 
# Description: Image process application
#########################################################

# GUI libraries
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets

# Layout for the image process application
from Layout import Ui_Layout

# Utility functions
from python_stack import Stack
import numpy as np

# Image process
from skimage.segmentation import morphological_chan_vese
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese
from skimage import img_as_ubyte
from skimage import filters
from skimage import io
from PIL import Image

class ImageProcess(QtWidgets.QMainWindow):
    def __init__(self):
        super(ImageProcess, self).__init__()
                
        # Construct the layout via Ui_Layout class object
        self.layout = Ui_Layout()
        
        # Initilize the layout settings
        self.layout.setupUi(self)
        
        # Create signal for button - method, action - method connections
        self.createButtonSignal()
        self.createActionSignal()
        
        # Initilize the history for undo redo operation
        self.history = Stack()     
                
    # load the image as png or jpeg
    def load_img(self):
        # get the path
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()
        self.img_path = self.file_name[0]
        # set source and output image as same on the screen initially
        self.set_pixmaps()
        # Image is loaded then enable the processing buttons and actions        
        self.enable_all()
                                        
    # Enable all the image processors (actions and buttons). For disabling enabled = False
    def enable_all(self, enabled = True):
        list(map(lambda x: x.setEnabled(enabled), self.layout.actions_list))
        
    # clear the source and output image screen and disable actions
    def clear_screens(self):
        self.layout.img_src.clear()
        self.layout.img_output.clear()
        self.enable_all(False)
        
    # exit the application
    def exit_application(self):
        QtWidgets.QApplication.quit()  
        
    # save the processed image. example.png -> example_processed.png
    def save_img(self):
        pixmap = self.img_out
        pixmap.save(self.img_path[:-4] + "_processed.png")
        
    # save as image in png or jpg format
    def save_as_img(self):
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                                                            "PNG(*.png);;JPEG(*.jpg) ")
        pixmap = self.img_out
        pixmap.save(filePath);
                      
    # export as source
    def export_as_source(self):
        extension = self.img_path[-4:]
        new_extension = self.extensionConverter(extension)
        self.img_source.save(self.img_path[:-4] + new_extension)
    
    # export as output
    def export_as_output(self):
        extension = self.img_path[-4:]
        new_extension = self.extensionConverter(extension)
        self.img_out.save(self.img_path[:-4] + new_extension)
    
    # convert the extension. jpg -> png, png -> jpg
    def extensionConverter(self, extension):
        converted = {".png": ".jpg", ".jpg": ".png"}
        return converted[extension]
    
    # convert RGB to Gray scale
    def RGB2GRAY(self):
        self.image = self.get_image_array(isGray = True)
        self.array_to_pixmap(self.image, QImage.Format_Grayscale8)
            
    # convert RGB to HSV scale
    def RGB2HSV(self):
        image = Image.fromarray(self.get_image_array()).convert("HSV")
        self.array_to_pixmap(image)
        
    # undo process
    def undo_process(self):
        if self.history.size() == 1:
            return
        self.previous_img = self.history.pop()
        self.layout.img_output.setPixmap(self.history.top().scaled(self.img_size))
        
    # redo process
    def redo_process(self):
        self.layout.img_output.setPixmap(self.previous_img.scaled(self.img_size))
       
    # roberts edge detection
    def roberts_edge_detection(self):
        edge_roberts = filters.roberts(self.image)
        self.array_to_pixmap(edge_roberts, QImage.Format_Grayscale8)   
    
    # sobel edge detection
    def sobel_edge_detection(self):
        edge_sobel = filters.sobel(self.image)
        self.array_to_pixmap(edge_sobel, QImage.Format_Grayscale8)
    
    # scharr edge detection
    def scharr_edge_detection(self):
        edge_scharr = filters.scharr(self.image)
        self.array_to_pixmap(edge_scharr, QImage.Format_Grayscale8)
    
    # prewitt edge detection
    def prewitt_edge_detection(self):
        edge_prewitt = filters.prewitt(self.image)
        self.array_to_pixmap(edge_prewitt, QImage.Format_Grayscale8)
        
    # multi otsu thresholding
    def otsu_thresholding(self):
        otsu_th = threshold_multiotsu(self.image)
        regions = np.digitize(self.image, bins = otsu_th)
        image = Image.fromarray((regions * 255).astype(np.uint8))
        self.array_to_pixmap(image, QImage.Format_Grayscale8)       
    
    # chan vese segmentation
    def chan_vese_segmentation(self):
        cv = chan_vese(self.image, extended_output = True)
        self.array_to_pixmap(cv[0], QImage.Format_Grayscale8)
        
    # morphological snakes segmentation
    def morphological_snakes(self):
        ls = morphological_chan_vese(self.image, 35, smoothing=3)
        image = Image.fromarray((ls * 255).astype(np.uint8))
        self.array_to_pixmap(image, QImage.Format_Grayscale8)
            
    # set the input and output with same image initially
    def set_pixmaps(self):
        # get the size for fitting the image on the screen properly
        self.img_size = self.layout.img_src.size()
        # show input image on the screen
        self.img_source = QPixmap(self.img_path)
        self.layout.img_src.setPixmap(self.img_source.scaled(self.img_size))        
        # Show Output Image that is Not Processed initially
        self.img_out = QPixmap(self.img_path)
        self.layout.img_output.setPixmap(self.img_out.scaled(self.img_size))
        # Store in the history
        self.history.push(self.img_out)
        self.previous_img = self.history.top()
        
    # get image in ndarray format
    def get_image_array(self, isGray = False):
        return io.imread(self.img_path, as_gray = isGray)              
    
    # set the pixmap from the array
    def array_to_pixmap(self, img_arr, img_format = QImage.Format_RGB888):
        img = img_as_ubyte(img_arr)
        img = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], img_format)
        self.img_out = QPixmap.fromImage(img)
        self.layout.img_output.setPixmap(self.img_out.scaled(self.img_size))
        # Store in the history
        self.history.push(self.img_out)
        
    # methods in image processor class
    def getMethodList(self):
        # store in tuple to prevent corruption
        return ("load_img",
                "save_img",
                "save_as_img",
                "clear_screens",
                "undo_process",
                "redo_process",
                "RGB2GRAY",
                "RGB2HSV",
                "otsu_thresholding",
                "chan_vese_segmentation",
                "morphological_snakes",
                "roberts_edge_detection",
                "sobel_edge_detection",
                "scharr_edge_detection",
                "prewitt_edge_detection") 
        
    # create button signal for methods.
    def createButtonSignal(self):        
        for push_button, method in zip(self.layout.get_button_list(), self.getMethodList()):
            eval("self.layout." + push_button + ".clicked.connect(self." + method + ")")
            
    # create action signal for methods
    def createActionSignal(self):
        for each_action, method in zip(self.layout.get_action_list(), self.getMethodList()):
            eval("self.layout." + each_action + ".triggered.connect(self." + method + ")")
                
        # Create signal for not common methods for both button and action
        self.layout.actionSource.triggered.connect(self.export_as_source)
        self.layout.actionOutput.triggered.connect(self.export_as_output)        
        self.layout.actionEXit.triggered.connect(self.exit_application)