from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from PIL import ImageTk,Image

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('600x380') #ขนาด

########################################## ใส่รูป
canvas = Canvas(GUI, width=600, height=380)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("money.jpg"))  
canvas.create_image(0, 0, anchor=NW, image=img) 
###########################################หัวข้อ
L1 = Label(GUI,text='รับ-จ่าย',font=('Angsana New',30),fg='black')
L1.place(x=270,y=20)
###########################################
def Button2():
    text = 'จำนวนเงินที่รับ'
    
    messagebox.showinfo('รายรับ',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=140,y=100)
B2 = ttk.Button(FB2, text='รายรับ',command=Button2)
B2.pack(ipadx=20,ipady=10)
###########################################
def Button3():
    text = 'จำนวนเงินที่จ่าย'
    messagebox.showwarning('รายจ่าย',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=370,y=100)
B3 = ttk.Button(FB3, text='รายจ่าย',command=Button3)
B3.pack(ipadx=20,ipady=10)

GUI.mainloop()
