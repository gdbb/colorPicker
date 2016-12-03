# -*- coding: utf-8 -*-

import gtk.gdk
import time
#import pythoncom
import pyperclip
from Tkinter import *
#from PIL import Image,ImageGrab

def setClipBoardText(text):
    pyperclip.copy(text)

def onKeyboardEvent(event):
    "handle keyboard events"
    global button_trigger
    
    if button_trigger == -1:
        return True

    if event.char == chr(32) or True:
        
        default = gtk.gdk.display_get_default()
        window = default.get_default_screen().get_root_window()

        weight, height = window.get_size()
        buf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False, 8, weight, height)
        buf = buf.get_from_drawable(window, window.get_colormap(), 0, 0, 0, 0, weight, height)
        
        #print event.x, event.y
        #print event.x_root, event.y_root
        x = root.winfo_pointerx()# - root.winfo_rootx()
        y = root.winfo_pointery()# - root.winfo_rooty()
        
        color = buf.get_pixels_array()[y][x]
        print x, y
        print color

        v_Red = color[0];
        v_Green = color[1];
        v_Blue = color[2];

        text_r.set(v_Red)
        text_g.set(v_Green)
        text_b.set(v_Blue)

        RGB = (hex(v_Red)[2:4] + hex(v_Green)[2:4] + hex(v_Blue)[2:4]).upper()
        RGB = "%02X"%v_Red + "%02X"%v_Green + "%02X"%v_Blue
        text_total.set(RGB)
        #setClipBoardText(RGB)

        #buf.save("screen.png", "png")

        '''
        #screen = ImageGrab.grab()
        pos_x = pos_y = 1
        color = screen.getpixel((x, y))

        v_Red = color[0];
        v_Green = color[1];
        v_Blue = color[2];

        text_r.set(v_Red)
        text_g.set(v_Green)
        text_b.set(v_Blue)

        RGB = (hex(v_Red)[2:4] + hex(v_Green)[2:4] + hex(v_Blue)[2:4]).upper()
        RGB = "%02X"%v_Red + "%02X"%v_Green + "%02X"%v_Blue
        text_total.set(RGB)
        setClipBoardText(RGB)
        '''
    return True

def changeState():
    global button_trigger
    if button_trigger == -1:
        button_text.set("STOP")
        button_trigger *= -1 
    else:
        button_text.set("START") 
        button_trigger *= -1


def showUsage():
    usageText = "    After clicking the \"START\" button you can press the \"Esc\" key to get RGB value of the point where your cursor is at and the RGB value will be in your clipboard."
    usageWindow = Toplevel(root)
    usageWindow.geometry("300x200")
    label = Label(usageWindow, text=usageText, font=("Helvetica", 16), wraplength=280, justify="left", anchor="center")
    label.pack()

def showAbout():
    aboutText = "David.\ngdbb.68@163.com"
    aboutWindow = Toplevel(root)
    aboutWindow.geometry("300x50")
    label = Label(aboutWindow, text=aboutText, font=("Helvetica", 16), wraplength=280, justify="left", anchor="center")
    label.pack()

root = Tk()
root.resizable(False, False)
root.title("colorPicker")

frame = Frame(root, width=300, height=220, bg='green')
frame.pack()

menuList = Menu(root)
fileMenu = Menu(menuList, tearoff=0)
fileMenu.add_command(label="Usage", command=showUsage)
fileMenu.add_command(label="About", command=showAbout)
menuList.add_cascade(label="Help", menu=fileMenu)


root.config(menu=menuList)

button_quit = Button(frame, text="QUIT", fg="red", command=frame.quit, width=6,height=1)
button_quit.place(x = 210, y = 170)

button_trigger = -1
button_text = StringVar()
button_state = Button(frame, textvariable=button_text, command=changeState, width=6,height=1)
button_state.place(x = 40, y = 170)
button_text.set("START")

text_r = StringVar()
text_g = StringVar()
text_b = StringVar()
text_total = StringVar()

text_r.set("R")
text_g.set("G")
text_b.set("B")
text_total.set("RGB")

entry_r = Entry(frame, width=28, textvariable= text_r, state="readonly")
entry_g = Entry(frame, width=28, textvariable= text_g, state="readonly")
entry_b = Entry(frame, width=28, textvariable= text_b, state="readonly")
entry_total = Entry(frame, width=28, textvariable= text_total, state="readonly")


label_r = Label(frame, text="R")
label_g = Label(frame, text="G")
label_b = Label(frame, text="B")


label_r.place(x = 40, y = 20)
label_g.place(x = 40, y = 55)
label_b.place(x = 40, y = 90)

entry_r.place(x = 60, y = 20)
entry_g.place(x = 60, y = 55)
entry_b.place(x = 60, y = 90)
entry_total.place(x = 60, y = 125)

root.bind("<Key>", onKeyboardEvent)

root.mainloop()
