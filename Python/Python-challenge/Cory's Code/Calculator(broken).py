__author__ = 'ColeDixon'

from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self, master):
        
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
               

        #MASTER SETTINGS
        master.title('CALCULATOR')
        # master.resizable(False, False) Commented out, I like to be able to resize :P

        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text = 'Python Calculator').grid(row = 0, column = 2, sticky = 'e')
        self.input = ttk.Label(self.header_frame).grid(row = 1, column = 0, columnspan = 4)
        self.num_entry = ttk.Entry(self.input)
        self.num_entry.pack(padx = 10, pady = 5)
        # self.num_entry.insert(0, "0")

        #SEPARATOR
        self.separator = ttk.Frame(height = 2, relief = SUNKEN)
        self.separator.pack(fill = X, padx = 5, pady = 5)

        #PANEL
        self.panel = ttk.Frame(master)
        self.panel.pack()

        #NUMBER BUTTONS
        self.one = ttk.Button(self.panel, text = '1', width = 3)
        self.one.grid(row = 3, column = 0, padx = 2, pady = 1)
        self.two = ttk.Button(self.panel, text = '2', width = 3)
        self.two.grid(row = 3, column = 1, padx = 2, pady = 1)
        self.three = ttk.Button(self.panel, text = '3', width = 3)
        self.three.grid(row = 3, column = 2, padx = 2, pady = 1)
        self.four = ttk.Button(self.panel, text = '4', width = 3)
        self.four.grid(row = 4, column = 0, padx = 2, pady = 1) # changed but should not have any effect?
        self.five = ttk.Button(self.panel, text = '5', width = 3)
        self.five.grid(row = 4, column = 1, padx = 2, pady = 1)
        self.six = ttk.Button(self.panel, text = '6', width = 3)
        self.six.grid(row = 4, column = 2, padx = 2, pady = 1)
        self.seven = ttk.Button(self.panel, text = '7', width = 3)
        self.seven.grid(row = 5, column = 0, padx = 2, pady = 1)
        self.eight = ttk.Button(self.panel, text = '8', width = 3)
        self.eight.grid(row = 5, column = 1, padx = 2, pady = 1)
        self.nine = ttk.Button(self.panel, text = '9', width = 3, command=self.num_press(9)) # changed to conform to width
        self.nine.grid(row = 5, column = 2, padx = 2, pady = 1) # change from pack to grid
        self.zero = ttk.Button(self.panel, text = '0', width = 9, command=self.num_press(0)) # changed to conform to Clear button
        self.zero.grid(row = 6, column = 0, columnspan = 2, padx = 2, pady = 1) # changed colspan to columnspan
        self.dec = ttk.Button(self.panel, text = '.', width = 3)
        self.dec.grid(row = 6, column = 2, padx = 2, pady = 1)
       
        #OPERATOR BUTTONS
        self.add = ttk.Button(self.panel, text = '+', width = 4)
        self.add.grid(row = 3, column = 3, padx = 5, pady = 1)
        self.sub = ttk.Button(self.panel, text = '-', width = 4)
        self.sub.grid(row = 4, column = 3, padx =5, pady = 1)
        self.multi = ttk.Button(self.panel, text = '*', width = 4)
        self.multi.grid(row = 5, column = 3, padx = 5, pady = 1)
        self.div = ttk.Button(self.panel, text = '/', width = 4)
        self.div.grid(row = 6, column = 3, padx = 5, pady = 1)
        self.equal = ttk.Button(self.panel, text = '=', width = 10)
        self.equal.grid(row = 7, column = 2, columnspan = 2, padx = 2, pady = 1)
        self.clear = ttk.Button(self.panel, text = 'CLEAR', width = 9, command=self.cancel)
        self.clear.grid(row = 7, column = 0, columnspan = 2, padx = 2, pady = 1)      

    def num_press(self, num):
        self.eq = False
        temp = self.num_entry.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)        
    
    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
            self.num_entry.delete(0, END)
            self.num_entry.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(self.num_entry.get()))
        self.display(self.current)

       

def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__": main()
