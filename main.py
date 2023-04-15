import requests
import tkinter as tk

MATCHES = 10

ENTRY_X = 450 # the base x axis of all of the scouting boxes
ENTRY_Y = 50 # the base y axis of all of the scouting boxes
ENTRY_SPACE = 100 # the space between scouting boxes

win = tk.Tk()
win.title("Scouting Data Scraper")
win.geometry("500x400+50+50")
win.iconbitmap()

reqBox = tk.Text(win, width=20, height=5)
reqBox.place(x=25, y=50)

resBox = tk.Text(win, width=50, height=25)
resBox.place(x=25, y=100)

sortedBox = tk.Text(win, width=50, height=25)
sortedBox.place(x=ENTRY_X, y=100)

scouters = [tk.Text(win, width=25, height=2)]
def placeX (): return ENTRY_X + (ENTRY_SPACE * (len(scouters) - 1))
scouters[0].place(x=placeX(), y=ENTRY_Y)

def reqData():
    req = reqBox.get("1.0", "end")
    res = requests.get("https://www.thebluealliance.com/event/2023gacmp").text
    print(res)
    print(sort(res))
    resBox.insert("1.0", sort("this is a team . . ."))

def sort(list):
    sortedList = []
    for i in list:
        if i == "i":
            sortedList.append(i)
    return sortedList

def sortScouters():
    sortedScouters = []
    for x in scouters:
        sortedScouters.append(x.get("1.0", "end")[0:-2])
    sortedBox.delete("1.0", "end")
    sortedBox.insert("1.0", str(sortedScouters))

reqDataButton = tk.Button(win, text="Request Data", command=reqData)
reqDataButton.place(x=25, y=20)

sortScoutersButton = tk.Button(win, text="Sort Scouters", command=sortScouters)
sortScoutersButton.place(x=ENTRY_X, y=20)

win.mainloop()