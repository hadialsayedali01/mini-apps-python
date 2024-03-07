from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
import random,time,calendar
from tkinter import *

totalcalendarinfo={}

class Calendar(Frame):
    def __init__(self,master,year=1970,month=1):
        Frame.__init__(self,master)
        self.year=year
        self.month=month
        
        try:
            self.data=totalcalendarinfo[str(self.month)+"-"+str(self.year)] #stores data for each month
        except:
            self.data={}
        self.pack()

        startday,numdays = calendar.monthrange(self.year,self.month)[0],calendar.monthrange(self.year,self.month)[1]
        weekdaynames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        week=1
        weekday=startday
        
        dateFrame=Frame(self)
        dateFrame.pack()
        label=Label(dateFrame,text=str(self.month)+"-"+str(self.year),
                    font=("Arial",20))
        label.pack()
        
        calFrame=Frame(self)
        calFrame.pack()

        for n in range(7):
            label=Label(calFrame,text=weekdaynames[n])
            label.grid(row=0,column=n)
        for m in range(1,numdays+1):
            #key is in the format day-month-year
            #default value for each day is empty string
            self.data.setdefault(str(m)+"-"+str(self.month)+"-"+str(self.year),
                                 "")

            if weekday==7:
                week+=1
                weekday=0
            button=Button(calFrame,text=str(m),width=1,relief=RIDGE,command=lambda mm=m:self.click(mm))
            #note the alternative use of the lambda keyword; in this case, since we want the self.click()
            #argument to change with each button, we have to set a new variable mm to be each button's
            #unique "m" (numerical day of the month) variable
            button.grid(row=week,column=weekday)
                            
            weekday+=1

        if str(self.month)+"-"+str(self.year) not in totalcalendarinfo:
            totalcalendarinfo[str(self.month)+"-"+str(self.year)]=self.data

        navFrame=Frame(self)
        navFrame.pack(side=BOTTOM)
        previousbutton=Button(navFrame,text="PREVIOUS",command=self.prevmonth)
        previousbutton.grid(row=0,column=0)

        nextbutton=Button(navFrame,text="NEXT",command=self.nextmonth)
        nextbutton.grid(row=0,column=1)

    def click(self,dayofmonth):
        dateintext=str(dayofmonth)+"-"+str(self.month)+"-"+str(self.year)

        self.data[dateintext]=askstring(dateintext,
                                        prompt="Enter info:",
                                        initialvalue=self.data[dateintext])

    def prevmonth(self):
        self.deletewidgets()
        if self.month==1:
            self.year-=1
            self.month=12
        else:
            self.month-=1
        Calendar(self,self.year,self.month)


    def nextmonth(self):
        self.deletewidgets()
        if self.month==12:
            self.year+=1
            self.month=1
        else:
            self.month+=1
        Calendar(self,self.year,self.month)

    def deletewidgets(self):
        for widget in self.winfo_children(): #for every widget in
                                             #[list of widgets contained in self]
                widget.destroy() #delete the widget

root=Tk()
Calendar(root,year=2004,month=2)
root.mainloop()

