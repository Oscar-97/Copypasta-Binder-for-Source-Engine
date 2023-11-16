# Copypasta Binder for Source Engine

<p align="center">
<img src="./resources/preview.png" />
</p>

## Instructions

Activate a virtual environment, install the dependencies, and run the `python main.py` command to start the program.

Follow the GUI prompts to use the program, select a text file and press convert to bind. Save the .cfg file to `...\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg` and run it in game.

~~Alternatively, set -netconport `<number>` in the startup options along with host and port in the application to automatically spam in-game. Click the remote button to start the process.~~ Not available in CS2.

Adjust the maximum number of characters and the word length to your liking by modifying the `split_text` function in `cbse_functions.py`.

---

Would it have been sufficient to have no GUI at all? Certainly, this was created mainly to tinker with tkinter and explore its features, while using the [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme).
