import os
from pathlib import Path

from aqt import mw


def media_files_path():
    """ Files are required by this dynamically playable chess Anki deck.

    The directory is also named 'collections.media', and it's contents
    shall be copied into the Anki collection's media folder up installation.
    """
    addon_folder = addon_dir()
    user_files = os.path.join(addon_folder, "user_files")
    return os.path.join(user_files, "collection.media")

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

def refresh_ui():
    mw.reset()