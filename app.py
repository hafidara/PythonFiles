import tkinter as tk
from tkinter import Label, Text, filedialog
import os
from flask import send_from_directory

root = tk.Tk()
root.title('Python Files')
#adds an icon 
root.iconbitmap("favicon (3).ico")
#an empty list that stores the files that have been selected
apps = [ ]

def addApp():
    #it will delete every filename that was added to the list beforehand
    #and show the updated list
    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Select file", 
    filetypes=(("python", "*.py"),("all files","*.*")))
    apps.append(filename) #the file that has been selected is added to the list
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def runFile():
    for app in apps:
        os.startfile(app)
          
label = Label(root, text="Python Files")
label.pack()
canvas = tk.Canvas(root, height=400, width=400, bg="SteelBlue")
canvas.pack()

frame = tk.Frame(root, bg="yellow2")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Selact File", padx=10, pady=5, fg="white", bg="SteelBlue", command=addApp)
openFile.pack()
runFile = tk.Button(root, text="Run File", padx=10, pady=5, fg="white", bg="SteelBlue", command=runFile)
runFile.pack()
root.resizable(False, False)
root.mainloop()