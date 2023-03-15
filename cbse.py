import tkinter as tk
from tkinter import filedialog
import sv_ttk

class CBSE:
    def __init__(self, master):
        self.root = master
        self.filename = None

       # Create a frame to hold the buttons.
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        # Choose file button.
        self.pick_button = tk.Button(
            button_frame, text="Choose a file", command=self.pick_file)
        self.pick_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W)

        # Filename button.
        self.filename_label = tk.Label(master)
        self.filename_label.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Convert button.
        self.convert_button = tk.Button(
            button_frame, text="Convert to bind", command=self.convert)
        self.convert_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W)

        # Download button.
        self.download_button = tk.Button(
            button_frame, text="Save as CFG", command=self.save_file)
        self.download_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W)

        # Text box field.
        self.textbox = tk.Text(master, height=50, width=100, wrap='word')
        self.textbox.pack()

        sv_ttk.set_theme("dark")

    def pick_file(self):
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)

    def read_file_content(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def split_text(self, text, max_chars=50, max_words=10):
        words = text.split()
        lines = []
        current_line = []
        current_chars = 0
        current_words = 0
        for word in words:
            if current_chars + len(word) + len(current_line) > max_chars or current_words >= max_words:
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

    def generate_modified_sentence(self, sentence, counter, str_alias, str_spam, str_first_spam, sentences_len):
        spam_alias = str_first_spam.format(counter)

        if sentence == sentences_len - 1:
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; {str_alias} {str_spam} {str_spam}1"'
        else:
            spam_alias_second = str_first_spam.format(counter+1)
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; {str_alias} {str_spam} {spam_alias_second}"'

        return modified_sentence

    def convert(self):
        if self.filename:
            file_content = self.read_file_content(self.filename)

            sentences = self.split_text(file_content)
            str_alias = "alias"
            str_spam = "boko"
            str_first_spam = str_spam + "{}"
            bind_button = f'bind "INS" "{str_spam}"'
            first_alias = f'{str_alias} "{str_spam}" "{str_spam}1"'
            counter = 0

            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, bind_button + "\n")
            self.textbox.insert(tk.END, first_alias + "\n")

            for i, sentence in enumerate(sentences):
                counter += 1
                modified_sentence = self.generate_modified_sentence(
                    sentence, counter, str_alias, str_spam, str_first_spam, len(sentences))
                self.textbox.insert(tk.END, modified_sentence + "\n")
        else:
            self.filename_label.config(text="No selected file.")

    def save_file(self):
        text_content = self.textbox.get("1.0", tk.END)
        filename = tk.filedialog.asksaveasfilename(defaultextension=".cfg")
        with open(filename, "w") as f:
            f.write(text_content)

    def run(self):
        self.root.mainloop()