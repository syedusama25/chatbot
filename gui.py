from tkinter import *
import time
import tkinter.messagebox
from bot import chat
import os, sys
import pyttsx3
import speech_recognition as sr
import threading
from pygame import mixer
saved_username = ["You"]
#ans=["PyBot"]
window_size="800x700"

class ChatInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
# Menu bar

    # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
       # file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Clear Chat", command=self.clear_chat)
      #  file.add_separator()
        file.add_command(label="Exit",command=self.chatexit)

    # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # username
       

        self.photo = PhotoImage(file='microphone.png').subsample(15,15)

        # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default",command=self.font_change_default)
        font.add_command(label="Times",command=self.font_change_times)
        font.add_command(label="System",command=self.font_change_system)
        font.add_command(label="Helvetica",command=self.font_change_helvetica)
        font.add_command(label="Fixedsys",command=self.font_change_fixedsys)

        # color theme
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default",command=self.color_theme_default) 
       # color_theme.add_command(label="Night",command=self.) 
        color_theme.add_command(label="Grey",command=self.color_theme_grey) 
        color_theme.add_command(label="Blue",command=self.color_theme_dark_blue) 
       
        color_theme.add_command(label="Torque",command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker",command=self.color_theme_hacker)
       # color_theme.add_command(label='Mkbhd',command=self.MKBHD)


      
        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        #help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About ChatBot", command=self.msg)
        help_option.add_command(label="Developers", command=self.about)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=6)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH,expand=0,side=RIGHT)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=self.open_app, activebackground="#FFFFFF",
                                  activeforeground="#000000")
        #self.send_button.pack(side=LEFT, ipady=8)
        #self.master.bind('<Return>',self.open_app)
        #self.master.bind('<Return>', self.send_message_insert)
        self.MyButton6 = Button(self.send_button_frame,image=self.photo , width=5, relief=GROOVE, bg='white',
                                  bd=1, command=self.button_Click, activebackground="#FFFFFF",activeforeground="#000000")
        self.send_button.pack(side=RIGHT, ipady=8)
        self.MyButton6.pack(side=RIGHT, ipadx=8,ipady=5)
        self.master.bind("<Return>", self.send_message_insert)
        
        self.last_sent_label(date="No messages sent.")
        #t2 = threading.Thread(target=self.send_message_insert(, name='t1')
        #t2.start()
    
    #@staticmethod
    def button_Click(self): 
        mixer.init()
        mixer.music.load('chime1.mp3')
        mixer.music.play()
        self.r = sr.Recognizer()
        self.r.pause_threshold = 0.7
        self.r.energy_threshold = 400
        with sr.Microphone() as source:
            try:
                self.audio =self.r.listen(source, timeout=5)
                self.message = str(self.r.recognize_google(self.audio))
                mixer.music.load('chime2.mp3')
                mixer.music.play()
                self.entry_field.focus()
                self.entry_field.delete(0, END)
                self.entry_field.insert(0,self.message)
                self.open_app()
            except sr.UnknownValueError:
                self.error='Google Speech Recognition could not understand audio'
                self.entry_field.focus()
                self.entry_field.delete(0, END)
                self.entry_field.insert(0,self.error)
                self.send_message_insert(self.error)
            except sr.RequestError as e:
                error='Could not request results from Google Speech Recognition Service'
                self.entry_field.focus()
                self.entry_field.delete(0, END)
                self.entry_field.insert(0,self.error)
                self.send_message_insert(self.error)
            else:
                pass 
    def playResponce(self,responce):
        x=pyttsx3.init()
        #print(responce)
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
                #print(b)
                 
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(responce)
        x.runAndWait()
        #print("Played Successfully......")
        
        
    def last_sent_label(self, date):
        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("PyBOT v1.0",'Chatbot is a chatbot for answering programming queries\n')

    def about(self):
        tkinter.messagebox.showinfo("CHATBOT Developers","1.Syed Usama\n2.Ifrah Ishtiaq\n3.Sadia Razzaq\n")
    def open_chrome(self):
        os.startfile( "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    def open_vs_code(self):
        os.startfile( "C:\Program Files\Microsoft VS Code\Code.exe")
    def open_arduino(self):
        os.startfile( "C:\\Program Files (x86)\\Arduino\\arduino.exe")
    def open_matlab(self):
        os.startfile( "C:\\Program Files\\MATLAB\MATLAB Production Server\\R2015a\\bin\\matlab.exe")
    def open_atmelstudio(self):
        os.startfile( "C:\\Program Files (x86)\\Atmel\\Studio\\7.0\\AtmelStudio.exe")
    def open_staruml(self):
        os.startfile( "C:\\Program Files\\StarUML\\StarUML.exe")
    def open_wpsoffice(self):
        os.startfile( "C:\\Users\\Syed Usama\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe")
    def open_python(self):
        os.startfile( "C:\\Users\\Syed Usama\\AppData\\Local\\Programs\\Python\\Python36\\pythonw.exe")    
    def open_texworks(self):
        os.startfile( "C:\\software\\miktex\\bin\\x64\\miktex-texworks.exe")
    def open_sqlite(self):
        os.startfile("C:\\Program Files\\DB Browser for SQLite\\DB Browser for SQLite.exe")


    # Close opened file
    def close_chrome(self):
        os.system('TASKKILL /F /IM chrome.exe')
    def close_arduino(self):
        os.system('TASKKILL /F /IM arduino.exe')
    def close_matlab(self):
        os.system('TASKKILL /F /IM matlab.exe')
    def close_atmelstudio(self):
        os.system('TASKKILL /F /IM AtmelStudio.exe')
    def close_staruml(self):
        os.system('TASKKILL /F /IM StarUML.exe')
    def close_wpsoffice(self):
        os.system('TASKKILL /F /IM ksolaunch.exe')
    def close_python(self):
        os.system('TASKKILL /F /IM pythonw.exe')
    def close_texworks(self):
        os.system('TASKKILL /F /IM miktex-texworks.exe')
    def close_sqlite(self):
        os.system('TASKKILL /F /IM DB Browser for SQLite.exe')
           
    def send_message_insert(self, message):
        #self.open_(self.entry_field.get())
        user_input = self.entry_field.get()
        pr1 = "Me : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        ob=chat(user_input)
        pr="PyBot : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.playResponce, args=(ob,))
        t2.start()
        #t1 = threading.Thread(target=self.playResponce, args=(user_input,))
        #t1.start()
        #time.sleep(1)
##        self.open_(self.entry_field.get())
##    def idenytifier(self, message):
##        #b=input("enter app name:  ")
##        self.c=self.entry_field.get().split()
##        print(self.c)
##        #print(self.c[0],self.c[1])
##        self.open_(self.c)
    def open_app(self):
        self.c=self.entry_field.get().split()
        #print(self.c)
        for i in range(0,len(self.c)-1):
        #print(i)
            self.z=self.c[i]
            if self.z=='open' or self.z=='Open':
                self.a=self.c[i+1]
                #print(self.a)
                if self.a == 'Chrome' or self.a=='chrome':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_chrome()
                    break
                elif self.a =='vs code' or self.a=='Vs Code' or self.a=='Vs code':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_vs_code()
                    break
                elif self.a=='arduino' or self.a=='Arduino':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_arduino()
                    break
                elif self.a=="matlab" or self.a=='Matlab':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_matlab()
                    break
                elif self.a=='atmel' or self.a=='Atmel':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_atmelstudio()
                    break
                elif self.a=='wps office' or self.a=='W P S Office':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_wpsoffice()
                    break
                elif self.a=='uml' or self.a=='Uml':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_staruml()
                    break
                elif self.a=='python' or self.a=='Python':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_python()
                    break
                elif self.a=='texworks' or self.a=='Texworks':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_texworks()
                    break
                elif self.a=='sqlite' or self.a=='Sqlite':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="opening"+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.open_sqlite()
                    break
##                else:
##                    self.close(c)
            
            elif i==len(self.c)-2:
                
                #print(i)
                self.close(self.c)
            
    def close(self,c):
        self.d=self.entry_field.get().split()
        #print(self.d)
        for i in range(0,len(self.d)-1):
            self.z=self.d[i]
            if self.d[i]=='close':
                self.a=self.d[i+1]
                if self.a== 'chrome':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_chrome()
                    break
                elif self.a=='vs code':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_vs_code()
                    break
                elif self.a=='arduino':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_arduino()
                    break
                elif self.a=='matlab':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_matlab()
                    break
                elif self.a=='atmel':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_atmelstudio()
                    break
                elif self.a=='wps office':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_wpsoffice()
                    break
                elif self.a=='uml':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    close_staruml()
                    break  
                elif self.a=='python':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_python()
                    break
                elif self.a=='texworks':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    close_texworks()
                    break
                elif a=='sqlite':
                    user_input = self.entry_field.get()
                    pr1 = "Me : " + user_input + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr1)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    #ob=chat(user_input)
                    ob="closing "+self.a
                    pr="PyBot : " + ob + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(ob,))
                    t2.start()
                    self.close_sqlite()
                    break
##                else:
##                    self.self.bot_response()
            elif i==len(self.d)-2:
                self.send_message_insert(None)
##                continue

##    def bot_response(self):
        #self.open_(self.entry_field.get())
##        ob=chat(user_input)
##        pr="PyBot : " + ob + "\n"
##        self.text_box.configure(state=NORMAL)
##        self.text_box.insert(END, pr)
##        self.text_box.configure(state=DISABLED)
##        self.text_box.see(END)
##        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
##        self.entry_field.delete(0,END)
##        time.sleep(0)
##        t2 = threading.Thread(target=self.playResponce, args=(ob,))
##        t2.start()
        #return ob   
        
    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.entry_field.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_times(self):
        self.text_box.config(font="Times")
        self.entry_field.config(font="Times")
        self.font = "Times"

    def font_change_system(self):
        self.text_box.config(font="System")
        self.entry_field.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.text_box.config(font="helvetica 10")
        self.entry_field.config(font="helvetica 10")
        self.font = "helvetica 10"

    def font_change_fixedsys(self):
        self.text_box.config(font="fixedsys")
        self.entry_field.config(font="fixedsys")
        self.font = "fixedsys"

    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.text_frame.config(bg="#EEEEEE")
        self.entry_frame.config(bg="#EEEEEE")
        self.text_box.config(bg="#FFFFFF", fg="#000000")
        self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg="#EEEEEE")
        self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.sent_label.config(bg="#EEEEEE", fg="#000000")

        self.tl_bg = "#FFFFFF"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"

    # Dark
    def color_theme_dark(self):
        self.master.config(bg="#2a2b2d")
        self.text_frame.config(bg="#2a2b2d")
        self.text_box.config(bg="#212121", fg="#FFFFFF")
        self.entry_frame.config(bg="#2a2b2d")
        self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#2a2b2d")
        self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
       # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

        self.tl_bg = "#212121"
        self.tl_bg2 = "#2a2b2d"
        self.tl_fg = "#FFFFFF"

    # Grey
    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#4f4f4f", fg="#ffffff")
        self.entry_frame.config(bg="#444444")
        self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        #self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"


    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"    

    # Blue
    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

 
    

    # Torque
    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

    # Hacker
    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"

    

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()    

        
root=Tk()

a = ChatInterface(root)
a.bind('<Return>',ChatInterface.open_app)
root.geometry(window_size)
root.title("PyBot")
root.iconbitmap('i.ico')
root.mainloop()
