# -*- coding: utf-8 -*-

from ctypes import * 
import time
import pythoncom  
import win32api
import win32con
import win32gui
import pyHook
from Tkinter import *
import win32clipboard as board

class POINT(Structure):  
    _fields_ = [  
            ("x", c_ulong),  
            ("y", c_ulong)  
            ]
  
def getPos():  
    point = POINT()  
    dll.GetCursorPos(byref(point))  
    return point.x, point.y

def getClipBoardText():  
    board.OpenClipboard()  
    d = board.GetClipboardData(win32con.CF_TEXT)  
    board.CloseClipboard()  
    return d

def setClipBoardText(aString):  
    board.OpenClipboard()  
    board.EmptyClipboard()  
    board.SetClipboardData(win32con.CF_TEXT, aString)  
    board.CloseClipboard()

def onKeyboardEvent(event):   
    "处理键盘事件"     
    #print('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')  
    #print("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))  
    print("MessageName:%s\n" % str(event.MessageName))  
    #print("Message:%d\n" % event.Message)  
    #print("Time:%d\n" % event.Time)  
    print("Window:%s\n" % str(event.Window))
    #print("WindowName:%s\n" % str(event.WindowName))  
    #print("Ascii_code: %d\n" % event.Ascii)  
    #print("Ascii_char:%s\n" % chr(event.Ascii))  
    print("Key:%s\n" % str(event.Key)) 
    if str(event.Key) == "Escape":
        global text_r
        text_r.set("!!!")
        pos_x , pos_y = getPos()

        hwnd = win32gui.GetDesktopWindow()
        #print hwnd
        dc = win32gui.GetWindowDC(hwnd)
        #print dc
        color = win32gui.GetPixel(dc, pos_x, pos_y)
        print color
        v_Red = color & 0xff;
        v_Green = (color & 0xff00) / 256;
        v_Blue = (color & 0xff0000) / 65536;

        RGB = (hex(v_Red)[2:4] + hex(v_Green)[2:4] + hex(v_Blue)[2:4]).upper()

        print RGB
        setClipBoardText(RGB)
    return True

dll = WinDLL('user32.dll'); 

root = Tk()
frame = Frame(root, width=300, height=200, bg='green')
frame.pack()

button_quit = Button(frame, text="QUIT", fg="red", command=frame.quit, width=6,height=1)
button_quit.place(x = 210, y = 150)
button_usage = Button(frame, text="USAGE", width=6,height=1)
button_usage.place(x = 40, y = 150)

text_r = StringVar()
text_g = StringVar()
text_b = StringVar()

entry_r = Entry(frame, width=30, textvariable= text_r)
entry_g = Entry(frame, width=30, textvariable= text_g)
entry_b = Entry(frame, width=30, textvariable= text_b)

text_r.set("R")
text_g.set("G")
text_b.set("B")

entry_r.place(x = 40, y = 20)
entry_g.place(x = 40, y = 55)
entry_b.place(x = 40, y = 90)

hm = pyHook.HookManager()

#keyboard
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()

#监控鼠标
#hm.MouseAll = onMouseEvent  
#hm.HookMouse()  

#pythoncom.PumpMessages()

while 1:
    root.after(100,root.quit)
    root.mainloop()
    #pythoncom.PumpMessages()

#root.mainloop()
