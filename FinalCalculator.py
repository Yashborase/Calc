from tkinter import *
from tkinter.messagebox import *
import math as m
font=('verdana',15,'bold')
#----------functions----------------
def all_clear():
    textField.delete(0,END)
def clear():
    ex= textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)
def click_btn_function(event):
    print("clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='x':
        textField.insert(END,'*')
        return
    if text=='=':
        try:
            ex= textField.get()
            answer=eval(ex)
            textField.delete(0,END)
            textField.insert(0, answer)
        except Exception as e:
            showerror("Error",e)
        return
    textField.insert(END, text)
window= Tk()
window.title("My calculator")
window.geometry("400x500")
#---------picture label---------
pic=PhotoImage(file='img/calculator.png')
headinglable= Label(window,image=pic)
headinglable.pack(side=TOP,pady=10)

#-----------heading-----------------
heading=Label(window,text="My calculator",font=font)
heading.pack(side=TOP)

#----------text field--------------
textField=Entry(window,font=font,justify=CENTER,bd=5)
textField.pack(padx=10,pady=10,fill='x')

#--------------Buttons----------------

buttonFrame=Frame(window)
buttonFrame.pack(side=TOP)

#----------adding button--------------
temp=1
for i in range(0,3):
    for j in range(0, 3):
        btn=Button(buttonFrame,text=str(temp),font=font,bd=5,width=5,relief='ridge',activeforeground="orange",padx=3,pady=3)
        btn.grid(row=i,column=j)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)
Zerobtn=Button(buttonFrame,text='0',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
Zerobtn.grid(row=3,column=0)

dotbtn=Button(buttonFrame,text='.',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
dotbtn.grid(row=3,column=1)

equalbtn=Button(buttonFrame,text='=',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
equalbtn.grid(row=3,column=2)

plusbtn=Button(buttonFrame,text='+',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
plusbtn.grid(row=0,column=3)

minusbtn=Button(buttonFrame,text='-',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
minusbtn.grid(row=1,column=3)

multbtn=Button(buttonFrame,text='x',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
multbtn.grid(row=2,column=3)

divbtn=Button(buttonFrame,text='/',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
divbtn.grid(row=3,column=3)

clearbtn=Button(buttonFrame,text='<--',font=font,bd=5,width=12,relief='ridge',padx=3,pady=3,activeforeground="orange",command=clear)
clearbtn.grid(row=4,column=0,columnspan=2)

allClearbtn=Button(buttonFrame,text='Ac',font=font,bd=5,width=11,relief='ridge',padx=3,pady=3,activeforeground="orange",command=all_clear)
allClearbtn.grid(row=4,column=2,columnspan=4)

#--------------binding all buttons-----------------
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
multbtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)

Zerobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)

#========================Scientific calculator=====================
#---------------functions--------------------
scFrame=Frame(window)

sqrtbtn=Button(scFrame,text='SQRT',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
sqrtbtn.grid(row=0,column=0)

powbtn=Button(scFrame,text='^',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
powbtn.grid(row=0,column=1)

factbtn=Button(scFrame,text='x!',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
factbtn.grid(row=0,column=2)

radbtn=Button(scFrame,text='ToRad',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
radbtn.grid(row=0,column=3)

degbtn=Button(scFrame,text='ToDeg',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
degbtn.grid(row=1,column=0)

sinbtn=Button(scFrame,text='SinΘ',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
sinbtn.grid(row=1,column=1)

cosbtn=Button(scFrame,text='CosΘ',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
cosbtn.grid(row=1,column=2)

tanbtn=Button(scFrame,text='TanΘ',font=font,bd=5,width=5,relief='ridge',padx=3,pady=3,activeforeground="orange")
tanbtn.grid(row=1,column=3)

normalcalc=True

def calculate_sc(event):
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textField.get()
    answer=''

    if text == 'SQRT':
        print("cal sqrt")
        answer = str(m.sqrt((float(ex))))
    elif text=="^":
        print("cal pow")
        base,pow=ex.split(',')
        answer = m.pow(int(base),int(pow))
    elif text=="x!":
        print("cal factorial")
        answer = str (m.factorial(int(ex)))
    elif text=="ToRad":
        print("cal radian")
        answer = str(m.radians((float(ex))))
    elif text=="ToDeg":
        print("cal radium")
        answer=str(m.degrees((float(ex))))
    elif text=="SinΘ":
        print("cal radian")
        answer = str(m.sin((m.radians(int(ex)))))
    elif text=="CosΘ":
        print("cal cos")
        answer = str(m.cos((m.radians(int(ex)))))
    elif text=="TanΘ":
        print("cal Tan")
        answer = str(m.tan((m.radians(int(ex)))))

    textField.delete(0,END)
    textField.insert(0,answer)


def sc_click():
    global normalcalc
    if normalcalc:
        buttonFrame.pack_forget()
        scFrame.pack(side=TOP,pady=10)
        buttonFrame.pack(side=TOP)
        normalcalc=False
    else:
        scFrame.pack_forget()
        buttonFrame.pack(side=TOP)
        normalcalc=True


sqrtbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
degbtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)


menubar=Menu(window)
mode=Menu(menubar,tearoff=0)
mode.add_checkbutton(label="Scientific calculator",command=sc_click)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)







window.mainloop()
