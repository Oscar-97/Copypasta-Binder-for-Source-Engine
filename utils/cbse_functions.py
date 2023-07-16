"""
Functions for CBSE, does not have GUI related functions.
"""
import sys
import time
import telnetlib
import tkinter as tk
from tkinter import messagebox


class CBSEFunctions:
    """
    Functions for CBSE.
    """

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
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; {str_alias} {str_spam} {str_spam}1"'
        else:
            spam_alias_second = str_first_spam.format(counter+1)
            modified_sentence = f'{str_alias} "{spam_alias}" "say {sentence.strip()}; {str_alias} {str_spam} {spam_alias_second}"'

        return modified_sentence

    def say_chat(self, ip_entry, port_entry, textboxchat):
        """
        Connects over telnet att sends the file content as a text message in allchat.
        """
        tn_host = ip_entry.get()
        tn_port = port_entry.get()
        try:
            tn_connection = telnetlib.Telnet(tn_host, tn_port)
        except ConnectionRefusedError:
            error_message = "Connection Refused. Ensure that a source game is open " \
                            "and that you have the following launch option set: -netconport " \
                            + str(tn_port)
            messagebox.showerror("Error", error_message)
            print(error_message)
            sys.exit(1)
        text_content = textboxchat.get("1.0", tk.END)
        lines = text_content.splitlines()
        for line in lines:
            line = "say " + line + "\n"
            line = line.encode("utf-8")
            tn_connection.write(line)
            time.sleep(2)
        print("Printed to console.")
