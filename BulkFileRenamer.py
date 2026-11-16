import os
import tkinter as tk
from tkinter import filedialog, messagebox

class BulkFileRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk File Renamer")
        self.root.geometry("600x420")
        self.folder_path = ""
        self.files = []

        # Top Section: Folder Picker
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack(fill="x", padx=15)

        tk.Button(top_frame, text="1. Select Folder", command=self.select_folder, bg="#2980b9", fg="white").pack(side="left")
        self.folder_label = tk.Label(top_frame, text="No folder selected", fg="gray")
        self.folder_label.pack(side="left", padx=10)

        # Middle Section: Prefix Input
        mid_frame = tk.Frame(root, pady=5)
        mid_frame.pack(fill="x", padx=15)

        tk.Label(mid_frame, text="2. New Prefix:").pack(side="left")
        self.prefix_entry = tk.Entry(mid_frame, width=30)
        self.prefix_entry.insert(0, "Document_")
        self.prefix_entry.pack(side="left", padx=10)
        # Update preview live whenever the user types
        self.prefix_entry.bind("<KeyRelease>", self.update_preview)

        # Preview Section: Side-by-Side Listboxes
        preview_frame = tk.Frame(root, pady=10)
        preview_frame.pack(expand=True, fill="both", padx=15)

        left_box = tk.Frame(preview_frame)
        left_box.pack(side="left", expand=True, fill="both", padx=(0, 5))
        tk.Label(left_box, text="Current Filenames", font=("Arial", 10, "bold")).pack(anchor="w")
        self.old_listbox = tk.Listbox(left_box)
        self.old_listbox.pack(expand=True, fill="both")

        right_box = tk.Frame(preview_frame)
        right_box.pack(side="right", expand=True, fill="both", padx=(5, 0))
        tk.Label(right_box, text="Live Preview (New Names)", font=("Arial", 10, "bold")).pack(anchor="w")
        self.new_listbox = tk.Listbox(right_box, fg="#27ae60")
        self.new_listbox.pack(expand=True, fill="both")

        # Bottom Section: Action Button
        tk.Button(
            root, text="3. Apply Rename", command=self.rename_files,
            bg="#27ae60", fg="white", font=("Arial", 11, "bold"), pady=5
        ).pack(pady=10)

    def select_folder(self):
        selected = filedialog.askdirectory()
        if not selected:
            return
        self.folder_path = selected
        self.folder_label.config(text=self.folder_path, fg="black")
        self.load_files()

    def load_files(self):
        # Filter out subdirectories so only files are renamed
        self.files = [
            f for f in os.listdir(self.folder_path)
            if os.path.isfile(os.path.join(self.folder_path, f))
        ]
        self.files.sort()
        self.update_preview()

    def update_preview(self, event=None):
        self.old_listbox.delete(0, tk.END)
        self.new_listbox.delete(0, tk.END)
        prefix = self.prefix_entry.get().strip()

        for index, filename in enumerate(self.files, start=1):
            _, extension = os.path.splitext(filename)
            # Pad numbers like 001, 002 for clean sorting
            new_name = f"{prefix}{index:03d}{extension}"
            self.old_listbox.insert(tk.END, filename)
            self.new_listbox.insert(tk.END, new_name)

    def rename_files(self):
        if not self.files:
            messagebox.showwarning("Warning", "Please select a folder with files first.")
            return

        new_names = self.new_listbox.get(0, tk.END)
        confirm = messagebox.askyesno("Confirm Rename", f"Rename {len(self.files)} files? This cannot be undone.")
        if not confirm:
            return

        try:
            for old_name, new_name in zip(self.files, new_names):
                old_path = os.path.join(self.folder_path, old_name)
                new_path = os.path.join(self.folder_path, new_name)
                os.rename(old_path, new_path)
            messagebox.showinfo("Success", "All files renamed successfully!")
            self.load_files()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BulkFileRenamer(root)
    root.mainloop()
