
import tkinter as tk
from tkinter import filedialog, messagebox
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_file_to_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    
    gfile = drive.CreateFile({'title': file_path.split('/')[-1]})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    gfile.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})
    
    return gfile['alternateLink']

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if filepath:
        entry_var.set(filepath)

def upload():
    filepath = entry_var.get()
    if not filepath:
        messagebox.showerror("Error", "Please select a ZIP file to upload.")
        return
    try:
        link = upload_file_to_drive(filepath)
        messagebox.showinfo("Success", f"File uploaded!
Link: {link}")
    except Exception as e:
        messagebox.showerror("Upload Failed", str(e))

# GUI Setup
root = tk.Tk()
root.title("Upload to Google Drive")

entry_var = tk.StringVar(value="brand_workspace_bundle.zip")

tk.Label(root, text="Select ZIP File:").pack(pady=5)
entry = tk.Entry(root, textvariable=entry_var, width=50)
entry.pack(padx=10)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)
tk.Button(root, text="Upload to Google Drive", command=upload, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
