
# **foldorg** 📂

**Auto-Organize Downloads Folder**

A Python script to automatically organize your **Downloads** folder by categorizing files into subfolders based on their file types. This script helps you keep your Downloads folder clean and clutter-free.

---

## **Features** ✨

- 🖼️ **Automatically categorizes files** into folders like:
  - **Images**
  - **Documents**
  - **Videos**
  - **Music**
  - **Archives**
  - **Executables**
  - **Code**
  - **Others**
- 🚫 **Ignores hidden files and directories**.
- ⚠️ **Prevents overwriting files** with the same name in the destination folder.
- 🛠️ **Easy to customize** and extend with additional file types or categories.

---

## **How to Use** 🚀

1. **Install Python**: Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your system.
2. **Download the Script**: Save the [`auto_organize_downloads.py`](auto_organize_downloads.py) script to your computer.
3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script using the command:
     ```bash
     python auto_organize_downloads.py
     ```
4. **Schedule the Script (Optional)**:
   - **On Windows**: Use **Task Scheduler** to run the script periodically.
   - **On macOS/Linux**: Use **`cron`** to schedule the script.

---

## **Customization** 🛠️

- **Add More File Types**: Edit the `CATEGORIES` dictionary in the script to include additional file extensions.
- **Change the Downloads Folder Path**: Modify the `DOWNLOADS_PATH` variable if your Downloads folder is located elsewhere.

---

## **Example** 📂

### Before:
```
Downloads/
├── image1.jpg
├── document1.pdf
├── video1.mp4
├── music1.mp3
├── archive1.zip
```

### After Running the Script:
```
Downloads/
├── Images/
│   └── image1.jpg
├── Documents/
│   └── document1.pdf
├── Videos/
│   └── video1.mp4
├── Music/
│   └── music1.mp3
├── Archives/
│   └── archive1.zip
```

---

## **Contributing** 🤝

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are welcome!

---

Enjoy a cleaner Downloads folder! 🎉
