# 📂 FolderFlow

**FolderFlow** is a lightweight and customizable **command-line file organizer** that automatically sorts files into categorized folders based on their extensions.

---

## 🚀 Features

- 🔍 Detects and moves files by type (Images, Videos, Documents, Music, Archives, etc.)
- 📁 Creates folders automatically if they don't exist
- 📝 Optional logging to a `log.txt` file for tracking actions
- 💻 Easy-to-use command-line interface with helpful flags
- ⚡️ Fast and cross-platform (Windows, Linux, macOS)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/folderflow.git
cd folderflow
```

2. Install the CLI tool locally:
```bash
pip install .
```

## ⚙️ Usage

### 🔧 Basic Command
Organize files in a directory:
```bash
folderflow --path "E:/Downloads"
```

### 📝 With Logging
Enable logging to track moved files:
```bash
folderflow --path "E:/Downloads" --log true
```

### 🗂️ Custom Folder Names
Specify custom folder names for file types:
```bash
folderflow --path "E:/Downloads" --images "Photos" --documents "Docs"
```

### 🆘 Help Command
Display all available options:
```bash
folderflow --help
```

# 🗃️ Example

### Before running:
```
E:/Downloads/
├── song.mp3
├── picture.jpg
├── doc.pdf
├── archive.zip
├── script.py
```

### After running:
```
E:/Downloads/
├── Music/
│   └── song.mp3
├── Images/
│   └── picture.jpg
├── Documents/
│   └── doc.pdf
├── Archives/
│   └── archive.zip
├── Code/
│   └── script.py
```
---
### Example with Custom Folder Names:
Command:
```bash
folderflow --path "E:/Downloads" --images "Photos" --documents "Docs"
```
Result:
```
E:/Downloads/
├── Music/
│   └── song.mp3
├── Photos/
│   └── picture.jpg
├── Docs/
│   └── doc.pdf
├── Archives/
│   └── archive.zip
├── Code/
│   └── script.py
```
---