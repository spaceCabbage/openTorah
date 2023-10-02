# HebrewTUIReader TODO List

## Directory Structure
```
HebrewTUIReader/
│
├── src/
│ ├── main.py
│ ├── app/
│ │ ├── init.py
│ │ ├── window.py
│ │ ├── widgets.py
│ │ ├── events.py
│ │ └── command_palette.py
│ │
│ ├── database/
│ │ ├── init.py
│ │ ├── db_interface.py
│ │ └── schema.sql
│ │
│ ├── translations/
│ │ ├── init.py
│ │ └── translator.py
│ │
│ ├── texts/
│ │ ├── init.py
│ │ ├── text_loader.py
│ │ └── text_downloader.py
│ │
│ └── utils/
│ ├── init.py
│ └── rtl_support.py
│
├── data/
│ ├── sefarim/
│ └── db/
└── README.md
```


## App Features

### Keymaps and Commands

| Key Combination | Command                  | Mnemonic (if any)           |
|-----------------|--------------------------|-----------------------------|
| `Ctrl-P`        | Text Search              | **P**roject/Text search     |
| `Ctrl-Shift-P`  | Command Palette          | Palette with **P**ower      |
| `Ctrl-B`        | Bookmark Current Page    | **B**ookmark                |
| `Ctrl-S`        | Save/Download Text       | **S**ave                    |
| `Ctrl-T`        | Translate Selected Text  | **T**ranslate               |
| `Ctrl-O`        | Open Sidebar/Bookmarks   | **O**pen side panel         |
| `Ctrl-A`        | Add Highlight            | **A**dd highlight           |
| `Ctrl-R`        | Remove Highlight         | **R**emove highlight        |
| `Ctrl-N`        | Next Page                | **N**ext                    |
| `Ctrl-Shift-N`  | Previous Page            | Previous (opposite of **N**ext) |


### TUI Interface

- [ ] **Set up main interface**:
    - [ ] Design the landing page of the application.
    - [ ] Add menu and navigation controls.

### Text Search

- [ ] **Implement text searching**:
    - [ ] Load available texts.
    - [ ] Use fuzzy search to filter results as the user types.
    - [ ] Highlight matched texts.
    - [ ] Navigate to the selected text when chosen.

### Command Palette

- [ ] **Develop command palette**:
    - [ ] Display list of available commands.
    - [ ] Allow filtering of commands by typing.
    - [ ] Execute selected command when chosen.

### Translation

- [ ] **Add translation functionality**:
    - [ ] Highlight desired text for translation.
    - [ ] Fetch translation using integrated translation service.
    - [ ] Display translation in a pop-up or side panel.

### Bookmarking

- [ ] **Implement bookmarking**:
    - [ ] Allow users to bookmark a particular text or page.
    - [ ] Store bookmarks in SQLite database.
    - [ ] Display list of bookmarks in a side panel or separate view.
    - [ ] Navigate to bookmarked text when selected from the list.

### Offline Access & Text Management

- [ ] **Manage text storage and caching**:
    - [ ] Load text from GitHub repo or local storage.
    - [ ] Cache loaded texts to reduce loading time for subsequent access.
    - [ ] Update cached texts when newer versions are available.

### Right-to-left Support

- [ ] **Ensure RTL Hebrew text support**:
    - [ ] Implement RTL text rendering.
    - [ ] Ensure all interface elements and text respect RTL layout.

### Sidebar Design

- [ ] **Implement a Sidebar**:
    - [ ] Design a retractable sidebar that can be toggled with `Ctrl-O`.
    - [ ] Display a list of loaded texts, bookmarks, highlights, and available themes.
    - [ ] Enable quick navigation: Clicking on a loaded text/bookmark should navigate the user to that specific text/page.
    - [ ] Integrate search functionality within the sidebar to find specific bookmarks or highlights.
    - [ ] Display metadata of the currently opened text (like author, date, etc.) at the top.

### Command Palette Design

- [ ] **Develop an Advanced Command Palette**:
    - [ ] Trigger command palette with `Ctrl-Shift-P`.
    - [ ] List all available commands with their descriptions and associated shortcuts.
    - [ ] Implement a search bar within the palette for faster command access.
    - [ ] Enable command execution directly from the palette.
    - [ ] Allow users to customize the order of commands based on their frequency of use.

### Themes

- [ ] **Implement Theming**:
    - [ ] Design a default light and dark theme.
    - [ ] Allow users to switch between themes via the sidebar or command palette.
    - [ ] Load themes: Use separate configuration files for each theme, specifying colors, fonts, and other UI elements.
    - [ ] Enable user-defined themes: Allow users to create, import, and export their themes.

### "Evil Mode" (Vim-like Controls)

- [ ] **Incorporate Vim-inspired Controls**:
    - [ ] Enable a mode that users can toggle on/off for Vim-like controls (maybe `Ctrl-E` to toggle evil mode).
    - [ ] Implement basic Vim navigation keys:
        - `h` for left, `j` for down, `k` for up, `l` for right.
        - `w` to jump forward by word, `b` to jump backward by word.
    - [ ] `gg` to go to the beginning of the text, `G` to go to the end.
    - [ ] Integrate Vim-like visual mode where a user can select text to be translated or copied.
    - [ ] Allow users to customize and extend Vim key bindings, if desired.
    - [ ] Provide a quick reference guide within the command palette for all Vim commands available in "Evil Mode."

## Initialization Process

- [ ] Design and implement the `install.py` script for automated setup.
- [ ] Check & install necessary Python version and libraries: `rich`, `textual`, `sqlite3`, `requests`.
- [ ] Verify and install a suitable Hebrew-supporting font for optimal display.
- [ ] Create and initialize SQLite database with tables for bookmarks, highlights, and other metadata.
- [ ] Implement a step-by-step interactive tutorial for first-time users, with an option to skip and access later.
- [ ] Ensure proper rendering and support for Hebrew texts, providing troubleshooting steps if issues are detected.
- [ ] Allow downloading and caching of core Hebrew texts for offline use.
- [ ] Inform users of successful setup and provide quick reference or link to project README.

## Start Page / Dashboard

- [ ] Design a welcoming and functional start page/dashboard.
- [ ] List of key sections for quick access:
  - [ ] Torah
  - [ ] Talmud
  - [ ] Psalms
  - [ ] Siddur
  - [ ] Rishonim
- [ ] Showcase recent locations for quick reading resumption.
- [ ] Display latest bookmarks, allowing users to directly jump to them.
- [ ] Quick access to the command palette.
- [ ] Integrate a search bar at the top for direct text searches or command executions.
- [ ] Highlight any project updates, news, or additional resources that users might find useful.

