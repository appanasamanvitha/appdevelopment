import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
import pygame
import cv2
from PIL import Image, ImageTk


import numpy as np

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="white",bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Quiz App Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="orange") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    abcdefgh='Welcome '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="#3DFA17",font="calibri 18",fg="#FAEF4C")
    level34.place(relx=0.17,rely=0.15)
    
    level = Label(menu_frame,text='Select Type of Quiz !!',bg="orange",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Number Series',bg="#7FFFD4",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Analogies',bg="#7FFFD4",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Artificial Language',bg="#7FFFD4",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    e.title('Quiz App - Number Series Type')
    
    easy_canvas = Canvas(e,width=720,height=440,bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#BADA55")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQu = [
                 [
                     "Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?",
                     "1/3",
                     "1/8",
                     "2/8",
                     "1/16" 
                 ] ,
                 [
                     "Look at this series: 36, 34, 30, 28, 24, ... What number should come next?" ,
                    "20",
                    "22",
                    "23",
                    "26"
                     
                 ],
                [
                    "Look at this series: 22, 21, 23, 22, 24, 23, ... What number should come next?" ,
                    "22",
                    "24",
                    "26",
                    "25"
                ],
                [
                    "Look at this series: 53, 53, 40, 40, 27, 27, ... What number should come next?" ,
                    "12",
                    "14",
                    "27",
                    "53"
                ],
                [
                    "Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come next?" ,
                    "7",
                    "10",
                    "12",
                    "13"
                ]
            ]
    answer = [
                "1/8",
                "22",
                "25",
                "14",
                "10"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQu[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQu[x][1],font="calibri 10",value=easyQu[x][1],variable = var,bg="#BADA55")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQu[x][2],font="calibri 10",value=easyQu[x][2],variable = var,bg="#BADA55")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQu[x][3],font="calibri 10",value=easyQu[x][3],variable = var,bg="#BADA55")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQu[x][4],font="calibri 10",value=easyQu[x][4],variable = var,bg="#BADA55")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    lis.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(lis) == 1:
                e.destroy()
                showMark(score)
        if len(lis) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if lis:
            x = random.choice(lis[1:])
            ques.configure(text =easyQu[x][0])
            
            a.configure(text=easyQu[x][1],value=easyQu[x][1])
      
            b.configure(text=easyQu[x][2],value=easyQu[x][2])
      
            c.configure(text=easyQu[x][3],value=easyQu[x][3])
      
            d.configure(text=easyQu[x][4],value=easyQu[x][4])
            
            lis.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    m.title('Quiz App -  Analogies type')
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#A1A100")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQu = [
                [
                     "Odometer is to mileage as compass is to",
                     "spped"
                     "hiking",
                     "needle",
                     "detection"
                ],
                [
                    "Marathon is to race as hibernation is to",
                    "winter",
                    "bear",
                    "dream",
                    "sleep"
                ],
                [
                    "Window is to pane as book is to",
                    "novel",
                    "glass",
                    "cover",
                    "page"
                ],
                [
                    "Cup is to coffee as bowl is to",
                    "dish",
                    "soup",
                    "spoon",
                    "food"
                ],
                [
                    "Yard is to inch as quart is to",
                    "gallon",
                    "ounce",
                    "milk",
                    "liquid"
                ], 
            ]
    answer = [
            "direction",
            "sleep",
            "page",
            "soup",
            "ounce"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQu[x][0],font="calibri 12",bg="#B26500")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQu[x][1],font="calibri 10",value=mediumQu[x][1],variable = var,bg="#A1A100")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQu[x][2],font="calibri 10",value=mediumQu[x][2],variable = var,bg="#A1A100")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQu[x][3],font="calibri 10",value=mediumQu[x][3],variable = var,bg="#A1A100")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQu[x][4],font="calibri 10",value=mediumQu[x][4],variable = var,bg="#A1A100")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQu[x][0])
            
            a.configure(text=mediumQu[x][1],value=mediumQu[x][1])
      
            b.configure(text=mediumQu[x][2],value=mediumQu[x][2])
      
            c.configure(text=mediumQu[x][3],value=mediumQu[x][3])
      
            d.configure(text=mediumQu[x][4],value=mediumQu[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    #count=0
    h = Tk()
    h.title('Quiz App -Artificial Language Type')
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#008080")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    """hardQu = [
                [
                    "Here are some words translated from an artificial language.\ngorblflur means fan belt\npixngorbl means ceiling fan\narthtusl means tile roof\nWhich word could mean "ceiling tile"?",
                    "gorbltusl",
                    "flurgorbl",
                    "arthflur",
                    "pixnarth"
                ],
                [
                    "Here are some words translated from an artificial language.\nmigenlasan means cupboard\nlasanpoen means boardwalk\ncuopdansa means pullman\nWhich word could mean "walkway"?",
                    "poenmigen",
                    "cuopeisel",
                    "lasandansa",
                    "poenforc"
                ],
                [
                    "Here are some words translated from an artificial language.\nmoolokarn means blue sky\nwilkospadi means bicycle race\nmoolowilko means blue bicycle\nWhich word could mean "racecar"?",
                    "wilkozwet",
                    "spadiwilko",
                    "moolobreil",
                    "spadivolo"   
                ],
                [
                    "Here are some words translated from an artificial language.\nagnoscrenia means poisonous spider\ndelanocrenia means poisonous snake\nagnosdeery means brown spider\nWhich word could mean "black widow spider"?",
                    "deeryclostagnos",
                    "agnosdelano",
                    "agnosvitriblunin",
                    "trymuttiagnos"
                ],
                [
                    "Here are some words translated from an artificial language.\nhapllesh means cloudburst\nsrenchoch means pinball\nresbosrench means ninepin\nWhich word could mean "cloud nine"?",
                    "leshsrench",
                    "ochhapl",
                    "haploch",
                    "haplresbo"
                ] 
            ]
    answer = [
            "pixnarth",
            "poenforc",
            "spadiwilko",
            "agnosvitriblunin",
            "haplresbo"
            ]"""
    
    hardQu = [
        [
            "Here are some words translated from an artificial language.\ngorblflur means fan belt\npixngorbl means ceiling fan\narthtusl means tile roof\nWhich word could mean 'ceiling tile'?",
            "gorbltusl",
            "flurgorbl",
            "arthflur",
            "pixnarth"
        ],
        [
            "Here are some words translated from an artificial language.\nmigenlasan means cupboard\nlasanpoen means boardwalk\ncuopdansa means pullman\nWhich word could mean 'walkway'?",
            "poenmigen",
            "cuopeisel",
            "lasandansa",
            "poenforc"
        ],
        [
            "Here are some words translated from an artificial language.\nmoolokarn means blue sky\nwilkospadi means bicycle race\nmoolowilko means blue bicycle\nWhich word could mean 'racecar'?",
            "wilkozwet",
            "spadiwilko",
            "moolobreil",
            "spadivolo"   
        ],
        [
            "Here are some words translated from an artificial language.\nagnoscrenia means poisonous spider\ndelanocrenia means poisonous snake\nagnosdeery means brown spider\nWhich word could mean 'black widow spider'?",
            "deeryclostagnos",
            "agnosdelano",
            "agnosvitriblunin",
            "trymuttiagnos"
        ],
        [
            "Here are some words translated from an artificial language.\nhapllesh means cloudburst\nsrenchoch means pinball\nresbosrench means ninepin\nWhich word could mean 'cloud nine'?",
            "leshsrench",
            "ochhapl",
            "haploch",
            "haplresbo"
        ] 
    ]
    answer = [
        "pixnarth",
        "poenforc",
        "spadiwilko",
        "agnosvitriblunin",
        "haplresbo"
    ]

    
    lis = ['',0,1,2,3,4]
    x = random.choice(lis[1:])
    
    ques = Label(hard_frame,text =hardQu[x][0],font="calibri 12",bg="#A0DB8E")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQu[x][1],font="calibri 10",value=hardQu[x][1],variable = var,bg="#008080",fg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQu[x][2],font="calibri 10",value=hardQu[x][2],variable = var,bg="#008080",fg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQu[x][3],font="calibri 10",value=hardQu[x][3],variable = var,bg="#008080",fg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQu[x][4],font="calibri 10",value=hardQu[x][4],variable = var,bg="#008080",fg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    lis.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(lis) == 1:
                h.destroy()
                showMark(score)
        if len(lis) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if lis:
            x = random.choice(lis[1:])
            ques.configure(text =hardQu[x][0])
            
            a.configure(text=hardQu[x][1],value=hardQu[x][1])
      
            b.configure(text=hardQu[x][2],value=hardQu[x][2])
      
            c.configure(text=hardQu[x][3],value=hardQu[x][3])
      
            d.configure(text=hardQu[x][4],value=hardQu[x][4])
            
            lis.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
 
    submit = Button(hard_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)

    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    sho = Tk()
    sho.title('Your Marks')
    
    sti = "Your score is "+str(mark)+"/5"
    mlabel = Label(sho,text=sti,fg="pink", bg="white")
    mlabel.pack()
    
    def callsignUpPage():
        sho.destroy()
        start()
    
    def myeasy():
        sho.destroy()
        easy()
    
    b79=Button(text="Re-attempt", command=myeasy, bg="black", fg="white")
    b79.pack()
    

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained : ','Total Marks: '
    sizes = [int(mark),5-int(mark)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    canvas = FigureCanvasTkAgg(fig, master=sho)  
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b78=Button(text="Sign Out",command=callsignUpPage,fg="blue", bg="pink")
    b78.pack()
    
    sho.mainloop()

def start():
    global root 
    root = Tk()
    root.title('Quiz')
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)

    imgg = Image.open("C:\\Users\\admin\\Downloads\\output-onlinepngtools (1).png")
    imagg = imgg.resize((40,40))
    img = ImageTk.PhotoImage(imagg)
    but = Button(root, text='Start',command = signUpPage,bg="blue",fg="gray") 
    but.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    but.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()