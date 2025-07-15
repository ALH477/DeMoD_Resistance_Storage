Resistance Storage Project

xAI Artifact: This entire project, including all modules and documentation, was designed, refined, and generated with assistance from Grok by xAI. It was made by DeMoD LLC with Grok 4.
Overview
An open-source project for encoding digital data (e.g., music, text) as physical resistances in PCB or ASIC designs. Features modular parsing, optional encryption, quality checks, and a terminal-like TUI.
Installation Directions by OS
Linux / macOS

Clone the repository or download the project files.
Open a terminal in the project root directory.
Make the CLI script executable: chmod +x scripts/resistance_cli.sh
Install: ./scripts/resistance_cli.sh install
Start: ./scripts/resistance_cli.sh start

Windows

Clone the repository or download the project files.
Use Git Bash (install Git if needed: https://git-scm.com/downloads) or WSL (Windows Subsystem for Linux).
In Git Bash or WSL terminal, navigate to the project root directory.
Run: bash scripts/resistance_cli.sh install
Start: bash scripts/resistance_cli.sh start
Note: If using PowerShell, adapt the script or run in Git Bash for best compatibility.



If extraction fails (e.g., awk not available on Windows without Git Bash), manually copy code blocks from the full project documentation to files.
Project Structure

src/: Contains the main Python modules.
binary_parser.py: Modular file parser to bitstream with parity.
cipher.py: Optional encryption module with ciphers like Caesar and Vigenère.
quality_check.py: Module for parity validation and corruption simulation.
tui.py: Text User Interface using Textual, simulating a terminal.


scripts/: Contains the bash CLI script.
resistance_cli.sh: CLI for installation and starting the TUI.


docs/: Contains this README.md file.
requirements.txt: Lists the dependencies (e.g., textual).

TUI Library Comparison



Library
Pros
Cons
Suitability for Project



ncurses (curses)
Standard, efficient, low-level control.
Steep learning curve, no mouse support by default, platform-dependent.
Good for simple terminals but overkill for our interactive needs.


Urwid
Widget-based, event loop, mouse support.
Older API, less modern styling, complex for beginners.
Viable for console apps, but less aesthetic than modern alternatives.


Textual (chosen)
Built on Rich, async, beautiful UIs, easy widgets.
Heavier (depends on Rich), newer so less mature in some areas.
Ideal for our project: Interactive file input, buttons for generation, visual feedback.


Picotui
Lightweight, pure-Python, no deps, simple.
Basic features, no advanced widgets, limited refresh optimization.
Great for minimalism, but lacks polish for user-friendly TUI.


Pytermgui
Modular widgets, mouse support, customizable.
Less community, potential bugs in edge cases.
Strong alternative to Textual if needing more customization without async.


Usage

After installation, use the TUI for interactive commands (parse, encrypt, quality check).
Modules can be imported in Python scripts for custom use.

License
MIT
Contributing
PRs welcome! Add parsers, ciphers, or TUI features.
