from PySide2.QtCore import QObject
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine

import sys
import os


class QmlMainView(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.script_directory = os.path.dirname(__file__)
        self.qml_root = os.path.join(
            self.script_directory,
            "qml"
        )
        self.main_qml = os.path.join(self.qml_root, "canvasboard/main.qml")
        self.current_qml = self.main_qml
    
    def show(self):
        # Create an Qt instance of the application
        app = QApplication(sys.argv)

        # Create a QML engine.
        self.qml_engine = QQmlApplicationEngine()
        self.qml_engine.rootContext().setContextProperty("pyview", self)
        self.qml_engine.load(self.current_qml)
        self.qml_engine.quit.connect(app.quit)
        sys.exit(app.exec_())
