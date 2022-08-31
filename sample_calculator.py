from tkinter import *

app = Tk()
app.title("CALCULATOR")
app.geometry("556x575")
app.resizable(True, True)
app.configure(bg="#17161b")

equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(app, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(app, text="C", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=lambda: clear()).place(x=10, y=120)
Button(app, text="/", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("/")).place(x=150, y=120)
Button(app, text="%", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("%")).place(x=290, y=120)
Button(app, text="*", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("*")).place(x=430, y=120)

Button(app, text="7", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("7")).place(x=10, y=210)
Button(app, text="8", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("8")).place(x=150, y=210)
Button(app, text="9", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("9")).place(x=290, y=210)
Button(app, text="-", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("-")).place(x=430, y=210)

Button(app, text="4", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("4")).place(x=10, y=305)
Button(app, text="5", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("5")).place(x=150, y=305)
Button(app, text="6", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("6")).place(x=290, y=305)
Button(app, text="+", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("+")).place(x=430, y=305)

Button(app, text="1", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("1")).place(x=10, y=400)
Button(app, text="2", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("2")).place(x=150, y=400)
Button(app, text="3", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("3")).place(x=290, y=400)
Button(app, text="0 ", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show("0")).place(x=10, y=492)

Button(app, text=".", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#242d36",
       command=lambda: show(".")).place(x=290, y=492)
Button(app, text="=", width=4, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: calculate()).place(x=430, y=400)

app.mainloop()
