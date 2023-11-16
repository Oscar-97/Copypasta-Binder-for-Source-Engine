"""
This module provides classes and functions for creating a graphical user interface using Tkinter.
"""
import tkinter as tk
from tkinter import ttk, filedialog
from utils.cbse_functions import CBSEFunctions

cbse_functions = CBSEFunctions()


class CBSE:
    """
    GUI setup.
    """

    def __init__(self, master):
        self.root = master
        self.filename = None
        self.buttons = None
        self.filename_label = None
        self.labelfile = None
        self.labelremote = None
        self.textbox = None
        self.textboxchat = None
        self.ip_entry = None
        self.port_entry = None
        self.setup_ui()

    def setup_ui(self):
        """
        Main setup of the UI.
        """
        # Create a frame to hold the buttons.
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=0, sticky='ew')

        ip_port_frame = ttk.Frame(self.root)
        ip_port_frame.grid(row=7, padx=5, pady=5, sticky='ew')

        # Create the buttons.
        self.buttons = self.create_buttons(button_frame)

        # Create the labels.
        self.filename_label = self.create_label(
            "Path to selected file...", 1, ("Calibri", 12, "italic"))
        self.labelfile = self.create_label("CFG Content", 3)
        self.labelremote = self.create_label("Direct Chat In-game", 5)

        # Create the textboxes.
        self.textbox = self.create_textbox(4)
        self.textboxchat = self.create_textbox(6)

        self.ip_entry = self.create_entry(
            ip_port_frame, 0, 0, "192.168.1.220", width=40)
        self.port_entry = self.create_entry(
            ip_port_frame, 0, 1, "2024", width=5)

        ip_port_frame.grid_columnconfigure(0, weight=85)
        ip_port_frame.grid_columnconfigure(1, weight=15)

    def create_buttons(self, frame):
        """
        Create the five buttons at the 
        """
        buttons = {}
        button_specs = [
            ("Choose a file", self.pick_file, 0),
            ("Convert to bind", self.convert, 1),
            ("Save as CFG", self.save_file, 2),
            ("Remote", self.say_chat, 3),
            ("Clear", self.clear_chat, 4)
        ]
        for text, command, column in button_specs:
            button = self.create_button(frame, text, command, column)
            buttons[text] = button
        return buttons

    def create_button(self, frame, text, command, column):
        """
        Returns a button widget.
        """
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=0, column=column, padx=5, pady=5)
        return button

    def create_label(self, text, row, custom_font=("Calibri", 12, "normal")):
        """
        Returns a label.
        """
        label = ttk.Label(self.root, text=text, font=custom_font)
        label.grid(row=row, padx=5, pady=5, sticky='ew')
        return label

    def create_textbox(self, row):
        """
        Returns a textbox.
        """
        textbox = tk.Text(self.root, height=10, width=60,
                          wrap='word', borderwidth=2, relief="flat")
        textbox.grid(row=row, padx=5, pady=5, sticky='ew')
        textbox.configure(background="#262626")
        return textbox

    def create_entry(self, frame, row, column, placeholder, width=None):
        """
        Returns a entry field.
        """
        entry = ttk.Entry(frame, width=width)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky='ew')
        entry.insert(0, placeholder)
        return entry

    def pick_file(self):
        """
        Returns a file picker dialog.
        """
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)

    def convert(self):
        """
        Create new sentences based on the content from the provided file.
        """
        if self.filename:
            file_content = cbse_functions.read_file_content(self.filename)

            sentences = cbse_functions.split_text(file_content)
            str_alias = "alias"
            str_spam = "spam"
            str_first_spam = str_spam + "{}"
            bind_button = f'bind "INS" "{str_spam}"'
            first_alias = f'{str_alias} "{str_spam}" "{str_spam}1"'
            counter = 0

            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, bind_button + "\n")
            self.textbox.insert(tk.END, first_alias + "\n")

            self.textboxchat.delete("1.0", tk.END)

            for sentence in enumerate(sentences):
                print(sentence)
                self.textboxchat.insert(tk.END, sentence[1] + "\n")
                counter += 1
                modified_sentence = cbse_functions.generate_modified_sentence(
                    sentence[1], counter, str_alias, str_spam, str_first_spam, len(sentences))
                self.textbox.insert(tk.END, modified_sentence + "\n")
        else:
            self.filename_label.config(text="No selected file.")

    def save_file(self):
        """
        Save the current content as a cfg file.
        """
        text_content = self.textbox.get("1.0", tk.END)
        filename = tk.filedialog.asksaveasfilename(defaultextension=".cfg")
        with open(filename, "w", encoding='utf-8') as f:
            f.write(text_content)

    def say_chat(self):
        """
        Connects over telnet att sends the file content as a text message in allchat.
        """
        cbse_functions.say_chat(
            self.ip_entry, self.port_entry, self.textboxchat)

    def clear_chat(self):
        """
        Clear chat window.
        """
        self.textbox.delete("1.0", tk.END)
        self.textboxchat.delete("1.0", tk.END)
        self.filename_label.config(text='')

    def run(self):
        """
        Set to loop.
        """
        self.root.mainloop()
