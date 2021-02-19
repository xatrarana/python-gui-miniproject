from tkinter import *

def click(event):
    global scvalue                              #making scvlaue global
    text = event.widget.cget("text")                  #geting text form the frame into text variable                                  #printing the geting value of text
    if text == '=':                        #if text value is equal to the = then it make the calculation
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())    ##evaluate the string
            except Exception as e:
                print(e)
                value= "eror"        # error handling with try block
             

        scvalue.set(value)
        screen.update()
    elif text == 'c':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)         # set the scvlaue in the screen
        screen.update()
        


root = Tk()                            #staring the tkinter
root.geometry("650x700")               # set the frame of the application
root.title("calculator")       # set tittle for the application
#root.wm_iconbitmap(r"melody.ico")


scvalue= StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold") 
screen.pack(fill=X, ipadx=8, ipady=10, padx=10)



f = Frame(root, )

b = Button(f, text="@",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="$",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="~",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="c",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT, padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root, )

b = Button(f, text="7",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)                                         #made frame and made button inside the frame and bind with the click event

b = Button(f, text="8",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="9",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="+",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()



f = Frame(root, )

b = Button(f, text="4",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)                                  #made frame and made button inside the frame and bind with the click event

b = Button(f, text="5",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="6",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="-",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, )

b = Button(f, text="1",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)                                  #made frame and made button inside the frame and bind with the click event

b = Button(f, text="2",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="3",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="*",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root, )

b = Button(f, text="1",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)                                  #made frame and made button inside the frame and bind with the click event

b = Button(f, text="2",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT ,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="3",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="/",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root )
b = Button(f,text="%",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT, padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="0",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT, padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text=".",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT, padx=15,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=15,pady=14,font="lucida 20 bold")
b.pack(side=LEFT, padx=15,pady=12)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()