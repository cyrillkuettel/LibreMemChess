import os
import shutil
import sys
from pathlib import Path
import aqt

from anki.importing import AnkiPackageImporter
# import the main window object (mw) from aqt

from aqt import mw
from aqt.utils import showInfo, qconnect

# from the documentation:
# "Generally speaking, if you write code that works in Qt6, and make sure
# to import any Qt classes from aqt.qt instead of directly from PyQt6, your
# code should also work in Qt5."
from aqt.qt import *


from .utils import media_files_path, refresh_ui, chess_apkg_path
from . import utils


anki_version = tuple(int(part) for part in aqt.appVersion.split("."))
is_first_run = False



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


def setup_initial_if_first_time():
    # Copy external media files to collection.media folder
    if is_first_run:
        media_dest = os.path.join(mw.col.media.dir(), '')
        showInfo(f"collections.media is {media_dest}")
        shutil.copytree(media_files_path(), media_dest)


def make_visible_in_collection():
    QTimer.singleShot(0, refresh_ui)


def test_import():
    def wrapper():
        # cardCount = mw.col.cardCount()
        # this might be useful, but for now we want to create a new package
        # showInfo("Card count: %d" % cardCount)

        setup_initial_if_first_time()

        importer = AnkiPackageImporter(mw.col, chess_apkg_path())
        importer.run()

        make_visible_in_collection()

        # Update media database
        # mw.col.media.force_resync()


    action = QAction("test", mw)
    qconnect(action.triggered, wrapper)
    mw.form.menuTools.addAction(action)


test_import()



action = QAction("Import Puzzles from Lichess", mw)
qconnect(action.triggered, run_quizlet_plugin)
mw.form.menuTools.addAction(action)
