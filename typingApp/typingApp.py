#typing speed application

from tkinter import *
import time
#from statistics import mean
from tkinter.messagebox import showinfo
from random import choice

class TypeSpeed(Frame):
    def __init__(self,master):
        Frame.__init__(self,master) 
        self.pack(padx=100,pady=100) #packing the app inside the main window

        texts=open("typingtesttexts.txt").read().split("\n")
        self.text=choice(texts)
        self.text_words=self.text.split(" ")
        print(self.text_words)
        text_label=Label(master,wraplength=400,width=50,text=self.text,
                         justify=LEFT)
        text_label.pack(fill=BOTH,expand=True,padx=100,side=TOP)

        self.textbox=Text(master,width=50,height=25) #text box
        self.textbox.pack(fill=BOTH,expand=True) #text box should fill & expand

        self.textbox.bind("<KeyPress>",self.begin) #self.begin() is called upon a key bieng pressed inside text box
        self.wordbegan=False #whether this is the start of a word
        self.start_time,self.end_time=0,0
        self.wpms=set() #set of wpms
        self.avgtimetaken=0
        
    def begin(self,event):
        #if key!=space and != enter and we are not at the beginning of the word,
        # consider this the start of the word, and start timer
        if event.keysym_num!=32 and self.wordbegan==False and event.keysym_num!=65293: 
            self.start_time=time.time()
            self.wordbegan=True

        elif event.keysym_num==32 and self.wordbegan==True:
            #if we are in a word and the space button is pressed,
            #stop the timer and record the time taken; calculate and record the time taken
            self.end_time=time.time()
            timetaken=self.end_time-self.start_time
            self.wpms.add(timetaken) #"wpms" is a misnomer
            self.avgtimetaken=sum(self.wpms)/len(self.wpms)

            self.wordbegan=False
            
        elif event.keysym_num==65293:
            #if enter is pressed, stop the recording program and show the user their wpm
            self.wordbegan=False

            user_words=self.textbox.get(1.0, "end-1c").split(" ")
            
            if len(user_words)>len(self.text_words):
                absolute_text=user_words
                relative_text=self.text_words
            else:
                absolute_text=self.text_words
                relative_text=user_words

            errors=0
            for i in range(len(relative_text)):
                if relative_text[i]!=absolute_text[i]:
                    errors += 1
            try:
                accuracy = round(len(self.text_words)/errors,2)
            except ZeroDivisionError:
                accuracy=100
            
            try:
                wpm = 60/self.avgtimetaken
                showinfo(title="Results",message="Wpm: {}\nAccuracy:{}".format(str(round(wpm,2)),str(accuracy)))
                
            except ZeroDivisionError:
                showinfo(title="Results",message="No data to record.")

root=Tk()
TypeSpeed(root)
root.mainloop()
