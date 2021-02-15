import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess


root = tk.Tk()
root.title("Quick Starter")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def openApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="select File",
                                          filetypes=(("executables", "*.app"),("all files", ".")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApp():
    for app in apps:
        try:
            os.startfile(app)
        except AttributeError:
            subprocess.call(['open', app])


canvas = tk.Canvas(root, height=750, width=750, bg="#98ded9")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

opeFile = tk.Button(root, text="Open File", padx=10,
                    pady=5, fg="black", bg="blue", command=openApp)

opeFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="black", bg="blue", command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')