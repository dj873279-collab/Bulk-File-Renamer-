# Bulk File Renamer

A simple desktop application built using **Python and Tkinter** that makes renaming multiple files faster and easier.

The application allows users to select a folder, enter a custom filename prefix, and automatically rename all files using sequential numbering (001, 002, 003, etc.). It also provides a live preview of the new filenames before applying changes and preserves the original file extensions.

## Features

- **Folder Selection:** Select a folder containing the files you want to rename.
- **Custom Prefix:** Add a custom prefix to all filenames.
- **Sequential Numbering:** Automatically assign numbers in sequence (001, 002, 003...).
- **Live Preview:** View original and updated filenames side by side before renaming.
- **Extension Preservation:** Retain original file extensions such as .pdf, .jpg, .docx, etc.
- **Confirmation Before Renaming:** Confirm the operation before making changes.
- **Directory Filtering:** Automatically exclude subfolders and process files only.

## Real-World Application: College Professors and Faculty

College professors and faculty members frequently handle large numbers of academic files, including assignments, examination papers, student submissions, lecture materials, and project reports.

This application can help professors organize these files more efficiently by renaming them in a consistent sequence.

**Example:**

A professor downloads multiple student assignment submissions with inconsistent filenames.

Original filenames:
- assignment_final.pdf
- submission_new.pdf
- document123.pdf

After using Bulk File Renamer with the prefix `DSA_Assignment_`:

- DSA_Assignment_001.pdf
- DSA_Assignment_002.pdf
- DSA_Assignment_003.pdf

This makes files easier to identify, organize, and manage.

Other potential users include students, researchers, administrative staff, and anyone who regularly manages large collections of digital files.

## Technologies Used

- Python
- Tkinter – Graphical User Interface
- OS Module – File and directory operations

## How to Run

1. Clone this repository.
2. Make sure Python is installed.
3. Navigate to the project directory.
4. Run the following command:

```bash
python bulk_renamer.py
```

No additional Python packages are required because the application uses built-in Python libraries.

## Project Objective

The objective of this project is to develop a simple, user-friendly desktop application that automates repetitive file-renaming tasks while demonstrating the practical use of Python programming, GUI development, and file-handling operations.
