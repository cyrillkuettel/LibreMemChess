import os

from aqt import mw


def media_files_path():
    """ Media files are required by the chess.apkg. Anki deck.
    They contain the chess pieces and board (javascript + html)."""
    CURRENT = os.path.dirname(os.path.abspath(__file__))
    user_files = os.path.join(CURRENT, "user_files")
    return os.path.join(user_files, "collection.media")

def refresh_ui():
    mw.reset()