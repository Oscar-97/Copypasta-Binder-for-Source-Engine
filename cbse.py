"""
This module provides classes and functions for creating a graphical user interface using Tkinter.
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import telnetlib
import time
import sys


class CBSE:
    def __init__(self, master):
        self.root = master
        self.filename = None
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
        self.pick_button = self.create_button(
            button_frame, "Choose a file", self.pick_file, 0)
        self.convert_button = self.create_button(
            button_frame, "Convert to bind", self.convert, 1)
        self.download_button = self.create_button(
            button_frame, "Save as CFG", self.save_file, 2)
        self.remote_button = self.create_button(
            button_frame, "Remote", self.say_chat, 3)
        self.clear_button = self.create_button(
            button_frame, "Clear", self.clear_chat, 4)

        # Create the labels.
        self.filename_label = self.create_label("Path to selected file...", 1)
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

    def create_button(self, frame, text, command, column):
        """
        Returns a button widget.
        """
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=0, column=column, padx=5, pady=5)
        return button

    def create_label(self, text, row):
        """
        Returns a label.
        """
        label = ttk.Label(self.root, text=text)
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

    def read_file_content(self, filename):
        """
        Reads the file.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    def split_text(self, text, max_chars=110, max_words=20):
        """
        Splits the text from the provided file by a maximum of 110 chars or 20 words.
        """
        words = text.split()
        lines = []
        current_line = []
        current_chars = 0
        current_words = 0
        for word in words:
            if current_chars + len(word) + len(current_line) > max_chars \
            or current_words >= max_words:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_chars = len(word)
                current_words = 1
            else:
                current_line.append(word)
                current_chars += len(word)
                current_words += 1
        if current_line:
            lines.append(" ".join(current_line))
        return lines

    def generate_modified_sentence(self, sentence, counter, str_alias, str_spam,
                                   str_first_spam, sentences_len):
        """
        Modifes the sentence.
        """
        spam_alias = str_first_spam.format(counter)

        if sentence == sentences_len - 1:
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; \
                                {str_alias} {str_spam} {str_spam}1"'
        else:
            spam_alias_second = str_first_spam.format(counter+1)
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; \
                                {str_alias} {str_spam} {spam_alias_second}"'

        return modified_sentence

    def convert(self):
        """
        Create new sentences based on the content from the provided file.
        """
        if self.filename:
            file_content = self.read_file_content(self.filename)

            sentences = self.split_text(file_content)
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
                self.textboxchat.insert(tk.END, sentence + "\n")
                counter += 1
                modified_sentence = self.generate_modified_sentence(
                    sentence, counter, str_alias, str_spam, str_first_spam, len(sentences))
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
        tn_host = self.ip_entry.get()
        tn_port = self.port_entry.get()
        try:
            tn_connection = telnetlib.Telnet(tn_host, tn_port)
        except ConnectionRefusedError:
            error_message = "Connection Refused. Ensure that a source game is open \
                            and that you have the following launch option set: -netconport " + \
                str(tn_port)
            messagebox.showerror("Error", error_message)
            print(error_message)
            sys.exit(1)
        text_content = self.textboxchat.get("1.0", tk.END)
        lines = text_content.splitlines()
        for line in lines:
            line = "say " + line + "\n"
            line = line.encode("utf-8")
            tn_connection.write(line)
            time.sleep(2)
        print("Printed to console.")

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
