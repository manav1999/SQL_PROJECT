from tkinter import *
import os
def get_info():
    global got_values
    for entry in got_values:
    	print(entry.get())

got_values=[]
def to_insert():
	# window.close()
	window2=Tk()
	window2.title("For Insert")
	window2.minsize(200,400)
	li=['ms','ts'] #list for values to inserted
	strvar=StringVar()
	global got_values
	r=0
	c=0
	for i in li:
		t1=Label(window2,text=i)
		t1.grid(row=r,column=c)
		e1=Entry(window2)
		e1.grid(row=r,column=(c+1),columnspan=20)
		r=r+1
		got_values.append(e1)

	b1=Button(window2,text="Submit",command=get_info)
	b1.place(relx=1.0,rely=1.0,anchor=SE)
	window2.mainloop()

def plot_it():
	print("hello")
def to_plot():
	window3=Tk()
	window3.title("For Plot")
	b1=Button(window3,text="date vs 1",command=plot_it)
	b1.grid(row=0,column=0)
	b2=Button(window3,text="date vs 2",command=plot_it)
	b2.grid(row=0,column=1)
	b3=Button(window3,text="date vs 3",command=plot_it)
	b3.grid(row=0,column=2)
	b4=Button(window3,text="date vs 4",command=plot_it)
	b4.grid(row=0,column=3)
	b5=Button(window3,text="date vs 5",command=plot_it)
	b5.grid(row=0,column=4)
	b6=Button(window3,text="date vs 6",command=plot_it)
	b6.grid(row=0,column=5)
	window3.mainloop()





window=Tk()
window.title("Welcome to this program")
window.minsize(150,100)

b1=Button(window,text="Insert",command=to_insert)
b1.place(relx=0.5,rely=0.5,anchor=CENTER)

b2=Button(window,text="Plot",command=to_plot)
b2.place(relx=0.5,rely=0.3,anchor=CENTER)
window.mainloop()