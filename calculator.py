from tkinter import *
win=Tk()
win.title("calculator")
win.geometry("510x400")
win.configure(bg="#17161b")
equation=""
def show(value):
    global equation
    equation=equation+value
    result.configure(text=equation)
def clear():
    global equation
    equation=""
    result.configure(text=equation)
def cal():
    global equation
    ans=""
    if equation !="":
        try:
            ans= eval(equation)
        except:
            ans="error"
            equation=""
    result.config(text=ans)           

result=Label(win,width=25,height=2,text="",font=("arial",30))
result.pack()
Button(win,height=1,width=5,text="C",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: clear()).place(x=10,y=100)
Button(win,height=1,width=5,text="/",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("/")).place(x=150,y=100)
Button(win,height=1,width=5,text="X",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("*")).place(x=290,y=100)
Button(win,height=1,width=5,text="%",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("%")).place(x=430,y=100)

Button(win,height=1,width=5,text="7",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("7")).place(x=10,y=150)
Button(win,height=1,width=5,text="8",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("8")).place(x=150,y=150)
Button(win,height=1,width=5,text="9",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("9")).place(x=290,y=150)
Button(win,height=1,width=5,text="-",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("-")).place(x=430,y=150)

Button(win,height=1,width=5,text="4",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("4")).place(x=10,y=200)
Button(win,height=1,width=5,text="5",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("5")).place(x=150,y=200)
Button(win,height=1,width=5,text="6",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("6")).place(x=290,y=200)
Button(win,height=1,width=5,text="+",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("+")).place(x=430,y=200)

Button(win,height=1,width=5,text="1",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("1")).place(x=10,y=250)
Button(win,height=1,width=5,text="2",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("2")).place(x=150,y=250)
Button(win,height=1,width=5,text="3",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("3")).place(x=290,y=250)
Button(win,height=1,width=11,text="0",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show("0")).place(x=10,y=300)


Button(win,height=1,width=5,text=".",font=("arial,30,bold"),bd=1,fg="#fff",bg="gray",command=lambda: show(".")).place(x=290,y=300)
Button(win,height=3,width=5,text="=",font=("arial,30,bold"),bd=1,fg="#fff",bg="orange",command=lambda: cal()).place(x=430,y=250)
win.mainloop()

