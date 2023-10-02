# openTorah

openTorah is an innovative Text User Interface (TUI) book reader designed to provide an enriched reading experience for Hebrew texts, including esteemed works such as the Hebrew Bible, Talmud, and more. It transforms your terminal into a powerful and intuitive reading platform, extending a plethora of features to enhance your interaction with the revered texts.

## Features

- **TUI Interface**: A highly interactive interface built with `rich` and `textual`, giving users a graphical experience within the terminal.
- **Text Search**: Execute fuzzy searches across all available texts swiftly using `Ctrl-P`.
- **Command Palette**: A robust command palette accessible with `Ctrl-Shift-P`, offering quick access to diverse features.
- **Translation**: Get instantaneous translations for selected Hebrew texts.
- **Bookmarking**: Easily bookmark and seamlessly navigate through your favored passages using `Ctrl-B`.
- **Offline Access & Text Management**: Manually download and access texts offline. Locally cached texts ensure speedy access.
- **Right-to-left Support**: Uninterrupted support for right-to-left Hebrew text.
- **Theming**: Customizable themes for a personalized reading experience.
- **Vim-inspired "Evil Mode"**: A modal, keyboard-centric interface inspired by Vim.
- **Cross-platform**: Compatible with Windows, Mac, and Linux.

### Keymaps and Commands

| Key Combination | Command                 | Mnemonic                        |
| --------------- | ----------------------- | ------------------------------- |
| `Ctrl-P`        | Text Search             | **P**roject/Text search         |
| `Ctrl-Shift-P`  | Command Palette         | Palette with **P**ower          |
| `Ctrl-B`        | Bookmark Current Page   | **B**ookmark                    |
| `Ctrl-S`        | Save/Download Text      | **S**ave                        |
| `Ctrl-T`        | Translate Selected Text | **T**ranslate                   |
| `Ctrl-O`        | Open Sidebar/Bookmarks  | **O**pen side panel             |
| `Ctrl-A`        | Add Highlight           | **A**dd highlight               |
| `Ctrl-R`        | Remove Highlight        | **R**emove highlight            |
| `Ctrl-N`        | Next Page               | **N**ext                        |
| `Ctrl-Shift-N`  | Previous Page           | Previous (opposite of **N**ext) |
| `Ctrl-E`        | Toggle Evil Mode        | Toggle Vim-like controls        |

## Requirements

- Python 3.8 or above
- Libraries: `rich`, `textual`, `sqlite3`, and `requests`

## Installation for Users

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/openTorah.git
   ```

2. Navigate into the directory:

   ```bash
   cd openTorah
   ```

3. Install the required Python libraries:

   ```bash
   pip install rich textual sqlite3 requests
   ```

4. Launch the application:
   ```bash
   python src/main.py
   ```

## Contribution

Contributions are warmly welcomed! If you'd like to contribute, please fork the repository and submit a pull request with your proposed features, enhancements, or bug fixes. Ensure that your code adheres to the prevailing coding standards within the project.

## License

[GNU General Public License v3.0](https://github.com/spaceCabbage/openTorah/blob/main/LICENSE)
