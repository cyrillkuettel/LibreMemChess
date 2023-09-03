import os
import tempfile
import zipfile
import sqlite3
from pathlib import Path


def addon_dir():
    from aqt.profiles import ProfileManager
    profile_manager = ProfileManager(
        ProfileManager.get_created_base_folder(path_override=None)
    )
    addon_folder = Path(profile_manager.addonFolder()) / "LibreMemChess"
    return addon_folder

def chess_apkg_path():
    addon_folder = addon_dir()
    user_files = os.path.join(addon_folder, "user_files")
    return os.path.join(user_files, "chess.apkg")



def get_single_note(file, temporary_directory: str):
    """
    # 1. read the apkg file
    # 2. find the note that is the only note in the deck
    # 3. inspect this note, so we can clone it and create it programmatically
    """

    # 1. Read the apkg file
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(temporary_directory)

    # 2. Connect to the SQLite database
    conn = sqlite3.connect(f"{temporary_directory}/collection.anki21")
    cursor = conn.cursor()

    # 3. Find the only note in the deck and inspect it
    cursor.execute(
        "SELECT id, flds FROM notes WHERE id = (SELECT nid FROM notes LIMIT 1)")
    note = cursor.fetchone()

    conn.close()
    return note


def test_read_anki_deck():


    chess_apkg = chess_apkg_path()
    assert os.path.isfile(chess_apkg)
    return

    # use namedtemporaryfile: temp dir:
    with tempfile.TemporaryDirectory() as tmp:

        note = get_single_note(chess_apkg, tmp)
        assert note


