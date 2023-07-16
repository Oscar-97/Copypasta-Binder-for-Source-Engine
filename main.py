"""
CBSE project in progress.
"""
import tkinter as tk
import sv_ttk
from cbse import CBSE


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("test.ico")
    root.title("Copypasta Binder for Source Engine")
    sv_ttk.use_dark_theme()
    app = CBSE(root)
    app.run()
