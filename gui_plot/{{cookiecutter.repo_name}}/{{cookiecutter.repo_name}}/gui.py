# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './{{cookiecutter.repo_name}}/gui.ui',
# licensing of './{{cookiecutter.repo_name}}/gui.ui' applies.
#
# Created: Mon Nov 25 11:05:14 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mdiArea.setObjectName("mdiArea")
        self.plot = QtWidgets.QWidget()
        self.plot.setObjectName("plot")
        self.gridLayout = QtWidgets.QGridLayout(self.plot)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = GraphicsWindow(self.plot)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.console_dock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_dock.sizePolicy().hasHeightForWidth())
        self.console_dock.setSizePolicy(sizePolicy)
        self.console_dock.setMinimumSize(QtCore.QSize(95, 113))
        self.console_dock.setObjectName("console_dock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.console = QtWidgets.QPlainTextEdit(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setStyleSheet("background-color:#CCCCCC;")
        self.console.setReadOnly(True)
        self.console.setMaximumBlockCount(200)
        self.console.setCenterOnScroll(False)
        self.console.setObjectName("console")
        self.gridLayout_2.addWidget(self.console, 0, 0, 1, 1)
        self.console_dock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console_dock)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConsole_Visibility = QtWidgets.QAction(MainWindow)
        self.actionConsole_Visibility.setCheckable(True)
        self.actionConsole_Visibility.setChecked(True)
        self.actionConsole_Visibility.setObjectName("actionConsole_Visibility")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionConsole_Visibility)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionConsole_Visibility, QtCore.SIGNAL("toggled(bool)"), self.console_dock.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "{{cookiecutter.repo_name}}", None, -1))
        self.plot.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Plot", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("MainWindow", "&View", None, -1))
        self.console_dock.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Console", None, -1))
        self.actionPreferences.setText(QtWidgets.QApplication.translate("MainWindow", "Preferences", None, -1))
        self.actionPreferences.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+,", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionNew_Project.setText(QtWidgets.QApplication.translate("MainWindow", "New Project", None, -1))
        self.actionNew_Project.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionOpen_Project.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionOpen_Project.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionDocumentation.setText(QtWidgets.QApplication.translate("MainWindow", "Documentation", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionConsole_Visibility.setText(QtWidgets.QApplication.translate("MainWindow", "Console Visibility", None, -1))
        self.actionConsole_Visibility.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+`", None, -1))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("MainWindow", "Save As", None, -1))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))

from pyqtgraph import GraphicsWindow
