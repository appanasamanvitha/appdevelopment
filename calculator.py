import tkinter as tk

LARGE = ("Monaco", 30, "bold")
SMALL = ("Monaco", 16)
DIGITS = ("Monaco", 24, "bold")
DEFAULT = ("Monaco", 20)

white9 = "#F5F5F5"
white = "#FFFFFF"
lightblue = "#CED682"
gray = "#F5F5F5"
turch = "#F20D5C"


class Calc:
    def __init__(self):
        self.dis = tk.Tk()
        self.dis.geometry("375x667")
        self.dis.resizable(0, 0)
        self.dis.title("CALCULATOR")

        self.totalexp = ""
        self.currentexp = ""
        self.displayframe = self.displayframe()

        self.totallabel, self.label = self.displaylabels()

        self.digitss = {
            1: (1, 1), 2: (1, 2), 3: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operation = {"/": "\u00F7", "*": "\u00D7", "+": "+", "-": "-"}
        self.buttonsframe = self.buttonsframe()

        self.buttonsframe.rowconfigure(0, weight=2)
        for x in range(1, 5):
            self.buttonsframe.rowconfigure(x, weight=2)
            self.buttonsframe.columnconfigure(x, weight=2)
        self.digitbuttons()
        self.operatorbuttons()
        self.specialbuttons()
        self.keys()

    def keys(self):
        self.dis.bind("<Return>", lambda event: self.evaluate())
        for key in self.digitss:
            self.dis.bind(str(key), lambda event, digit=key: self.addtoexpression(digit))

        for key in self.operation:
            self.dis.bind(key, lambda event, operator=key: self.appendoperator(operator))

    def specialbuttons(self):
        self.clearbutton()
        self.equalsbutton()
        self.squarebutton()
        self.sqrtbutton()

    def displaylabels(self):
        totallabel = tk.Label(self.displayframe, text=self.totalexp, anchor=tk.E, bg=gray,
                               fg=turch, padx=24, font=SMALL)
        totallabel.pack(expand=True, fill='both')

        label = tk.Label(self.displayframe, text=self.currentexp, anchor=tk.E, bg=gray,
                         fg=turch, padx=24, font=LARGE)
        label.pack(expand=True, fill='both')

        return totallabel, label

    def displayframe(self):
        framee = tk.Frame(self.dis, height=221, bg=gray)
        framee.pack(expand=True, fill="both")
        return framee

    def addtoexpression(self, value):
        self.currentexp += str(value)
        self.updatelabel()

    def digitbuttons(self):
        for digit, grid_value in self.digitss.items():
            butt = tk.Button(self.buttonsframe, text=str(digit), bg=white, fg=turch, font=DIGITS,
                               borderwidth=0, command=lambda x=digit: self.addtoexpression(x))
            butt.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def appendoperator(self, operator):
        self.currentexp += operator
        self.totalexp += self.currentexp
        self.currentexp = ""
        self.updatetotallabel()
        self.updatelabel()

    def operatorbuttons(self):
        i = 0
        for operator, symbol in self.operation.items():
            butt = tk.Button(self.buttonsframe, text=symbol, bg=white9, fg=turch, font=DEFAULT,
                               borderwidth=0, command=lambda x=operator: self.appendoperator(x))
            butt.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.currentexp = ""
        self.totalexp = ""
        self.updatelabel()
        self.updatetotallabel()

    def clearbutton(self):
        butt = tk.Button(self.buttonsframe, text="C", bg=white9, fg=turch, font="BOLD",
                           borderwidth=0, command=self.clear)
        butt.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.currentexp = str(eval(f"{self.currentexp}**2"))
        self.updatelabel()

    def squarebutton(self):
        butt = tk.Button(self.buttonsframe, text="x\u00b2", bg=white9, fg=turch, font=  "BOLD",
                           borderwidth=0.1, command=self.square)
        butt.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.currentexp = str(eval(f"{self.currentexp}**0.5"))
        self.updatelabel()

    def sqrtbutton(self):
        butt = tk.Button(self.buttonsframe, text="\u221ax", bg=white9, fg=turch, font=  "BOLD",
                           borderwidth=0.1, command=self.sqrt)
        butt.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.totalexp += self.currentexp
        self.updatetotallabel()
        try:
            self.currentexp = str(eval(self.totalexp))

            self.totalexp = ""
        except Exception as e:
            self.currentexp = "Error"
        finally:
            self.updatelabel()

    def equalsbutton(self):
        butt = tk.Button(self.buttonsframe, text="=", bg=lightblue, fg=turch, font="BOLD",
                           borderwidth=0, command=self.evaluate)
        butt.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def buttonsframe(self):
        framee = tk.Frame(self.dis)
        framee.pack(expand=True, fill="both")
        return framee

    def updatetotallabel(self):
        expression = self.totalexp
        for operator, symbol in self.operation.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.totallabel.config(text=expression)

    def updatelabel(self):
        self.label.config(text=self.currentexp[:11])

    def run(self):
        self.dis.mainloop()


if __name__ == "__main__":
    calcul = Calc()
    calcul.run()