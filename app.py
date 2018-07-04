from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image
import os


def predict_action():

    os.system('python ./code/label_image.py --image=./%s'%a)
    file = open("result.txt", "r")
    label_result.set("Result: ")
    output.set(file.read())
    loadGallery()
    tampil()



def open_action():
   global a
   filename = askopenfilename(parent=master, initialdir='C:\\')
   head, tail = os.path.split(filename)
   filePath.set(tail)
   loadImage(tail)
   a=tail
   
   

def loadImage(Tail):
   img = Image.open(Tail)
   img = img.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
   filename = ImageTk.PhotoImage(img)
   canvas = Canvas(master,height=250,width=250)
   canvas.image = filename  # <--- keep reference of your image
   canvas.create_image(0,0,anchor='nw',image=filename)
   canvas.grid(column=0, row = 1)



def loadImageDefault():
	tail =os.path.abspath('./res/desc/default_desc.jpg')
	img = Image.open(tail)
	img = img.resize((819, 720), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=900,width=800)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=1, row = 1, columnspan = 5, rowspan = 5)

def loadImageDefaultGal():
	tail =os.path.abspath('./res/desc/default_gal.jpg')
	img = Image.open(tail)
	img = img.resize((440, 240), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=440,width=440)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=0, row = 4, columnspan = 3)

def loadGallery():
	file = open("image_name.txt","r")
	imagedesc=file.read()
	tail =os.path.abspath('./res/desc/%s/%s_gal.jpg'%(imagedesc,imagedesc))
	img = Image.open(tail)
	img = img.resize((440, 240), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=440,width=440)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=0, row = 4, columnspan = 3)
	
def tampil():
	file = open("image_name.txt","r")
	imagedesc=file.read()
	tail =os.path.abspath('./res/desc/%s/%s_1.jpg'%(imagedesc,imagedesc))
	img = Image.open(tail)
	img = img.resize((819, 720), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=900,width=800)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=3, row = 1, columnspan = 5, rowspan = 5)
	
def tampil2():
	file = open("image_name.txt","r")
	imagedesc=file.read()
	tail =os.path.abspath('./res/desc/%s/%s_2.jpg'%(imagedesc,imagedesc))
	img = Image.open(tail)
	img = img.resize((819, 720), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=900,width=800)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=3, row = 1, columnspan = 5, rowspan = 5)
	
def tampil3():
	file = open("image_name.txt","r")
	imagedesc=file.read()
	tail =os.path.abspath('./res/desc/%s/%s_3.jpg'%(imagedesc,imagedesc))
	img = Image.open(tail)
	img = img.resize((819, 720), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=900,width=800)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=3, row = 1, columnspan = 5, rowspan = 5)
	
def tampil4():
	file = open("image_name.txt","r")
	imagedesc=file.read()
	tail =os.path.abspath('./res/desc/%s/%s_4.jpg'%(imagedesc,imagedesc))
	img = Image.open(tail)
	img = img.resize((819, 720), Image.ANTIALIAS) #The (250, 250) is (height, width)
	filename = ImageTk.PhotoImage(img)
	canvas = Canvas(master,height=900,width=800)
	canvas.image = filename  # <--- keep reference of your image
	canvas.create_image(0,0,anchor='nw',image=filename)
	canvas.grid(column=3, row = 1, columnspan = 5, rowspan = 5)
	


master = Tk()

#master.columnconfigure(1, weight=1)
#master.columnconfigure(3, pad=7)
#master.rowconfigure(1, weight=1)
#master.rowconfigure(5, pad=7)

filePath = StringVar(None)
output = StringVar(None)
label_result = StringVar(None)
imagedesc = StringVar(None)
idesc = StringVar(None)
loadImageDefault()


e1 = Entry(master,textvariable=filePath, width='30', state='disabled')
e1.grid(row=0, column=0)

b1 = Button(master, text="choose image file", command=open_action)
b1.grid(row=0, column=1)

b2 = Button(master, text="Predict", command=predict_action)
b2.grid(row=0, column=2)



b3 = Button(master,text="Physical & Chemical Properties", command=tampil)
b3.grid(row=0, column=3)

b4 = Button(master,text="Optical Data & Cristallogprahy", command=tampil2)
b4.grid(row=0, column=4)

b5 = Button(master,text="Occourance", command=tampil3)
b5.grid(row=0, column=5)

b6 = Button(master,text="Other Information", command=tampil4)
b6.grid(row=0, column=6)

l0 = Label(master, text="label", textvariable=output)
l0.grid(row=3)

l2 = Label(master, text="Result :", textvariable=label_result)
l2.grid(row=2)

l1 = Label(master, text="Isi text", textvariable=imagedesc)
l1.grid(row=2,column=1)


mainloop( )

