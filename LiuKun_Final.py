 
from PySide import QtGui, QtCore
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import pymel.core as pm
import math 
import os

import cPickle as pickle

import logging 
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

"""
# DOWNLOAD AND PUT IN MAYA SCRIPTS DIRECTORY
https://github.com/lunaryorn/snippets/blob/master/qt4/designer/pyside_dynamic.py


# GOOD PAGE FOR ALL THE QT GUI stuff
http://qt-project.org/doc/qt-5.0/qtdoc/modules.html

# GREAT TUTORIALS
http://zetcode.com/gui/pysidetutorial/eventsandsignals/

how to run in maya
import connectionsUI
reload(connectionsUI)
connectionsUI.run()

"""
save={}
pickle.dump(save, open( r"Z:\Maya\scripts\myPickle.pkl", "wb" ) )
defaultLibararyPath = os.path.join(os.path.dirname(__file__), 'myPickle.pkl')


def run():
    """
    DON'T CHANGE EXCEPT THE 'BasiceExample' PART IF YOU NEED TO
    This is the main run function for your code's UI
    """
    global win
    
    win = ParticleSettings()
    win.show()

class ParticleSettings(QtGui.QDialog):

    def __init__(self, parent=None):
        """DON'T CHANGE THE FIRST TWO LINES """
        super(ParticleSettings, self).__init__(parent) 

        self.gridLayout = QtGui.QGridLayout()
        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 331, 411))
        self.tabWidget.setMinimumSize(QtCore.QSize(327, 415))
        self.Fire = QtGui.QWidget()
        self.Temperature = QtGui.QGroupBox(self.Fire)
        self.Temperature.setGeometry(QtCore.QRect(10, 20, 301, 91))
        self.hSl_tScale = QtGui.QSlider(self.Temperature)
        self.hSl_tScale.setGeometry(QtCore.QRect(160, 20, 131, 21))
        self.hSl_tScale.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_tScale = QtGui.QLCDNumber(self.Temperature)
        self.lcd_tScale.setGeometry(QtCore.QRect(110, 20, 41, 23))
        self.tScale = QtGui.QLabel(self.Temperature)
        self.tScale.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.tDissipation = QtGui.QLabel(self.Temperature)
        self.tDissipation.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.lcd_tDissipation = QtGui.QLCDNumber(self.Temperature)
        self.lcd_tDissipation.setGeometry(QtCore.QRect(110, 50, 41, 23))
        self.hSl_tDissipation = QtGui.QSlider(self.Temperature)
        self.hSl_tDissipation.setGeometry(QtCore.QRect(160, 50, 131, 21))
        self.hSl_tDissipation.setOrientation(QtCore.Qt.Horizontal)
        self.Fuel = QtGui.QGroupBox(self.Fire)
        self.Fuel.setGeometry(QtCore.QRect(10, 130, 301, 91))
        self.hSl_fScale = QtGui.QSlider(self.Fuel)
        self.hSl_fScale.setGeometry(QtCore.QRect(160, 20, 131, 21))
        self.hSl_fScale.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_fScale = QtGui.QLCDNumber(self.Fuel)
        self.lcd_fScale.setGeometry(QtCore.QRect(110, 20, 41, 23))
        self.fScale = QtGui.QLabel(self.Fuel)
        self.fScale.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.fReaSpe = QtGui.QLabel(self.Fuel)
        self.fReaSpe.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.lcd_fReaSpe = QtGui.QLCDNumber(self.Fuel)
        self.lcd_fReaSpe.setGeometry(QtCore.QRect(110, 50, 41, 23))
        self.hSl_fReaSpe = QtGui.QSlider(self.Fuel)
        self.hSl_fReaSpe.setGeometry(QtCore.QRect(160, 50, 131, 21))
        self.hSl_fReaSpe.setOrientation(QtCore.Qt.Horizontal)
        self.InputBias = QtGui.QGroupBox(self.Fire)
        self.InputBias.setGeometry(QtCore.QRect(10, 240, 301, 91))
        self.hSl_Incandescence = QtGui.QSlider(self.InputBias)
        self.hSl_Incandescence.setGeometry(QtCore.QRect(160, 20, 131, 21))
        self.hSl_Incandescence.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_Incandescence = QtGui.QLCDNumber(self.InputBias)
        self.lcd_Incandescence.setGeometry(QtCore.QRect(110, 20, 41, 23))
        self.Incandescence = QtGui.QLabel(self.InputBias)
        self.Incandescence.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.Opacity = QtGui.QLabel(self.InputBias)
        self.Opacity.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.lcd_Opacity = QtGui.QLCDNumber(self.InputBias)
        self.lcd_Opacity.setGeometry(QtCore.QRect(110, 50, 41, 23))
        self.hSl_Opacity = QtGui.QSlider(self.InputBias)
        self.hSl_Opacity.setGeometry(QtCore.QRect(160, 50, 131, 21))
        self.hSl_Opacity.setOrientation(QtCore.Qt.Horizontal)
        self.CreateFire = QtGui.QPushButton(self.Fire)
        self.CreateFire.setGeometry(QtCore.QRect(20, 350, 81, 23))  
        self.DeleteFire = QtGui.QPushButton(self.Fire)
        self.DeleteFire.setGeometry(QtCore.QRect(120, 350, 81, 23))      
        self.ResetFire = QtGui.QPushButton(self.Fire)
        self.ResetFire.setGeometry(QtCore.QRect(224, 350, 81, 23))
        self.tabWidget.addTab(self.Fire, "")
        self.Word = QtGui.QWidget()
        self.wordEdit = QtGui.QLineEdit(self.Word)
        self.wordEdit.setPlaceholderText("Maya")
        self.wordEdit.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.fontComboBox = QtGui.QFontComboBox(self.Word)
        self.fontComboBox.setGeometry(QtCore.QRect(140, 40, 171, 22))
        self.CreateWord = QtGui.QPushButton(self.Word)
        self.CreateWord.setGeometry(QtCore.QRect(160, 70, 151, 23))
        self.DeleteWord = QtGui.QPushButton(self.Word)
        self.DeleteWord.setGeometry(QtCore.QRect(10, 70, 141, 23))
        self.Input = QtGui.QLabel(self.Word)
        self.Input.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.toolBox = QtGui.QToolBox(self.Word)
        self.toolBox.setGeometry(QtCore.QRect(10, 130, 301, 241))
        self.Position = QtGui.QWidget()
        self.Position.setGeometry(QtCore.QRect(0, 0, 301, 237))
        self.X = QtGui.QLabel(self.Position)
        self.X.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lcd_x = QtGui.QLCDNumber(self.Position)
        self.lcd_x.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.hSl_x = QtGui.QSlider(self.Position)
        self.hSl_x.setGeometry(QtCore.QRect(100, 20, 181, 21))
        self.hSl_x.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_y = QtGui.QLCDNumber(self.Position)
        self.lcd_y.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.hSl_y = QtGui.QSlider(self.Position)
        self.hSl_y.setGeometry(QtCore.QRect(100, 60, 181, 21))
        self.hSl_y.setOrientation(QtCore.Qt.Horizontal)
        self.Y = QtGui.QLabel(self.Position)
        self.Y.setGeometry(QtCore.QRect(10, 60, 31, 21))
        self.lcd_z = QtGui.QLCDNumber(self.Position)
        self.lcd_z.setGeometry(QtCore.QRect(30, 100, 51, 21))
        self.hSl_z = QtGui.QSlider(self.Position)
        self.hSl_z.setGeometry(QtCore.QRect(100, 100, 181, 21))
        self.hSl_z.setOrientation(QtCore.Qt.Horizontal)
        self.Z = QtGui.QLabel(self.Position)
        self.Z.setGeometry(QtCore.QRect(10, 100, 31, 21))
        self.ResetWord = QtGui.QPushButton(self.Position)
        self.ResetWord.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.toolBox.addItem(self.Position, "")
        self.Color = QtGui.QWidget()
        self.Color.setGeometry(QtCore.QRect(0, 0, 301, 237))
        self.dial = QtGui.QDial(self.Color)
        self.dial.setGeometry(QtCore.QRect(200, 30, 91, 101))
        self.dial.setMaximum(359)
      #  myPixmap = QtGui.QPixmap(QtGui.QImage('color.jpg'))
     #   myScaledPixmap = myPixmap.scaled(self.dial.size(), Qt.KeepAspectRatio)
     #   self.dial.setPixmap(myScaledPixmap)
     #   self.colorLabel = QtGui.QLabel(self.Color)
     #   self.colorLabel.setGeometry(QtCore.QRect(210, 30, 91, 91))
     #   self.dial.setPixmap(QtGui.QPixmap(os.getcwd() + "/color.jpg"))
    #    self.colorLayout = QtGui.QVBoxLayout(self.colorWidget)
    #    self.colorLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_deColor = QtGui.QRadioButton(self.Color)
        self.radio_deColor.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.radio_deColor.setChecked(True)
        self.radio_setColor = QtGui.QRadioButton(self.Color)
        self.radio_setColor.setGeometry(QtCore.QRect(180, 10, 82, 17))
        self.lcd_R = QtGui.QLCDNumber(self.Color)
        self.lcd_R.setGeometry(QtCore.QRect(20, 40, 41, 21))
        self.hSl_R = QtGui.QSlider(self.Color)
        self.hSl_R.setEnabled(False)
        self.hSl_R.setGeometry(QtCore.QRect(70, 40, 131, 21))
        self.hSl_R.setOrientation(QtCore.Qt.Horizontal)
        self.R = QtGui.QLabel(self.Color)
        self.R.setGeometry(QtCore.QRect(10, 40, 31, 21))
        self.hSl_G = QtGui.QSlider(self.Color)
        self.hSl_G.setEnabled(False)
        self.hSl_G.setGeometry(QtCore.QRect(70, 70, 131, 21))
        self.hSl_G.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_G = QtGui.QLCDNumber(self.Color)
        self.lcd_G.setGeometry(QtCore.QRect(20, 70, 41, 21))
        self.G = QtGui.QLabel(self.Color)
        self.G.setGeometry(QtCore.QRect(10, 70, 31, 21))
        self.hSl_B = QtGui.QSlider(self.Color)
        self.hSl_B.setEnabled(False)
        self.hSl_B.setGeometry(QtCore.QRect(70, 100, 131, 21))
        self.hSl_B.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_B = QtGui.QLCDNumber(self.Color)
        self.lcd_B.setGeometry(QtCore.QRect(20, 100, 41, 21))
        self.B = QtGui.QLabel(self.Color)
        self.B.setGeometry(QtCore.QRect(10, 100, 31, 21))
        self.word_tran = QtGui.QLabel(self.Color)
        self.word_tran.setGeometry(QtCore.QRect(10, 150, 81, 21))
        self.lcd_wordTran = QtGui.QLCDNumber(self.Color)
        self.lcd_wordTran.setGeometry(QtCore.QRect(90, 150, 51, 21))
        self.hSl_wordTran = QtGui.QSlider(self.Color)
        self.hSl_wordTran.setGeometry(QtCore.QRect(150, 150, 141, 21))
        self.hSl_wordTran.setOrientation(QtCore.Qt.Horizontal)
        self.line_2 = QtGui.QFrame(self.Color)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 281, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.toolBox.addItem(self.Color, "")
        self.line = QtGui.QFrame(self.Word)
        self.line.setGeometry(QtCore.QRect(10, 100, 301, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.tabWidget.addTab(self.Word, "")
        self.Ink = QtGui.QWidget()
        self.CreateInk = QtGui.QPushButton(self.Ink)
        self.CreateInk.setGeometry(QtCore.QRect(230, 20, 71, 26))
        self.DeleteInk = QtGui.QPushButton(self.Ink)
        self.DeleteInk.setGeometry(QtCore.QRect(230, 55, 71, 26))
        self.addToList = QtGui.QPushButton(self.Ink)
        self.addToList.setGeometry(QtCore.QRect(230, 90, 71, 26))
        self.inkList = QtGui.QListWidget(self.Ink)
        self.inkList.setGeometry(QtCore.QRect(20, 20, 171, 111))
        self.inkOpenBtn = QtGui.QPushButton(self.Ink)
        self.inkOpenBtn.setGeometry(QtCore.QRect(20, 140, 71, 23))
        self.inkSaveBtn = QtGui.QPushButton(self.Ink)
        self.inkSaveBtn.setGeometry(QtCore.QRect(120, 140, 71, 23))
        self.btnDrop = QtGui.QPushButton(self.Ink)
        self.btnDrop.setGeometry(QtCore.QRect(230, 125, 71, 36))
        self.line_3 = QtGui.QFrame(self.Ink)
        self.line_3.setGeometry(QtCore.QRect(200, 20, 20, 141))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4 = QtGui.QFrame(self.Ink)
        self.line_4.setGeometry(QtCore.QRect(20, 170, 281, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.inkColor = QtGui.QColorDialog() 
        self.verticalLayoutWidget = QtGui.QWidget(self.Ink)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 281, 181))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.inkColor)
    #    self.inkColor.setGeometry(QtCore.QRect(30, 230, 261, 141))
      #  self.inkColor.getColor()

        self.tabWidget.addTab(self.Ink, "")

        # SETTING WINDOW TITLE
        self.setWindowTitle("Particle")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fire),"Fire")
        self.Temperature.setTitle("Temperature")
        self.tScale.setText("Scale :")
        self.tDissipation.setText("Dissipation :")
        self.Fuel.setTitle("Fuel")
        self.fScale.setText("Scale :")
        self.fReaSpe.setText("Reaction Speed :")
        self.InputBias.setTitle("InputBias")
        self.Incandescence.setText("Incandescence")
        self.Opacity.setText("Opacity")
        self.CreateFire.setText("Create")
        self.DeleteFire.setText("Delete")
        self.ResetFire.setText("Reset")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Word),"Word")
        self.Input.setText("Input a word:")
        self.CreateWord.setText("OK")
        self.toolBox.setItemText(self.toolBox.indexOf(self.Position), "Position")
        self.X.setText("X :")
        self.Y.setText("Y :")
        self.Z.setText("Z :")
        self.DeleteWord.setText("Clean")
        self.ResetWord.setText("Reset")
        self.toolBox.setItemText(self.toolBox.indexOf(self.Color), "Color")
        self.radio_deColor.setText("default color")
        self.radio_setColor.setText("set color")
        self.R.setText("R ")
        self.B.setText("B ")
        self.G.setText("G ")
        self.word_tran.setText("transparency:")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ink),"Ink")
        self.inkOpenBtn.setText("open")
        self.inkSaveBtn.setText("save")
        self.CreateInk.setText("create Ink")
        self.btnDrop.setText("click me")
        self.DeleteInk.setText("delete")
        self.addToList.setText("addToList")

        # set Slider values
        self.hSl_tScale.setRange(0,10000)
        self.hSl_tScale.setSliderPosition(1000)   
        self.lcd_tScale.display(1)

        self.hSl_tDissipation.setRange(0,1000)
        self.hSl_tDissipation.setSliderPosition(300)
        self.lcd_tDissipation.display(0.3)

        self.hSl_fScale.setRange(0,10000)
        self.hSl_fScale.setSliderPosition(3000)
        self.lcd_fScale.display(3)

        self.hSl_fReaSpe.setRange(0,1000)
        self.hSl_fReaSpe.setSliderPosition(1000)
        self.lcd_fReaSpe.display(1)
 
        self.hSl_Incandescence.setRange(-1000,1000)
        self.hSl_Incandescence.setSliderPosition(250)
        self.lcd_Incandescence.display(0.25)

        self.hSl_Opacity.setRange(-1000,1000)
        self.hSl_Opacity.setSliderPosition(-100)
        self.lcd_Opacity.display(-0.1)

        self.hSl_x.setRange(-10000,10000)
        self.hSl_x.setSliderPosition(0) 
        self.lcd_x.display(0)

        self.hSl_y.setRange(-10000,10000)
        self.hSl_y.setSliderPosition(0) 
        self.lcd_y.display(0)

        self.hSl_z.setRange(-10000,10000)
        self.hSl_z.setSliderPosition(0) 
        self.lcd_z.display(0)

        self.hSl_R.setRange(0,1000)
        self.hSl_R.setSliderPosition(500) 
        self.lcd_R.display(0.5)

        self.hSl_B.setRange(0,1000)
        self.hSl_B.setSliderPosition(500) 
        self.lcd_B.display(0.5)

        self.hSl_G.setRange(0,1000)
        self.hSl_G.setSliderPosition(500) 
        self.lcd_G.display(0.5)

        self.hSl_wordTran.setRange(0,1000)
        self.hSl_wordTran.setSliderPosition(0)
        self.lcd_wordTran.display(0)


        # ADDED TO GET IT TO SHOW
        self.gridLayout.addWidget(self.tabWidget)
        self.setLayout(self.gridLayout)
        self.show()

        # variable
        self.fire=[]
        self.word=[]
        self.wordPar=[]
        self.wordTexture=[]
        self.setRGB={'r':0.5,'g':0.5,'b':0.5}
        self.font='Tahoma'
        self.ink=[]
        self.inkEmi=[]

        #time line
        mc.playbackOptions(min=1,max=300,loop='continuous')

        # MAKE THE BUTTONS WORK
        self.makeConnections()

        # LOAD DEFAULT LIBRARY

        self.controllers =  pickle.load(open( defaultLibararyPath,"rb"))
        

    def makeConnections(self):
        """ connect """

        # adjust fire
        self.hSl_tScale.valueChanged.connect(self.tScaleHandler)
        self.hSl_tDissipation.valueChanged.connect(self.tDissipationHandler)
        self.hSl_fScale.valueChanged.connect(self.fScaleHandler)
        self.hSl_fReaSpe.valueChanged.connect(self.fReaSpeHandler)
        self.hSl_Incandescence.valueChanged.connect(self.IncandescenceHandler)
        self.hSl_Opacity.valueChanged.connect(self.OpacityHandler)

        # adjust word
        self.fontComboBox.activated.connect(self.fontChanged)
        self.radio_deColor.clicked.connect(self.radioEventHandler)
        self.radio_setColor.clicked.connect(self.radioEventHandler)
        self.hSl_x.valueChanged.connect(self.XHandler)
        self.hSl_y.valueChanged.connect(self.YHandler)
        self.hSl_z.valueChanged.connect(self.ZHandler)
        self.hSl_R.valueChanged.connect(self.RHandler)
        self.hSl_G.valueChanged.connect(self.GHandler)
        self.hSl_B.valueChanged.connect(self.BHandler)        
        self.dial.valueChanged.connect(self.DialHandler)
        self.hSl_wordTran.valueChanged.connect(self.wordTranHandler)

        # adjust ink
        self.btnDrop.clicked.connect(self.addDrop)
        self.inkOpenBtn.clicked.connect(self.loadLibrary)
        self.inkSaveBtn.clicked.connect(self.saveLibrary)
        self.inkList.itemDoubleClicked.connect(self.inkDoubleClicked)
        self.inkColor.currentColorChanged.connect(self.InkColorselect)
        self.addToList.clicked.connect(self.addSelectedtoList)

        # main button 
        self.CreateFire.clicked.connect(self.makeFire)
        self.ResetFire.clicked.connect(self.fireReset)
        self.DeleteFire.clicked.connect(self.fireDelete)
        self.CreateWord.clicked.connect(self.makeWordBtn)
        self.ResetWord.clicked.connect(self.wordReset)
        self.DeleteWord.clicked.connect(self.wordDelete)
        self.CreateInk.clicked.connect(self.makeInk)
        self.DeleteInk.clicked.connect(self.inkDelete)

    def tScaleHandler(self):
        """ FOR FIRE: adjust temperature scale"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_tScale.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].temperatureScale.set(newVal)

    def tDissipationHandler(self):
        """ FOR FIRE: adjust temperature dissipation"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_tDissipation.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].temperatureDissipation.set(newVal)

    def fScaleHandler(self):
        """ FOR FIRE: adjust fuel scale"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_fScale.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].fuelScale.set(newVal)

    def fReaSpeHandler(self):
        """ FOR FIRE: adjust fuel reaction speed"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_fReaSpe.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].reactionSpeed.set(newVal)

    def IncandescenceHandler(self):
        """ FOR FIRE: adjust incandescence"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_Incandescence.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].incandescenceInputBias.set(newVal)

    def OpacityHandler(self):
        """ FOR FIRE: adjust opacity"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_Opacity.display(newVal)

    #    fire = pm.ls(sl=1)[0]
    #    fireShape = fire.getShape()
        self.fire[-1].opacityInputBias.set(newVal)

    def fireReset(self):
        """ FOR FIRE: reset attributes to default value"""

        fire = pm.ls(sl=1)[0]
        fireShape = fire.getShape()
        fireShape.temperatureScale.set(1)
        fireShape.temperatureDissipation.set(0.3)
        fireShape.fuelScale.set(3)
        fireShape.reactionSpeed.set(1)
        fireShape.incandescenceInputBias.set(0.25)
        fireShape.opacityInputBias.set(-0.1)

        self.hSl_tScale.setSliderPosition(1000)   
        self.lcd_tScale.display(1)
        self.hSl_tDissipation.setSliderPosition(300)
        self.lcd_tDissipation.display(0.3)
        self.hSl_fScale.setSliderPosition(3000)
        self.lcd_fScale.display(3)
        self.hSl_fReaSpe.setSliderPosition(1000)
        self.lcd_fReaSpe.display(1)
        self.hSl_Incandescence.setSliderPosition(250)
        self.lcd_Incandescence.display(0.25)
        self.hSl_Opacity.setSliderPosition(-100)
        self.lcd_Opacity.display(-0.1)

    def fireDelete(self):
        """ FOR FIRE: delete choosen fire"""

        fire = pm.ls(sl=1)[0]
        pm.delete()


    def fontChanged(self):
        """ FOR WORD: delete choosen fire"""

        getfont = self.fontComboBox.currentFont()
        self.font = getfont.family() 
        # self.font.append(self.fontComboBox.currentFont)
        print self.font

    def XHandler(self):
        """ FOR WORD: change X translate"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.01
        self.lcd_x.display(newVal)

    #    word = pm.ls(sl=1)[0]
        self.word[-1].setAttr("tx",newVal)


    def YHandler(self):
        """ FOR WORD: change Y translate"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.01
        self.lcd_y.display(newVal)

    #    word = pm.ls(sl=1)[0]
        self.word[-1].setAttr("ty",newVal)

    def ZHandler(self):
        """ FOR WORD: change Z translate"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.01
        self.lcd_z.display(newVal)

    #    word = pm.ls(sl=1)[0]
        self.word[-1].setAttr("tz",newVal)

    def wordReset(self):
        """ FOR WORD: reset translate attributes to default value"""

    #    word = pm.ls(sl=1)[0]
        pm.setAttr(self.word[-1]+".tx",0)
        pm.setAttr(self.word[-1]+".ty",0)
        pm.setAttr(self.word[-1]+".tz",0)

        self.hSl_x.setSliderPosition(0) 
        self.lcd_x.display(0)
        self.hSl_y.setSliderPosition(0) 
        self.lcd_y.display(0)
        self.hSl_z.setSliderPosition(0) 
        self.lcd_z.display(0)

    def wordDelete(self):
        """ FOR WORD: delete every object and any unused material"""

        pm.mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        pm.select(all=True)
        pm.delete()

    def radioEventHandler(self):
        """ FOR WORD: choose color style of the word"""

        if self.radio_deColor.isChecked():	

            self.hSl_R.setEnabled(False)
            self.hSl_B.setEnabled(False)
            self.hSl_G.setEnabled(False)
            self.dial.setEnabled(False)

        if self.radio_setColor.isChecked():

            self.hSl_R.setEnabled(True)
            self.hSl_B.setEnabled(True)
            self.hSl_G.setEnabled(True)
            self.dial.setEnabled(True)

        else :
        	self.hSl_R.setSliderPosition(500) 
	        self.lcd_R.display(0.5)
	        self.hSl_B.setSliderPosition(500) 
	        self.lcd_B.display(0.5)
	        self.hSl_G.setSliderPosition(500) 
	        self.lcd_G.display(0.5)

	        pm.dynExpression(self.wordPar[-1],s='rgbPP=position;',rbd=1)

    def RHandler(self):
        """ FOR WORD: change red"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        self.setRGB['r'] = val*0.001
        self.lcd_R.display(self.setRGB['r'])
    #    print self.setRGB['r']

    	pm.dynExpression(self.wordPar[-1],s="rgbPP=<<%s,%s,%s>>;"%(self.setRGB['r'],self.setRGB['g'],self.setRGB['b']),rbd=1)

        
    def GHandler(self):
        """ FOR WORD: change green"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        self.setRGB['g'] = val*0.001
        self.lcd_G.display(self.setRGB['g'])

        pm.dynExpression(self.wordPar[-1],s="rgbPP=<<%s,%s,%s>>;"%(self.setRGB['r'],self.setRGB['g'],self.setRGB['b']),rbd=1)


    def BHandler(self):
        """ FOR WORD: change blue"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        self.setRGB['b'] = val*0.001
        self.lcd_B.display(self.setRGB['b'])

        pm.dynExpression(self.wordPar[-1],s="rgbPP=<<%s,%s,%s>>;"%(self.setRGB['r'],self.setRGB['g'],self.setRGB['b']),rbd=1)

    def DialHandler(self):
        """ FOR WORD: change color with dial"""

        slider = self.sender() 
        val = slider.value()
        r=val
        g=val
        b=val

        # count the value of RGB
        if val<=150:
            r=1
        elif (val>150 and val<=180):
            r=1-(val-150)/30.000
        elif val>330:
            r=(val-330)/30.000
        else:
            r=0

        if (val<=30 or val>240):
            g=1
        elif (val>30 and val<=60):
            g=1-(val-30)/30.000
        elif (val>210 and val<=240):
            g=(val-210)/30.000
        else:
            g=0 

        if (val>120 and val<=270):
            b=1
        elif (val>90 and val<=120):
            b=(val-90)/30.000
        elif (val>270 and val<=300):
            b=1-(val-270)/30.000
        else:
            b=0 

        print r
        print g
        print b

        pm.dynExpression(self.wordPar[-1],s="rgbPP=<<%s,%s,%s>>;"%(r,g,b),rbd=1)

    def wordTranHandler(self):
        """ FOR WORD: change transparency"""

        slider = self.sender() 
        val = slider.value()
    #    print("val",val)
        newVal = val*0.001
        self.lcd_wordTran.display(newVal)

        self.wordTexture[-1].transparency.set(newVal,newVal,newVal)


    def makeWordBtn(self):
        """ FOR WORD: make a new word"""

        if self.wordEdit.text():
            word = self.wordEdit.text()
        else:
            word = "Maya"
        
        self.makeWord(word)


    def addDrop(self):
        """ FOR INK: add a drop"""

        time = pm.currentTime(query=True)
        print ("current time:%s" %time)

        mc.setKeyframe(self.inkEmi[-1]+".fde",v=0,t=time)
        mc.setKeyframe(self.inkEmi[-1]+".fde",v=20,t=time+20)
        mc.setKeyframe(self.inkEmi[-1]+".fde",v=0,t=time+21)

    def inkDelete(self):
        """ FOR INK: delete chosen ink """

        ink = pm.ls(sl=1)[0] 
        pm.delete()

    def InkColorselect(self):
        """ FOR INK: change ink color """

        color = self.inkColor.currentColor()
        r = color.red()/255.000
        g= color.green()/255.000
        b = color.blue()/255.000
        print ("r:%f"%r)
        print ("g:%f"%g)
        print ("b:%f\n"%b)
        
        self.ink[-1].incandescence[0].incandescence_Color.set(r,g,b)
        self.ink[-1].incandescence[0].incandescence_Position.set(r+0.1)
        self.ink[-1].incandescence[0].incandescence_Position.set(r-0.1)

    def loadLibrary(self):
        """ FOR INK: open file"""

        # GET THE PATH TO THE PICKLE TO LOAD
        pickleLibPath = pm.fileDialog()
        _logger.debug("LOADING : %s" % pickleLibPath)
        
        # TEMP HOLDER FOR DATA
        controllers = None
        
        # IF THERE WAS A PATH TRY AN LOAD IT UP
        if pickleLibPath:
            controllers =  pickle.load(open( pickleLibPath,"rb"))

        # UPDATING CONTROLLERS
        if controllers:
            if controllers.keys():
                _logger.debug("replacing self.controllers with pickle data")
                self.controllers = controllers
        

    def saveLibrary(self):
        """ FOR INK: save created ink"""

        # GET THE PATH TO THE PICKLE TO LOAD
        pickleLibPath = pm.fileDialog2()
        _logger.debug("SAVING : %s" % pickleLibPath)
        if pickleLibPath:
            pickle.dump( self.controllers, open( pickleLibPath[0], "wb" ) ) 

        con = pm.selected()[0]

        # UPDATE THE LIST WIDGET
        self.updateListWidget()

    def addSelectedtoList(self):
        """ saves the selected con to the library and displays it in the list widget"""
        _logger.debug("saving a selected CON in the library")
        inkSelect = pm.selected()[0]
    
        pickleDict = {}
        
        inkList=[]

        inkList.append(inkSelect)
         
        # PROMPT FOR CON NAME
        inkName = pm.promptBox("Controller Name", "Enter name:", "Okay", "Cancel")
        
        # ADD TO THE DICTIONARY 
        if inkName:
            self.controllers[inkName] = {}

        # UPDATE THE LIST WIDGET
        self.updateListWidget()

    def inkDoubleClicked(self):
        """ listWidget Item clicked"""
        
        # GET THE QListViewWidget
        sender = self.sender()
        
        # GET THE QListWidgetItem selected:
        listItem = sender.currentItem()
        
        # GET THE TEXT ON THE ITEM which is a key in the controllers dictionary
        
        text = listItem.text()
        
        _logger.debug("sender: %s " % text)
        
        # GENRATE THE CON
        self.generateCon(text)

    def generateCon(self,conName,color=6, scaleCon=1.0):
        """ generates the CON selected by the list"""

        _logger.debug("CON NAME : %s" % conName)
        
        # GET THE VALUES YOU NEED TO MAKE THE CON        
        inks = self.controllers.get(inkName,None)
        # CREATE CON         
        newink = self.makeInk()

        
        # DE SELECT ALL
        pm.select(d=True)
        
        # RETURN THE CURVE
        return newink

    def updateListWidget(self):
        """ Adds an item to the list wiget """
        _logger.debug("updating list widget")
        
        # REMOVE THE WHOLE CONTENTS FIRST
        self.inkList.clear()
        
        # ADD THEM ALL AGAIN
        for k,v in self.controllers.iteritems():
            
            item = QtGui.QListWidgetItem(k)
            self.inkList.addItem(item)
            item.doubleClicked.connect(self.inkDoubleClicked)

    def makeFire(self):
        """ create fire effects"""

        fluidShape = pm.mel.eval('create3DFluid(20, 30, 20, 15, 20, 15)')
        mc.move(0,8,0)
        fluidShape = pm.PyNode(fluidShape)  
        self.fire.append(fluidShape)    
        # see(fluidShape)
        
        fluidemitter = pm.fluidEmitter(pos=(0, 1, 0),type='omni',der=1,her=2,fer=4,fdr=2,r=100.0,cye='none',cyi=1, mxd=1, mnd=0)
        fluidemitter = pm.PyNode(fluidemitter)    
        # see(fluidemitter)
        
        fluidemitter.setParent(fluidShape)
        pm.connectDynamic(fluidShape,em=fluidemitter)
        
        fluidShape.boundaryY.set(2)
        fluidShape.temperatureMethod.set(2)
        fluidShape.fuelMethod.set(2)
        fluidemitter.fluidHeatEmission.set(2)
        fluidemitter.fluidFuelEmission.set(4)
        # fluidShape.viscosity.set(0.01)
        # fluidShape.velocityDamp.set(0.02)
        # fluidShape.simulationRateScale.set(2)
        
        fluidShape.densityScale.set(0.5)
        fluidShape.densityBuoyancy.set(5)
        # fluidShape.densityDissipation.set(0.5)
        # fluidShape.densityDiffusion.set(0.1)
        # fluidShape.densityNoise.set(0.2)
        # fluidShape.densityTension.set(0.2)
        # fluidShape.densityGradientForce.set(-1)
        
        fluidShape.velocitySwirl.set(10)
        fluidShape.velocityNoise.set(0.5)
        
        # fluidShape.turbulenceStrength.set(0.03)
        # fluidShape.turbulenceFrequency.set(0.1)
        
        fluidShape.temperatureScale.set(1)
        fluidShape.buoyancy.set(5)
        fluidShape.temperatureDissipation.set(0.3)
        # fluidShape.temperatureDiffusion.set(0.1)
        # fluidShape.temperatureTurbulence.set(0.4)
        fluidShape.temperatureNoise.set(0.03)
        # fluidShape.temperatureTension.set(0.15)
        
        fluidShape.fuelScale.set(3)
        fluidShape.reactionSpeed.set(1)
        fluidShape.lightReleased.set(0.3)
        fluidShape.maxReactionTemp.set(10)
        
        # see(fluidShape.transparency)
        fluidShape.transparency.set(0.22,0.22,0.22)
        fluidShape.color[0].color_Color.set(0,0,0)
        
        fluidShape.incandescence[3].incandescence_Color.set(1,1,1)
        fluidShape.incandescence[3].incandescence_Position.set(0.994)
        fluidShape.incandescence[2].incandescence_Position.set(0.96)
        fluidShape.incandescence[1].incandescence_Position.set(0.56)
        fluidShape.incandescence[0].incandescence_Position.set(0.03)
        fluidShape.incandescenceInputBias.set(0.25)
        
        fluidShape.opacity[1].opacity_Interp.set(1)
        fluidShape.opacity[1].opacity_FloatValue.set(0.41)
        fluidShape.opacity[1].opacity_Position.set(0.31)
        fluidShape.opacity[2].opacity_Interp.set(1)
        fluidShape.opacity[2].opacity_FloatValue.set(0.9)
        fluidShape.opacity[2].opacity_Position.set(0.51)
        fluidShape.opacity[3].opacity_Interp.set(1)
        fluidShape.opacity[3].opacity_FloatValue.set(0.55)
        fluidShape.opacity[3].opacity_Position.set(0.64)
        fluidShape.opacity[4].opacity_Interp.set(1)
        fluidShape.opacity[4].opacity_FloatValue.set(0.51)
        fluidShape.opacity[4].opacity_Position.set(0.8)
        fluidShape.opacity[5].opacity_Interp.set(1)
        fluidShape.opacity[5].opacity_FloatValue.set(0.23)
        fluidShape.opacity[5].opacity_Position.set(1)
        fluidShape.opacityInput.set(6)
        fluidShape.opacityInputBias.set(-0.1)

        fluidShape.select()

    def makeWord(self,in_word):
        """ create particle word"""

    #    in_word='maya'
    #    font = 'Arial'
    #    font = self.fontChoose.currentFont()
    #    print self.font[-1]
        tCrvs = pm.textCurves(t=in_word,f=self.font,ch=0)
        tCrvs = pm.PyNode(tCrvs[0])  
        
        letterNum = tCrvs.numChildren()
        letter = []
        grpWord = pm.group(em=True)
        for n in range(0,letterNum):
            letterShape = pm.listRelatives(tCrvs.getChildren()[n],type='nurbsCurve',ad=True,path=True)
            letter.append(pm.planarSrf(letterShape,ch=1,tol=0.01,o = 1,po=1)[0])
        pm.parent(letter,grpWord)
            
        # pm.select(grpWord) 
        wordshape = pm.polyUnite(ch=1,muv=1)[0]
        mc.DeleteHistory()   
        wordshape=pm.PyNode(wordshape)
        self.word.append(wordshape)
        # see(wordshape)
        
        pm.setAttr(tCrvs+".visibility",0)
        wordshape.centerPivots()
        # pm.move(-8,0,0)
        pm.makeIdentity(apply=True,t=1,r=1,s=1,n=0,pn=1)
        wordshape.makeLive()
        
        
        wordshape.select()
        pm.emitter(type='surface',r=1000,spd=0)
        wordEmitter = wordshape.getChildren()[1]
        wordEmitter = pm.PyNode(wordEmitter)
        wordEmitter.cycleEmission.set(1)
        wordEmitter.maxDistance.set(5)
        # see(wordEmitter)
        # wordEmitter.select()
        wordParticle = pm.particle()[0]
        wordParticle = pm.PyNode(wordParticle)
        wordPaShape = wordParticle.getShape()
        self.wordPar.append(wordPaShape)
        pm.connectDynamic(wordParticle,em=wordEmitter)
        mc.setKeyframe([wordEmitter+".rate"],v=200,t=100)
        mc.setKeyframe([wordEmitter+".rate"],v=0,t=101)
        
        wordPaShape.lifespanMode.set(2)
        wordPaShape.attr("lifespan").set(5)
        wordPaShape.lifespanRandom.set(3)
            
        wordPaShape.particleRenderType.set(0)
        wordPaShape.addAttr('colorAccum',dv=True,at='bool',internalSet=True,keyable=True)
        wordPaShape.addAttr('useLighting',dv=False,at='bool',internalSet=True)
        wordPaShape.addAttr('multiCount',at='long',min=1,max=60,dv=2,internalSet=True)
        wordPaShape.addAttr('multiRadius',at='float',min=1,max=60,dv=0.3,internalSet=True)
        wordPaShape.addAttr('normalDir',min=1,max=3,at='long',internalSet=True,dv=2)
        wordPaShape.addAttr('pointSize',min=1,max=60,at='long',internalSet=True,dv=2)
        wordPaShape.colorAccum.set(1)
        wordPaShape.multiCount.set(7)
        wordPaShape.pointSize.set(1)
        
        wordPaShape.addAttr('goalU',dt='doubleArray',keyable=True)
        wordPaShape.addAttr('goalV',dt='doubleArray',keyable=True)
        pm.dynExpression(wordPaShape,s='goalU=rand(0,1);\ngoalV=rand(0,1);',c=1)
        wordPaShape.addAttr('rgbPP',dt='vectorArray',keyable=True)
        pm.dynExpression(wordPaShape,s='rgbPP=position;',rbd=1)
        
        pm.goal(wordParticle,g=wordshape,w=1, utr=0)
        pm.setKeyframe(wordParticle,attribute='goalWeight[0]',v=1,t=90)
        pm.setKeyframe(wordParticle,attribute='goalWeight[0]',v=0,t=100)
        pm.setAttr(wordshape+".visibility",0)
        
        
        field = pm.turbulence(pos=(0,0,2),m=10)
        pm.connectDynamic(wordParticle,f=field)
        pm.setKeyframe(field,attribute='tx',v=12,t=100)
        pm.setKeyframe(field,attribute='tx',v=0,t=110)
        pm.parent(field,wordshape)
        
        lambert = pm.shadingNode('lambert',asShader=1)
        lambertSG = pm.sets(renderable=True,empty=1,noSurfaceShader=True,name=lambert+"SG")
        pm.connectAttr(lambert+".outColor",lambert+"SG.surfaceShader",f=1)
        # pm.sets(wordParticle,forceElement='lambert6SG',e=True)
        wordParticle.select()
        pm.hyperShade(a=lambertSG)
        self.wordTexture.append(lambert)
        pm.setAttr(lambert+".transparency" ,0.7,0.7,0.7,type='double3')
        pm.setAttr(lambert+".incandescence",0.6,0.6,0.6,type='double3')
        pm.setAttr(lambert+".incandescence",0.5,0.5,0.5,type='double3')
        pm.setAttr(lambert+".glowIntensity",0.6)

        wordshape.select()

    def makeInk(self):
        """ create ink drops"""

        inkShape = pm.mel.eval('create3DFluid(50, 50, 50, 10, 20, 10)')
        mc.move(0,10,0)
        inkShape = pm.PyNode(inkShape)
        self.ink.append(inkShape)
        inkemitter = pm.fluidEmitter(pos=(0, 20, 0),type='omni',der=20,her=1,fer=1,fdr=2,r=100.0,cye='none',cyi=1, mxd=1, mnd=0)
        inkemitter = pm.PyNode(inkemitter) 
        self.inkEmi.append(inkemitter)
        
        inkemitter.setParent(inkShape)
        pm.connectDynamic(inkShape,em=inkemitter)
        
        inkShape.highDetailSolve.set(3)
        inkShape.densityBuoyancy.set(-1)
        inkShape.color[0].color_Color.set(0,0,0)
        inkShape.incandescence[2].remove()
        inkShape.incandescence[1].remove()
        
        
        inkShape.renderInterpolator.set(3)
        inkShape.selfShadowing.set(1)
        inkShape.realLights.set(0)
        
        mc.setKeyframe(inkemitter+".fde",v=20,t=20)
        mc.setKeyframe(inkemitter+".fde",v=0,t=21)

        pm.select(deselect = True)
        inkShape.select()