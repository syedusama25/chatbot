from tkinter import*
import tkinter.messagebox
import numpy as np
import sqlite3
import datetime
win1=Tk()
win1.geometry('800x700')
win1.title("PyBot")
win1.iconbitmap('i.ico')
txt=StringVar()
var=""
txted=StringVar()
var=""
#win1.iconbitmap('atm.jpg')
C=Canvas(win1,bg='grey19',height=900,width=1600)
#img= PhotoImage(file='C:\\Users\\DANISH LAPTOP\\Desktop\\oop project\\final oop project\\giphy.gif')
img= PhotoImage(file='bot.png')
C.create_image(0, 0,anchor=NW,image=img)
C.place(x=0,y=0)
L=Label(C,text='CHATBOT APPLICATION',font='Times 30 bold',fg='black')
L.place(x=150,y=40)
#L1=Label(C,text='APPLICATION',font='Times 30 bold',fg='black')
#L1.place(x=200,y=80)
L2=Label(C,text="Enter UserName here: ",font='Times 20 bold',fg='black')
L2.place(x=450,y=180)
L3=Label(C,text='Enter Password here:',font='Times 20 bold',fg='black')
L3.place(x=450,y=330)
entry=Entry(C,justify=RIGHT,width=30,textvariable=txt,bg='grey12',fg='white',font='Times 10 bold')
entry.place(x=450,y=230)
password=Entry(C,justify=RIGHT,width=30,textvariable=txted,bg='grey12',fg='white',font='Times 10 bold',show='*')
password.place(x=450,y=380)
#show='*'
def all_clear():
    
    global txt
    global txted
    #var=''
    txt.set('')
    txted.set('')
def new_window():
    global txt
    global txted
    save=entry.get()
    saved=password.get()
    
    #z=int(save)
    a=str(save)
    b=str(saved)
    #print(a)
    #print(b)
    connect= sqlite3.connect('chatterbot.db')
    cursor = connect.cursor()
    cursor.execute('SELECT id FROM users where id= ?',(a,))
    exists = cursor.fetchall()
##    cursor.execute('SELECT password FROM users where password= ?',(b,))
##    exist = cursor.fetchall()
    #print(exists)
##    exists1 =exists[0]
##    exists2 =exists1[0]
##    print(exists2)
    d= datetime.date.today()
    now = datetime.datetime. now()
    t= now. strftime("%H:%M:%S")
    #print(d,t)
    cursor.execute('SELECT password FROM users where password= ?',(b,))
    exist = cursor.fetchall()
    #print(exist)
    if exists:
        if exist:
            with connect:
                cursor = connect.cursor()
                cursor.execute('INSERT INTO record(id,date,time) VALUES(?,?,?)',(a,d,t,)) #saving PIN in db
                connect.commit()
                win1.destroy()
                import gui
        else:
            tkinter.messagebox.showinfo('ERROR','PLEASE ENTER CORRECT USER NAME AND PASSWORD')
    else:
##        camera=cv2.VideoCapture(0)
##        for i in range(1):
##            return_value,image=camera.read()
##            cv2.imshow('image',image)
                #cv2.imwrite('opencv'+str(i)+'.png',image)

            #tkinter.messagebox.configure(background='black')
        tkinter.messagebox.showinfo('ERROR','PLEASE ENTER CORRECT USER NAME AND PASSWORD')
B=Button(C,text='CLICK HERE TO ENTER',bg='grey15',fg='white',font='Times 16 bold',command=new_window,height=2,width=32,padx=10,pady=10)
B.place(x=200,y=600)
B1=Button(C,text='CLEAR',bg='grey15',fg='white',font='Times 12 bold',command=all_clear,height=1,width=6,padx=4,pady=2)
B1.place(x=650,y=450)
 
win1.mainloop()
