# Smart File Organizer

A Python automation script that organizes files into categorized folders automatically.

## Features

- Organizes Images
- Organizes Documents
- Organizes Videos
- Organizes Music
- Organizes Archives
- Places unknown files into an Others folder

## Technologies Used

- Python
- os module
- shutil module

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/smart-file-organizer.git
```

Move into the project:

```bash
cd smart-file-organizer
```

Run:

```bash
python organizer.py
```

## Example

Before:

Downloads/

- report.pdf
- movie.mp4
- song.mp3
- image.jpg

After:

Downloads/

├── Documents/
│   └── report.pdf

├── Videos/
│   └── movie.mp4

├── Music/
│   └── song.mp3

└── Images/
    └── image.jpg

## Future Enhancements

- GUI with Tkinter
- Auto-organize every hour
- Duplicate file detection
- Log file generation

## License

MIT
