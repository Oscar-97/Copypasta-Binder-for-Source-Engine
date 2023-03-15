import tkinter as tk
from tkinter import filedialog
import sv_ttk
from cbse import CBSE

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("./test.ico")
    root.title("Copypasta Binder for Source Engine")
    app = CBSE(root)
    app.run()