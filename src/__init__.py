
# Anki
from aqt import mw
from aqt.qt import *

# PyQT
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
import aqt
from anki.importing import AnkiPackageImporter

anki_version = tuple(int(part) for part in aqt.appVersion.split("."))


class QuizletWindow(QWidget):
    # main window of LibreMemChess plugin
    def __init__(self):
        super(QuizletWindow, self).__init__()
        self.init_ui()


    def init_ui(self):
        self.box_top = QVBoxLayout()
        self.box_upper = QHBoxLayout()


        self.setMinimumWidth(400)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setWindowTitle("Get Puzzles")
        self.show()


def run_quizlet_plugin():
    global __window
    __window = QuizletWindow()


# create menu item in Anki
action = QAction("Import Puzzles from Lichess", mw)
action.triggered.connect(run_quizlet_plugin)
mw.form.menuTools.addAction(action)
