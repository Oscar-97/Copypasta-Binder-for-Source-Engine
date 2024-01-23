# Copypasta Binder for Source Engine

<p align="center">
<img src="./resources/preview.png" alt="Copypasta Binder for Source Engine Preview"/>
</p>

CBSE is a utility tool designed for the Source Engine games. It allows players to easily convert text files into bindable .cfg files, facilitating in-game communication by enlightening the mood via copypastas.

# Installation

Activate a virtual environment, install the dependencies, and run the `python main.py` command to start the program. Alternatively, download the executable from the releases tab and run it.

1. Clone the repository (Optional):

   ```
   git clone https://github.com/Oscar-97/Copypasta-Binder-for-Source-Engine.git
   cd Copypasta-Binder-for-Source-Engine
   ```

2. Set up a Virtual Environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install Dependencies:

   ```
   pip install -r requirements.txt
   ```

# Usage

## 1. Start the program

- Run the program using Python:

  ```
  python main.py
  ```

- Or download the executable from the releases tab and run it.

## 2. Using the GUI

- Select a text file and press convert to bind.
- Click on `Save as CFG` button.
- Enter a name and save the `.cfg` file to `...\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg`.
- Manually modify the bound button or other preferences by opening the `.cfg` file.

## 3. In-Game Usage:

- Press the "INSERT" button to start spamming line by line.
- ~~Alternatively, set -netconport `<number>` in the startup options along with host and port in the application to automatically spam in-game. Click the remote button to start the process.~~ Not available in CS2 yet :(

# Customization

Modify the `split_text` function in `cbse_functions.py` to adjust the maximum number of characters and the word length according to your preferences.

# Why would you need a GUI for this?

Would it have been sufficient to have no GUI at all? Certainly, this was created mainly to tinker with tkinter and explore its features, while using the [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme).

# Building from Source

A specification file is provided for building the project with PyInstaller.

```
pyinstaller CBSE.spec
```

# Contributions

Feel free to submit pull requests, open issues, or suggest features.
