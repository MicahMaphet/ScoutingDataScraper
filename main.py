import requests
import tkinter as tk

SCOUTERS_ENTRY_SPACE = 100

win = tk.Tk()
win.title("Scouting Data Scraper")
win.geometry("500x400+50+50")
win.iconbitmap()

reqBox = tk.Text(win, width=20, height=5)
reqBox.place(x=25, y=50)
resBox = tk.Text(win, width=50, height=50)
resBox.place(x=100, y=50)

def reqData():
    req = reqBox.get("1.0", "end")
    res = requests.get(req)

reqDataButton = tk.Button(win, text="Request Data", command=reqData)
reqDataButton.place(x=25, y=20)


win.mainloop()