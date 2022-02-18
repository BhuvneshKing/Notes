#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[importing module's]

from tkinter import *
from time import sleep   
from tracemalloc import stop
from tkinter import messagebox
import datetime

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading frame ]

def nike():

    ro=Tk()
    ro.config(bg="black")
    ro.title("Loading")
    # ro.geometry("350x300+300+300")
    ro.attributes("-fullscreen",True)
    # ro.attributes('-transparentcolor','black')
    # ro.state('zoomed')
    Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
    for i in range (16):
        Label(ro,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
        ro.update()
        for i in range(3):
            for j in range(16):
                Label(ro,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(0.06)
                ro.update_idletasks()
                Label(ro,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
                stop()
        else:
            ro.destroy()
            ok()
            break
            
    ro.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame structure]

def ok():

    root = Tk()
    root.geometry("350x300+300+300")
    root.title("Notes")
    root.iconbitmap("notebook.ico")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save function]

    def save():
        r=Tk()
        r.geometry("210x70+300+300")
        r.iconbitmap("notebook.ico")
        r.title("Save")
        Label(r, text="Save with the name .....",bg="#1F2732",fg="#FFBD09").grid(sticky=W, pady=4, padx=5)
        r.config(bg="#1F2732")
        def printIn():
            j = jk.get(1.0, "end-1c") 
            strDate = datetime.datetime.now().strftime("%d:%B:%y")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            inp = area.get(1.0, "end-1c")
            foo=open(f"{j}.txt","w")
            foo.write(f" Note of the  Date:- {strDate} \n while time was {strTime}")
            foo.write("\n")
            foo.write(inp)
            foo.close()
            messagebox.showinfo("Message","your file as saved") 
            r.destroy()
            print(j)
        jk = Text(r,height=1,width=5,relief=RIDGE,bd=0)
        jk.grid(row=1, column=0,padx=5,ipady=3, sticky=E+W+S+N)
        hi=Button(r, text="Save",command=printIn,bg="#1F2732",fg="#FFBD09",borderwidth=2)
        hi.grid(row=1, column=3)
        def changex(event):
            hi['bg']='#3e4042'
        def returnx(event):
            hi['bg']="#1F2732"
        hi.bind('<Enter>',changex)
        hi.bind('<Leave>',returnx)
        r.mainloop() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[viewing function]

    def printInput():
        inp = area.get(1.0, "end-1c")
        print(inp)
        rt=Tk()
        rt.title("View")
        rt.iconbitmap("notebook.ico")
        rt.config(bg="#1F2732")
        rt.geometry("350x300+300+300")
        Label(rt,text="The text you have wrote",bg="#1F2732",fg="#FFBD09", pady=15).grid(sticky=NW)
        Label(rt,text=inp,bg="#1F2732",fg="white").grid(sticky=E+W+S+N)
        rt.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[joing row and column]

    root.config(bg="#1F2732")
    root.columnconfigure(1, weight=1)
    root.columnconfigure(3, pad=7)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(5, pad=7)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[labeling the text]

    lbl = Label(root,text="Don't forget to save before closing",bg="#1F2732",fg="#FFBD09")
    lbl.grid(sticky=W, pady=4, padx=5)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[entery taking]
    area = Text(root,bg='#3e4042',fg="white",relief=RIDGE,bd=0)
    area.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E+W+S+N)
    inp = area.get(1.0, "end-1c") 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[view button]

    abtn = Button(root,text="view",command=printInput,bg="#1F2732",fg="#FFBD09",borderwidth=0)
    abtn.grid(row=1, column=3,ipadx=2)
    def changex(event):
        abtn['bg']='#3e4042'
    def returnx(event):
        abtn['bg']="#1F2732"
    abtn.bind('<Enter>',changex)
    abtn.bind('<Leave>',returnx)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[colse button]

    close=Button(root, text='  close  ', command=root.destroy,bg="#1F2732",fg="#FFBD09",bd=0,highlightthickness=0,borderwidth=0)
    close.grid(row=2, column=3, pady=4)
    def changex(event):
        close['bg']='red'
    def returnx(event):
        close['bg']="#1F2732"
    close.bind('<Enter>',changex)
    close.bind('<Leave>',returnx)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about button]

    hbtn = Button(root,text="about",bg="#1F2732",fg="#FFBD09",borderwidth=0,command=aboutview)
    hbtn.grid(row=5, column=0, padx=5,sticky=W)
    def changex(event):
        hbtn['bg']='#3e4042'
    def returnx(event):
        hbtn['bg']="#1F2732"
    hbtn.bind('<Enter>',changex)
    hbtn.bind('<Leave>',returnx)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save button]

    obtn = Button(root, text="Save",command=save,bg="#1F2732",fg="#FFBD09",borderwidth=0)
    obtn.grid(row=5, column=3)
    def changex(event):
        obtn['bg']='#3e4042'
    def returnx(event):
        obtn['bg']="#1F2732"
    obtn.bind('<Enter>',changex)
    obtn.bind('<Leave>',returnx)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame close]

    root.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about creator]
def aboutview():
    aro=Tk()
    aro.config(bg="#1F2732")
    #ro.config(bg="black")
    aro.title("About")    
    aro.iconbitmap("notebook.ico")
    aro.geometry("350x300+300+300")
    Label(aro,text="About me :-",font="Bahnschrift 19",bg="#1F2732",fg="#FFBD09").pack(anchor=NW)   
    Label(aro,
    text=
    """my self bhuvnesh verma .
    The application is created with the
      help of python and tkinter 
        hopefully you like it  .""",font="calibri 15",bg="#1F2732",fg="white").pack(anchor=NW)
    closei=Button(aro, text='  close  ', command=aro.destroy,bg='#10121f',font=("calibri", 13),bd=0,fg='white',highlightthickness=0,pady=3)
    closei.pack(padx=50,pady=50)
    def changex(event):
        closei['bg']='red'
    def returnx(event):
        closei['bg']='#10121f'
    closei.bind('<Enter>',changex)
    closei.bind('<Leave>',returnx)
    aro.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Runing the application]

if __name__=="__main__":
    nike()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[The End.]