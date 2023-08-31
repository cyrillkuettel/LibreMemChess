import os
import tempfile
import zipfile
import sqlite3
from anki.collection import _Collection

def read_anki_deck(file, temporary_directory):
    """
    # 1. read the apkg file
    # 2. find the note that is the only note in the deck
    # 3. inspect this note, so we can clone it and create it programmatically
    """

    # 1. Read the apkg file
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(temporary_directory)

    # 2. Connect to the SQLite database
    conn = sqlite3.connect("anki_deck/collection.anki2")
    cursor = conn.cursor()

    # 3. Find the only note in the deck and inspect it
    cursor.execute(
        "SELECT * FROM notes WHERE id = (SELECT nid FROM cards LIMIT 1)")
    note = cursor.fetchone()

    # Close the connection
    conn.close()

    return note


def test_read_anki_deck():


    CURRENT = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(CURRENT)
    templates_path = os.path.join(parent_directory, "template")
    chess_apkg = os.path.join(templates_path, "chess.apkg")


    # use namedtemporaryfile: temp dir:
    with tempfile.TemporaryDirectory() as tmp:

        read_anki_deck(chess_apkg, tmp)


    # deck = read_anki_deck("..//test_deck.apkg")

    #
    # assert len(deck) == 2
    # assert deck[0].front == "front1"
    # assert deck[0].back == "back1"
    # assert deck[1].front == "front2"
    # assert deck[1].back == "back2"
