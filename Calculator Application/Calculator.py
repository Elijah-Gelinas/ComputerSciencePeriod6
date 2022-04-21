# Elijah Gelinas and Branson Gibbs
import tkinter as tk

# Adds or removes text in text box
def add_text (text):
    global new_message
    if text == " ":
        new_message = ""
        message.set(new_message)
    else:
        new_message = new_message + text
        message.set(new_message)

#Creates window
WIN = tk.Tk()
WIN.title("Calculator")
WIN.geometry("600x500")
WIN.columnconfigure(0,weight=1)

# Calculator entry box
new_message = ""
message = tk.StringVar(WIN)
message.set(new_message)
num_box = tk.Entry(WIN,textvariable=message)
num_box.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Calculator Button 1
Num_Button1 = tk.Button(WIN, text='1')
Num_Button1.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.E))
Num_Button1.configure(command= lambda: add_text("1"))

# Calculator Button 2
Num_Button2 = tk.Button(WIN, text='2')
Num_Button2.grid(row=1, column=2, padx=5, pady=5, sticky=(tk.W))
Num_Button2.configure(command= lambda: add_text("2"))

# Calculator Button 3
Num_Button3 = tk.Button(WIN, text='3')
Num_Button3.grid(row=1, column=3, padx=5, pady=5, sticky=(tk.W))
Num_Button3.configure(command= lambda: add_text("3"))

# Calculator Button 4
Num_Button4 = tk.Button(WIN, text='4')
Num_Button4.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.E))
Num_Button4.configure(command= lambda: add_text("4"))

# Calculator Button 5
Num_Button5 = tk.Button(WIN, text='5')
Num_Button5.grid(row=2, column=2, padx=5, pady=5, sticky=(tk.W))
Num_Button5.configure(command= lambda: add_text("5"))

# Calculator Button 6
Num_Button6 = tk.Button(WIN, text='6')
Num_Button6.grid(row=2, column=3, padx=5, pady=5, sticky=(tk.W))
Num_Button6.configure(command= lambda: add_text("6"))

# Calculator Button 7
Num_Button7 = tk.Button(WIN, text='7')
Num_Button7.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.E))
Num_Button7.configure(command= lambda: add_text("7"))

# Calculator Button 8
Num_Button8 = tk.Button(WIN, text='8')
Num_Button8.grid(row=3, column=2, padx=5, pady=5, sticky=(tk.W))
Num_Button8.configure(command= lambda: add_text("8"))

# Calculator Button 9
Num_Button9 = tk.Button(WIN, text='9')
Num_Button9.grid(row=3, column=3, padx=5, pady=5, sticky=(tk.W))
Num_Button9.configure(command= lambda: add_text("9"))

# Calculator Button 0
Num_Button0 = tk.Button(WIN, text='0')
Num_Button0.grid(row=4, column=2, padx=5, pady=5, sticky=(tk.W))
Num_Button0.configure(command= lambda: add_text("0"))

# Calculator Button +
Button_add = tk.Button(WIN, text='+')
Button_add.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.E))
Button_add.configure(command= lambda: add_text("+"))

# Calculator Button -
Button_sub = tk.Button(WIN, text=' -')
Button_sub.grid(row=2, column=0, padx=5, pady=5, sticky=(tk.E))
Button_sub.configure(command= lambda: add_text("-"))

# Calculator Button x
Button_multi = tk.Button(WIN, text='x')
Button_multi.grid(row=3, column=0, padx=5, pady=5, sticky=(tk.E))
Button_multi.configure(command= lambda: add_text("x"))

# Calculator Button /
Button_div = tk.Button(WIN, text=' /')
Button_div.grid(row=4, column=0, padx=5, pady=5, sticky=(tk.E))
Button_div.configure(command= lambda: add_text("/"))

# Calculator Button Enter
Button_enter = tk.Button(WIN, text='Enter')
Button_enter.grid(row=4, column=1, padx=5, pady=5, sticky=(tk.W))
Button_enter.configure(command= lambda: add_text(" "))

# Calculator Button Clear
Button_clr = tk.Button(WIN, text='Clear')
Button_clr.grid(row=4, column=3, padx=5, pady=5, sticky=(tk.W))
Button_clr.configure(command= lambda: add_text(" "))



WIN.mainloop()