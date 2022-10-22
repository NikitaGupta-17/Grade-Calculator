import tkinter
from tkinter import *

root = Tk() #Tk refers to new tkinter window
root.title("GRADE CALCULATOR") #title of new tkinter window
root.geometry("550x450")
root.configure(background='yellow')

def marks_calculate():
    maths = int(maths_value.get())
    science = int(science_value.get())
    computer = int(computer_value.get())
    final = (maths+science+computer)
    Label(text=f"{final}", bg='light green', font="Calibri 20 bold").place(x=250,y=170)

    average=int(final/3)
    Label(text=f"{average}", bg='light green', font="Calibri 20 bold").place(x=250,y=220)

    if average>50:
        grade_scored = "PASS"
    else:
        grade_scored = "FAIL"

    Label(text=f"{grade_scored}",bg='light green', font="Calibri 20 bold").place(x=250,y=270)
    Label(text="300",bg='light green', font="Calibri 20 bold").place(x=250,y=320)
    

sub_1 = Label(root, text="Maths", font="Calibri 20", bg ="yellow") #label is used to give some configuration
sub_1.place(x=50,y=20)

sub_2 = Label(root, text="Science", font="Calibri 20", bg ="yellow")
sub_2.place(x=50,y=70)

sub_3 = Label(root, text="Computer", font="Calibri 20", bg ="yellow")
sub_3.place(x=50,y=120)

total_marks = Label(root, text="Total", font="Calibri 20", bg ="yellow")
total_marks.place(x=50,y=170)

average_marks = Label(root, text="Average", font="Calibri 20", bg ="yellow")
average_marks.place(x=50,y=220)

grade_scored= Label(root, text="Grades", font="Calibri 20", bg ="yellow")
grade_scored.place(x=50,y=270)

max_marks = Label(root, text="Maximum Marks", font="Calibri 20", bg ="yellow")
max_marks.place(x=50,y=320)

maths_marks = StringVar()
science_marks = StringVar()
computer_marks = StringVar()

maths_value = Entry(root, textvariable = maths_marks, font="arial 20", bg='light green', width=15)
maths_value.place(x=250, y=20)

science_value = Entry(root, textvariable = science_marks, font="arial 20", bg='light green', width=15)
science_value.place(x=250, y=70)

computer_value = Entry(root, textvariable = computer_marks, font="arial 20", bg='light green', width=15)
computer_value.place(x=250, y=120)

Button(text="Calculator", font= "arial 15", bg ="green", bd=5,command=marks_calculate).place(x=50,y=370)
Button(text="Exit", font= "arial 15", bg ="red", bd=5,width=8,command=lambda: exit()).place(x=350,y=370)

root.mainloop()
