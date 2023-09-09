import shutil
from pathlib import Path
from anki.collection import Collection

from anki.importing import AnkiPackageImporter
from anki.notes import Note
# import the main window object (mw) from aqt

from aqt import mw, appVersion
from aqt.utils import showInfo, qconnect

# from the documentation:
# "Generally speaking, if you write code that works in Qt6, and make sure
# to import any Qt classes from aqt.qt instead of directly from PyQt6, your
# code should also work in Qt5."
from aqt.qt import *


from .utils import media_files_path, refresh_ui, chess_apkg_path
from . import utils


anki_version = tuple(int(part) for part in appVersion.split("."))
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
def get_last_added_note(collection: 'Collection'):
    last_nid = collection.db.scalar("SELECT max(id) FROM notes")
    return mw.col.getNote(last_nid)

def test_import():
    def wrapper():
        card_count_before = mw.col.cardCount()
        # this might be useful, but for now we want to create a new package
        # showInfo("Card count: %d" % cardCount)

        setup_initial_if_first_time()
        p = chess_apkg_path()
        importer = AnkiPackageImporter(mw.col, p)
        try:
            importer.run()
        except Exception as e:
            showInfo(f"Error: {str(e)}, path=={p}")


        card_count_after = mw.col.cardCount()
        assert card_count_after == card_count_before +1

        note: 'Note' = get_last_added_note(mw.col)
        assert isinstance(note, Note)
        assert note, "Note assert failed"

        new_note = Note(mw.col, model=note.model())
        new_note.fields = note.fields.copy()
        deck_id = note.note_type()["did"]

        # I think we have to insert into the note.fields the new values,
        # that will be a list of chess pgn

        mw.col.add_note(new_note, deck_id)
        mw.col.save()

        make_visible_in_collection()
        # Update media database
        # mw.col.media.force_resync()


    action = QAction("test_import", mw)
    qconnect(action.triggered, wrapper)
    mw.form.menuTools.addAction(action)


test_import()



action = QAction("Import Puzzles from Lichess", mw)
qconnect(action.triggered, run_quizlet_plugin)
mw.form.menuTools.addAction(action)
