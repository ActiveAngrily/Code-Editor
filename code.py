import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading
import os


name = "untilted.py"
directory = name
default_directory = "/temp/"+name
fd = open(directory,'w+').close()
output = " "
chk = True
run_time = 1 # in seconds


def run ():
	global output
	global directory
	save ()
	try:
		output=os.popen(directory).read()
		global output_text
		output_text.configure(state='normal')
		output_text.delete(1.0,'end-1c')
		output_text.insert(1.0,output)
		output_text.configure(state='disabled')
	except:
		pass
		
def new ():
	global directory
	global fd
	fd = open(directory,"w+").close()

def openf ():
	global directory
	global fd
	global code_text
	global name
	directory = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("python files","*.py"),("all files","*.*")))

	fd = open(directory)
	code_text.delete(1.0,'end-1c')
	code_text.insert(1.0,fd.read())
	fd.close()


def save ():
	#save file
	global directory
	global fd
	fd = open(directory,"w")
	fd.write(code_text.get(1.0,'end-1c'))
	fd.close()


def saveas ():
	#save file in new directory
	global directory
	global fd
	directory = filedialog.asksaveasfilename(initialdir="/",title="Save As",filetypes=(("python files","*.py"),("all files","*.*")))
	save()

def exitf ():
	global name
	answer=messagebox.askyesnocancel(message="do you want to save changes to"+name+"before exiting")
	try:
		if(answer==True):
			save()
		if(answer==False):
			root.destroy()
			chk = False
		if(answer==None):
			pass
	except:
		pass



def create_menu ():
	menu=tk.Menu(root)

	file = tk.Menu(menu)

	file.add_command(label="New",command=new)
	file.add_command(label="Open",command=openf)
	file.add_separator()

	file.add_command(label="Save",command=save)
	file.add_command(label="Save As...",command=saveas)
	file.add_separator()

	file.add_command(label="Exit",command=exitf)
	file.add_command(label="Break",command=lambda:chk==False)#disables auto running
	menu.add_cascade(label="File",menu=file)
	menu.add_command(label="Run",command=run)

	root.config(menu=menu)

root = tk.Tk()

root.title("Code Editor")
create_menu ()


#create frame
f_main = tk.Frame(root,height=500,width=600)

xscrollbar = tk.Scrollbar(f_main,orient=tk.HORIZONTAL)
xscrollbar.pack(side=tk.BOTTOM,fill=tk.X)

yscrollbar = tk.Scrollbar(f_main)
yscrollbar.pack( side = tk.RIGHT, fill = tk.Y )

code_text = tk.Text(f_main,relief=tk.RAISED,padx=3,pady=3,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)

code_text.pack(fill=tk.BOTH,expand=1)

f_main.pack(fill=tk.BOTH,expand=1)
#end create frame

#create another frame
out_frame = tk.Frame(root,height=200,width=600)
xscrollbar_z = tk.Scrollbar(out_frame,orient=tk.HORIZONTAL)
xscrollbar_z.pack(side=tk.BOTTOM,fill=tk.X)

yscrollbar_z = tk.Scrollbar(out_frame)
yscrollbar_z.pack(side=tk.RIGHT, fill = tk.Y )

output_text = tk.Text(out_frame,bg='black',relief=tk.FLAT,padx=5,pady=5,fg='#DEDEDE',state='disabled',yscrollcommand=yscrollbar_z.set,xscrollcommand=xscrollbar_z.set)
output_text.pack(fill=tk.BOTH,expand=1)

out_frame.pack(fill=tk.BOTH,side=tk.BOTTOM)
#end create another frame

def Update ():
    global code_text
    if(chk == True):
        s = threading.Timer(run_time, Update).start()
    if(chk==False):
        pass
    if(chk==None):
        pass
    run()

Update()

root.mainloop()

chk=False
