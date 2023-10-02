# HebrewTUIReader

A Text User Interface (TUI) book reader for Hebrew texts, including the Hebrew Bible, Talmud, and more. The reader provides a seamless terminal-based reading experience, complete with text search, translation, bookmarking, and other essential features.

## Features

- **TUI Interface**: Built using `rich` and `textual`, offering a GUI-like experience within the terminal.
- **Text Search**: Fuzzy searching across all texts using `Ctrl-P`.
- **Command Palette**: A quick access palette for features using `Ctrl-Shift-P`.
- **Translation**: Instant translation for selected texts.
- **Bookmarking**: Save and quickly navigate to your favorite passages.
- **Offline Access**: Download texts for offline reading. Texts are cached locally for quick access.
- **Right-to-left Support**: Complete support for the right-to-left Hebrew text.
- **Cross-platform**: Available for Windows, Mac, and Linux.

## Requirements

- Python 3.8 or above
- Libraries: `rich`, `textual`, `sqlite3`, and `requests`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/HebrewTUIReader.git
    ```

2. Change directory:
    ```bash
    cd HebrewTUIReader
    ```

3. Install the required Python libraries:
    ```bash
    pip install rich textual sqlite3 requests
    ```

4. Run the app:
    ```bash
    python src/main.py
    ```

## Development

### Directory Structure

Provide a brief overview of the main directories and their purpose.

### Database

Explain the schema of the SQLite database and its main tables for bookmarks and highlights.

### Text Management

Detail how texts are loaded, cached, and stored for offline access.

### Command Palette and Widgets

Discuss the command palette's implementation, associated shortcuts, and other TUI widgets.

## Contribution

Open for contributions! Please fork the repository and submit a pull request for any features, enhancements, or bug fixes.

## License

[Your preferred license, e.g., MIT]

