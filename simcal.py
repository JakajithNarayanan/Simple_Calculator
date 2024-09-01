from tkinter import *

root =Tk()

root.title("Simple calculator")

e=Entry(root,borderwidth=5,width=35)
e.grid(padx=10,pady=10,columnspan=3,column=0,row=0)
def pres(number) :
     current=e.get()
     e.delete(0,END)
     e.insert(0,(current)+str(number))
 
def presadd():
     firstnumber=e.get()
     global f_num
     global math 
     math="addition"
     f_num=int(firstnumber)
     e.delete(0,END)

def preseql():
    s_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(s_num))
    elif math=="subraction":
        e.insert(0,f_num -int(s_num))
    elif math=="multiplication":
        e.insert(0, f_num * int(s_num))
    elif math=="division":
        e.insert(0,f_num /int(s_num))        
              
def pressub():
     firstnumber=e.get()
     global f_num
     global math 
     math="subraction"
     f_num=int(firstnumber)
     e.delete(0,END)       
def presmul():
     firstnumber=e.get()
     global f_num
     global math 
     math="multiplication"
     f_num=int(firstnumber)
     e.delete(0,END)
def presdiv():
     firstnumber=e.get()
     global f_num
     global math 
     math="division"
     f_num=int(firstnumber)
     e.delete(0,END)     

def presclr():
    e.delete(0,END)     
     
     
       
but_one=Button(root,text="1",padx=40,pady=20,command=lambda:pres("1"))
but_two=Button(root,text="2",padx=40,pady=20,command=lambda:pres("2"))
but_three=Button(root,text="3",padx=40,pady=20,command=lambda:pres("3"))
but_four=Button(root,text="4",padx=40,pady=20,command=lambda:pres("4"))
but_five=Button(root,text="5",padx=40,pady=20,command=lambda:pres("5"))
but_six=Button(root,text="6",padx=40,pady=20,command=lambda:pres("6"))
but_seven=Button(root,text="7",padx=40,pady=20,command=lambda:pres("7"))
but_eight=Button(root,text="8",padx=40,pady=20,command=lambda:pres("8"))
but_nine=Button(root,text="9",padx=40,pady=20,command=lambda:pres("9"))
but_zero=Button(root,text="0",padx=40,pady=20,command=lambda:pres("0"))
but_clr=Button(root,text="Clear",padx=79,pady=20,command=presclr)
but_eql=Button(root,text="=",padx=91,pady=20,command=preseql)
but_add=Button(root,text="+",padx=39,pady=20,command=presadd)
but_sub=Button(root,text="-",padx=41,pady=20,command=pressub)
but_mul=Button(root,text="*",padx=40,pady=20,command=presmul)
but_div=Button(root,text="/",padx=41,pady=20,command=presdiv)

but_nine.grid(row=1,column=2)
but_eight.grid(row=1,column=1)
but_seven.grid(row=1,column=0)
but_six.grid(row=2,column=2)
but_five.grid(row=2,column=1)
but_four.grid(row=2,column=0)
but_three.grid(row=3,column=2)
but_two.grid(row=3,column=1)
but_one.grid(row=3,column=0)
but_zero.grid(row=4,column=0)
but_clr.grid(row=4,column=1,columnspan=2)
but_add.grid(row=5,column=0,)
but_eql.grid(row=5  ,column=1,columnspan=2)
but_mul.grid(row=6,column=0)
but_sub.grid(row=6,column=1)
but_div.grid(row=6,column=2)

mainloop()