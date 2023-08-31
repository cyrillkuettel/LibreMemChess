
# Anki
from aqt.qt import *

# PyQT
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
import aqt
from anki.importing import AnkiPackageImporter
# import the main window object (mw) from aqt
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *


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

def test_main():
    ## ======================================= test stuff
    def example_card_count():

        cardCount = mw.col.cardCount()
        mw.col.
        showInfo("Card count: %d" % cardCount)

    action = QAction("test", mw)
    qconnect(action.triggered, example_card_count)
    mw.form.menuTools.addAction(action)


test_main()

    ## ======================================= test stuff


action = QAction("Import Puzzles from Lichess", mw)
qconnect(action.triggered, run_quizlet_plugin)
mw.form.menuTools.addAction(action)
