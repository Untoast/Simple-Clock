import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import time
import os
import json
from datetime import datetime
import platform
favicon = 'SimpleClock.ico'
if platform.system() == "Windows":
    clearwindows = lambda: os.system('cls')
    clearwindows()
else:
    clearelse = lambda: os.system('clear')
    clearelse()
#-----------------------LOAD Settings.json FILE---------------------
with open('Settings.json', 'r') as f:
    data = json.load(f)
f.close
name = data["name"]
showsec = data["showsec"]
startfullscreen = data["startfull"]
#Default Settings:
#showsec = False
#startfull = False
#name = "User"
#--------------------------------------------------------

#---------Get time/date Functions---------
def gettime():
    ltime = time.strftime("%H:%M")
    hours, minutes = ltime.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    elif hours == 0:
        setting = "AM"
        hours = 12
    ltime = (("%02d:%02d" + " "+setting) %(hours, minutes))
    return ltime
#time with seconds (5:03:32 PM)
def gettimewsec():
    ltime = time.strftime("%H:%M")
    hours, minutes = ltime.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    elif hours == 0:
        setting = "AM"
        hours = 12
    ltime = (("%02d:%02d:"+str(datetime.now().second) + " "+ setting) %(hours, minutes))
    return ltime
    
def getdate():
    date = time.strftime("%A, %B %d, 20%y")
    return date
#-----------------
print("Starting UI...\n")
#-----
#-----
if startfullscreen == "True":
    setfull = 1
else:
    setfull = 0
window = tk.Tk()
def current_time_period():
    #1 = morning
    #2 = afternoon
    #3 = evening
    militime =time.strftime("%H")
    if militime == "06":
        timereference = 1
    if militime == "07":
        timereference = 1
    if militime == "08":
        timereference = 1
    if militime == "09":
        timereference = 1
    if militime == "10":
        timereference = 1
    if militime == "11":
        timereference = 1
    if militime == "12":
        timereference = 1
    if militime == "13":
        timereference = 2
    if militime == "14":
        timereference = 2
    if militime == "15":
        timereference = 2
    if militime == "16":
        timereference = 2
    if militime == "17":
        timereference = 2
    if militime == "18":
        timereference = 2
    if militime == "19":
        timereference = 2
    if militime == "20":
        timereference = 2
    if militime == "21":
        timereference = 3
    if militime == "22":
        timereference = 3
    if militime == "23":
        timereference = 3
    if militime == "24":
        timereference = 3
    if militime == "00":
        timereference = 3
    if militime == "01":
        timereference = 3
    if militime == "02":
        timereference = 3
    if militime == "03":
        timereference = 3
    if militime == "04":
        timereference = 3
    if militime == "05":
        timereference = 3
    if timereference == 1:
        timeperiod = "morning"
    elif timereference == 2:
        timeperiod = "afternoon"
    elif timereference == 3:
        timeperiod = "evening"
    window.after(10000, current_time_period)
    return timeperiod
current_time_period()
#-------Window Info-------------
#---Window Info---
window.title("Simple Clock")
favicon = 'SIcon.png'
window.iconphoto(True, tk.PhotoImage(file=favicon))
#---Window Settings---
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
startw = width - (width * 30 / 100)
starth = height - (height * 20 / 100)
window.minsize(width=270, height=190)
window.eval('tk::PlaceWindow . center')
if startfullscreen == "True":
    window.attributes('-fullscreen', True)
window.geometry(str(int(width / 1.1))+"x"+str(int(height / 1.1)))
window.configure(bg="#000000")
#-------------------------------
print("UI started\n")
print("-------------Start Time---------")
print("Raw time: "+str(datetime.now()))
print("Formatted Time: "+str(gettime()))
print("Formatted Time w/seconds: "+str(gettimewsec()))
print("Formatted Date: "+str(getdate()))
print("-------------Config------------")
print("Name: "+name)
print("Show Seconds: "+str(showsec))
print("Start Fullscreen: "+str(startfullscreen))
print("-----------Screen Info----------")
print("Width: "+str(width)+"\nHeight: "+str(height))
#----------Get Window Dimensions------------------------
def Getw():
        window_w = window.winfo_width()
        return window_w
def Geth():
        window_h = window.winfo_height()
        return window_h
def getdimensionsfunc():
    Getw()
    Geth()
getdimensionsfunc()
#----------text-------------
welcome = tk.Label(text="Good "+current_time_period()+", "+name, font=('arial', 40, 'underline'),bg='#000000',fg='#ffffff')
welcome.pack()
datelabel = tk.Label(text=str(getdate()), font=('arial', 50),bg='#000000',fg='#ffffff')
datelabel.pack(pady=height / 5)
timelabel = tk.Label(text=str(gettime()), font=('arial', 100),bg='#000000',fg='#ffffff')
timelabel.pack()

#---------setting-------------
nameinputvalue = name
showsecondsvalue = ''
startfullscreenvalue = '' 
if showsec == "True":
    showsecondsvalue = True
else:
    showsecondsvalue = False
if startfullscreen == "True":
    startfullscreenvalue = True
else:
    startfullscreenvalue = False

#------------------------Setting Window--------------------------------------
def settings():
    #------Setting Functions--------------
    def setname():
        global nameinputvalue
    def togglesec():
        global showsecondsvalue
        showsecondsvalue = not showsecondsvalue
        print("-------------Debug: Toggle Confirm-------------")
        if showsecondsvalue == True:
            print("Toggled Seconds: True")
        else:
            print("Toggled Seconds: False")
        print("------------------------------------------------")
    def togglefull():
        global startfullscreenvalue
        startfullscreenvalue = not startfullscreenvalue
        print("-------------Debug: Toggle Confirm-------------")
        if startfullscreenvalue == 1:
            print("Toggled Start on Full: True")
        else:
            print("Toggled Start on Full: False")
        print("------------------------------------------------")
    

    def enterfullscreen():
        global setfull

        if setfull == 1:
            window.attributes('-fullscreen', False)
            enterfullscreen.config(text="Enter Fullscreen")
            setfull = 0
        else:
            window.attributes('-fullscreen', True)
            enterfullscreen.config(text="Exit Fullscreen")
            setfull = 1
    #------config functions----------
    def closebutton():
        settingswin.destroy()
    def savesettings():
        newnameval = nametextbox.get("1.0", "end-1c")
        global showsec
        global startfullscreen
        showsec = showsecondsvalue
        startfullscreen = startfullscreenvalue
        data["name"] = newnameval
        data["showsec"] = str(showsec)
        data["startfull"] = str(startfullscreen)
        with open('Settings.json', 'w') as f:
            json.dump(data, f)
        #----update live
        welcome.configure(text="Welcome, "+newnameval)
        update()
        
        print("--------------------Saved Settings--------------------")
        print("Name: " + str(newnameval))
        print("Show Seconds: "+str(showsec))
        print("Start In Full Screen: " + str(startfullscreenvalue))
    #-------------------------OPEN SETTINGS WINDOW-----------------------------------------------------
    settingswin = Toplevel(window)
    settingswin.title("Settings")
    settingswin.configure(bg='#ffffff')
    settingswin.geometry(str(int(width-(width * 80 / 100)))+"x"+str(int(height - (height * 50 / 100))))
    #------------------------NAME LABEL AND BOX-----------------------
    InputNameLabel = tk.Label(settingswin, text="Name: ", font=('arial', 10, 'underline'),bg='#ffffff',fg='#000000')
    InputNameLabel.place(x=5,y=7)
    nametextbox = Text(settingswin,font='arial', height=1, width=30,bg='#ffffff')
    nametextbox.place(x=5,y=32)
    #------------------------SHOW SECONDS OPTION----------------
    showsecondstime = tk.Checkbutton(settingswin,relief='flat',width=20, text='Show Seconds',
                       variable= showsecondsvalue,
                       onvalue=True,
                       offvalue=False,
                       command=togglesec
                      )
    showsecondstime.pack(pady=10)
    showsecondstime.place(x=5,y=64)
    #------------------------START FULLSCREEN OPTION--------------------
    startfullscreenbox = tk.Checkbutton(settingswin,relief='flat',width=20, text='Start on Fullscreen',
                       variable= startfullscreenvalue,
                       onvalue=1,
                       offvalue=0,
                       command=togglefull
                      )
    startfullscreenbox.place(x=5,y=96)
    #--------Enter Fullscreen------------------------
    enterfullscreen = tk.Button(settingswin, relief='flat',width=23, text='Enter Fullscreen', command=enterfullscreen)
    if setfull == 1:
        enterfullscreen.config(text="Exit Fullscreen")
    else:
        enterfullscreen.config(text="Enter Fullscreen")
    enterfullscreen.place(x=5, y=128)
    #-----get value for check--------
    global showsec
    global startfullscreen
    if showsec == "True":
        showsecondstime.select()
    print(startfullscreen)
    if startfullscreen == "True":
        startfullscreenbox.select()
    #----------------------
    printdimensions = Button(settingswin,relief='flat', text="Print Main Window Dimensions")
    #-----Window config----
    showdimbutton = FALSE
    def getdim():
        print("width: "+str(window.winfo_width()))
        print("height: "+str(window.winfo_height()))
    def Getwfs():
        window_w = settingswin.winfo_width()
        settingswin.after(1000, Getw)
        return window_w
    Getwfs()
    if showdimbutton == True:
        getdimensions = Button(settingswin,relief='flat',text='Get Dimensions', command=getdim)
        getdimensions.place(x=5,y=1000)
    save = Button(settingswin,relief='flat', text="Save",width=10, command=savesettings)
    save.place(x=5,y=160)
    returnbutton = Button(settingswin,relief='flat', text="Exit",width=10, command=closebutton)
    returnbutton.place(x=str(Getwfs()/4.09),y=160)
    restartreminder = Label(settingswin, text="(Restart app to apply)", bg="#fff")
    restartreminder.place(x=str(Getwfs()/4.09),y=190)
    def updatesettings():
        returnbutton.place(x=str(Getwfs()/4.09),y=160)
        settingswin.after(1000, updatesettings)
    updatesettings()
#------------------------Setting Window--------------------------------------
def closemain():
    window.destroy()
Settingsb = tk.Button(window, text = "Settings", font = ('roboto', 10, 'bold'),borderwidth=1,relief='flat',bg='#fff',fg='#555',activebackground='#fff',width=10,activeforeground='#000',command =settings)
Settingsb.place(x=10,y=10)
CloseButton = Button(window, text="Close", font = ('roboto', 10, 'bold'),borderwidth=1,relief='flat',bg='#fff',fg='#555',activebackground='#fff',activeforeground='#000',width=10,command =closemain)
CloseButton.place(x= 100,y= 10)
#--------------
#--------Update function---------
def update():
    datelabel.config(text=str(getdate()))
    global showsec
    if showsec == "False":
        timelabel.config(text=str(gettime()))
    else:
        timelabel.config(text=str(gettimewsec()))
    window.after(500, update)
    welcome.pack(pady=Geth()/30)
    welcome.config(font=('arial', int(Geth()/30)), text="Good "+current_time_period()+", "+name)
    #-----------------------------
    datelabel.pack(pady=Geth()/10)
    datelabel.config(font=('arial', int(Geth()/15)))
    #-----------------------------
    timelabel.pack(pady=Geth()/7)
    timelabel.config(font=('arial', int(Geth()/10)))
    #-----------------------------
    Settingsb.config(font = ('roboto', int(Geth()/100), 'bold'))
    #-----------------------------
    CloseButton.config(font = ('roboto', int(Geth()/100), 'bold'))
    CloseButton.place(x= int((Geth()/10)),y= 10)
update()
window.mainloop()