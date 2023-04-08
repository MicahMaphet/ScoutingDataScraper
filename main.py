import requests
import tkinter as tk

win = tk.Tk()
win.title("Scouting Data Scraper")
win.geometry("500x400+50+50")

compBox = tk.Text(win, width=20, height=10)
compBox.place(x=50, y=50)
def reqData():
    req = compBox.get("1.0", "end")
    res = requests.get(req)
    
reqDataButton = tk.Button(win, text="Request Data", command=reqData)
reqDataButton.place(x=50, y=30)

win.mainloop()