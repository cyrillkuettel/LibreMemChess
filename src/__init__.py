import os
import shutil
import sys
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


# fixme: very inelegant, obnoxious even
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # src
from utils import media_files_path, refresh_ui

anki_version = tuple(int(part) for part in aqt.appVersion.split("."))


def chess_apkg_path():
    # todo: use ProfileManager absolute path to avoid issues
    from aqt.profiles import ProfileManager

    CURRENT = os.path.dirname(os.path.abspath(__file__))
    user_files = os.path.join(CURRENT, "user_files")
    return os.path.join(user_files, "chess.apkg")


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


def test_import():
    def wrapper():
        # cardCount = mw.col.cardCount()
        # this might be useful, but for now we want to create a new package
        # showInfo("Card count: %d" % cardCount)

        # Copy external media files to collection.media folder
        media_dest = os.path.join(mw.col.media.dir(), '')
        # showInfo(f"collections.media is {media_dest}")
        showInfo(f"media files path is {media_files_path()}")
        # shutil.copytree(media_files_path(), media_dest)

        showInfo(f"Importing {chess_apkg_path()}")
        importer = AnkiPackageImporter(mw.col, chess_apkg_path())
        importer.run()

        QTimer.singleShot(0, refresh_ui)

        # Update media database
        # mw.col.media.force_resync()


    action = QAction("test", mw)
    qconnect(action.triggered, wrapper)
    mw.form.menuTools.addAction(action)


test_import()



action = QAction("Import Puzzles from Lichess", mw)
qconnect(action.triggered, run_quizlet_plugin)
mw.form.menuTools.addAction(action)
