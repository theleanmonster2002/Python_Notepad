from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


# FUNCTIONS
def newfile():
    with open(filename, 'w') as file:
        file.write('Hello, this is a new file created using Python!\n')
        file.write('You can add more lines of text here.')
        print(f'{filename} has been created and written to successfully.')
        
def cutt():
    text_area.event_generate(("<<Cut>>"))
    
def copyy():
    text_area.event_generate(("<<Copy>>"))

def pastee():
    text_area.event_generate(("<<Paste>>"))
    
def aboutt():
    a= tmsg.showinfo("Notepad", "Notepad by Arpit Arora")
    
def exitt():
    quit= tmsg.askquestion("Notepad", "Do you want to exit?")
    if quit== "yes":
        root.destroy()
    else:
        pass
    
def openn():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "": 
        file= None
    else: #to open file
        root.title(os.path.basename(file)+ "- Notepad")
        text_area.delete(1.0, END)
        f= open(file, "r")  
        text_area.insert(1.0, f.read())  
        f.close()
        
def savefile():
    global file
    if file== None:
        file= asksaveasfilename(initialfile='Untittled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file== "":
            file= None
        else:
            # save as new file
            f=open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ "- Notepad")
            print("file saved")
    else:
        # save the new file
        f=open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
    
        
        
if __name__ == '__main__':
    root=Tk()
root.geometry("600x550")
root.title("United- Notepad")
root.wm_iconbitmap("Notepad.ico")


mainmenu= Menu(root)
m1= Menu(mainmenu, tearoff=0)
m1.add_command(label="New file", command=newfile)
m1.add_command(label="New window")
m1.add_command(label="Open", command=openn)
m1.add_command(label="Save")
m1.add_command(label="Save as", command=savefile)
m1.add_command(label="Save all")
m1.add_separator()
m1.add_command(label="Page setup")
m1.add_command(label="Print")
m1.add_separator()
m1.add_command(label="Close tab")
m1.add_command(label="Close window")
m1.add_command(label="Exit", command=exitt)


mainmenu.add_cascade(label="File", menu=m1)

m2= Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo")
m2.add_separator()
m2.add_command(label="Cut", command=cutt)
m2.add_command(label="Copy", command=copyy)
m2.add_command(label="Paste", command=pastee)
m2.add_command(label="Delete")
m2.add_separator()
m2.add_command(label="Search with Being")
m2.add_separator()
m2.add_command(label="Find")
m2.add_command(label="Find next")
m2.add_command(label="Find previous")
m2.add_command(label="Replace")
m2.add_command(label="Goto")
m2.add_separator()
m2.add_command(label="Select all")
m2.add_command(label="Time/Date")
m2.add_separator()
m2.add_command(label="Font")
mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Zoom")
m3.add_command(label="Status bar")
m3.add_command(label="Word wrap")

mainmenu.add_cascade(label="View", menu=m3)

m4= Menu(mainmenu, tearoff=0)
m4.add_command(label="About", command=aboutt)
mainmenu.add_cascade(label="Help", menu=m4)

# file for new file
filename = 'new_file.txt'

scroll1= Scrollbar(root)
scroll1.pack(side=RIGHT,fill=BOTH)

text_area= Text(root, font="lucida 10", yscrollcommand=scroll1.set)
text_area.pack(fill=BOTH, expand=TRUE)
file= None

scroll1.config(command= text_area.yview)

root.config(menu=mainmenu)

root.mainloop()
    


