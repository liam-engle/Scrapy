from asset import *
def login(username):
        print("Logging in..."+username)


def main():
    win = Tk()
    win.title("Testing")
    win.configure(background="lightgrey")
    win.geometry("800x80")
    
    win.mainloop()

if(__name__=="__main__"):
    main()