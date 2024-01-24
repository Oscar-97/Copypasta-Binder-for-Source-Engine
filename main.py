"""
CBSE GUI project.
"""
import os
import sys
import tkinter
import sv_ttk
from utils.cbse import CBSE


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS  # pylint: disable=protected-access
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = tkinter.Tk()
    icon_path = resource_path("resources/cbse.ico")
    root.iconbitmap(icon_path)
    root.title("Copypasta Binder for Source Engine")
    root.resizable(False, False)
    root.attributes('-topmost', True)
    sv_ttk.set_theme("dark")
    app = CBSE(root)
    app.run()
