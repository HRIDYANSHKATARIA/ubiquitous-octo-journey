from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("world clock")
root.geometry("600x450")

clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))


#India

India_label = Label(root,text="India")
India_label.place(relx=0.2,rely=0.055,anchor=CENTER)

India_clock = Label(root)
India_clock["image"]=clock_image
India_clock.place(relx=0.2,rely=0.65,anchor=CENTER)


India_time = Label(root)
India_time.place(relx=0.2,rely=0.75,anchor=CENTER)

#AUSTRALIA
AUS_label = Label(root,text="India")
AUS_label.place(relx=0.2,rely=0.055,anchor=CENTER)

AUS_clock = Label(root)
AUS_clock["image"]=clock_image
AUS_clock.place(relx=0.2,rely=0.65,anchor=CENTER)


AUS_time = Label(root)
AUS_time.place(relx=0.2,rely=0.75,anchor=CENTER)


#Usa

Usa_label = Label(root,text="USA")
Usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)

Usa_clock = Label(root)
Usa_clock["image"]=clock_image
Usa_clock.place(relx=0.7,rely=0.35,anchor=CENTER)


Usa_time = Label(root)
Usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)

#JAPAN

JAP_label = Label(root,text="JAPAN")
JAP_label.place(relx=0.7,rely=0.055,anchor=CENTER)

JAP_clock = Label(root)
JAP_clock["image"]=clock_image
JAP_clock.place(relx=0.7,rely=0.65,anchor=CENTER)


JAP_time = Label(root)
JAP_time.place(relx=0.7,rely=0.75,anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        India_time["text"]="Time : "+current_time
        India_time.after(200,self.times)
        
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        India_time["text"]="Time : "+current_time
        India_time.after(200,self.times)
class Japan():
    def times(self):
        home=pytz.timezone('Japan/Hiroshima')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        India_time["text"]="Time : "+current_time
        India_time.after(200,self.times)
        
class Australia():
    def times(self):
        home=pytz.timezone('Australia/Sydney')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        India_time["text"]="Time : "+current_time
        India_time.after(200,self.times)
        
obj_India = India()
obj_USA = USA()
obj_Australia = Australia()
obj_Japan = Japan()


India_btn = Button(root,text="Show Time",command=obj_India.times)
India_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

USA_btn = Button(root,text="Show Time",command=obj_USA.times)
USA_btn.place(relx=0.7,rely=0.8,anchor=CENTER)
        
Australia_btn = Button(root,text="Show Time",command=obj_Australia.times)
Australia_btn.place(relx=0.3,rely=0.8,anchor=CENTER)

Japan_btn = Button(root,text="Show Time",command=obj_Japan.times)
Japan_btn.place(relx=0.8,rely=0.8,anchor=CENTER)




root.mainloop()
