from tkinter import *
class asset:
    def debug():
        print("test succeeded")

    class grids:
        def addTextBox(win,text,x,y):
            T = Text(win)
            T.insert(INSERT,text)
            T.grid(column=x,row=y)

        def addLabel(win,text,x,y,colspan):
            L = Label(win,text=text).grid(column=x,row=y,columnspan=colspan,padx=3,pady=5)
            return L


        def addEntry(win,variable, x, y):
            E=Entry(win,textvariable=variable).grid(column=x,row=y)
            return E


        def addButton(win,text,x,y,span):
            B=Button(win,text=text).grid(column=x,row=y,columnspan=span)
            return B
        
        def addAuthButton(win,text,x,y,span):
            B=Button(win,text=text)
            B.bind('<ButtonRelease-1>',command=asset.process.basicLogin)
            return B.grid(column=x,row=y,columnspan=span)
        
        def emptyRow(root,row,colspan):
            L = Label(root,text="              \n").grid(column=0,row=row,columnspan=colspan)
            return L

    

    class packs:
        def addScrollBar(root,orient):
            if orient=='horizontal':
                ## do hrizontal bar
                bar = Scrollbar(root)
                return bar.pack(side=BOTTOM,fill=X)
            elif orient == 'vertical':
                bar = Scrollbar(root)
                return bar.pack(side=RIGHT, fill=Y)

        def addVertScrollFrame(root,*args,**kwargs):
                wid = Frame(root)
                if kwargs["text"]:
                    l=Label(wid,text=kwargs['text'])
                    l.pack(side=LEFT)
                asset.packs.addScrollBar(wid,'vertical')
                return wid.pack()
        
        def addTextBox(root,text):
                T = Text(root)
                T.insert(INSERT,text)
                T.pack()

        def addLabel(root,text):
            L = Label(root,text=text).pack()
            return L


        def addEntry(root):
            E=Entry(root).pack()
            return E


        def addButton(root,text):
            B=Button(root,text=text).pack()
            return B
        
   