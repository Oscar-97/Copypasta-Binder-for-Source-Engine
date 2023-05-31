import tkinter as tk
from cbse import CBSE
import sv_ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("test.ico")
    root.title("Copypasta Binder for Source Engine")
    sv_ttk.use_dark_theme()
    app = CBSE(root)
    app.run()