"""
CBSE GUI project.
"""
import tkinter as tk
import sv_ttk
from utils.cbse import CBSE


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("resources/test.ico")
    root.title("Copypasta Binder for Source Engine")
    sv_ttk.use_dark_theme()
    app = CBSE(root)
    app.run()
