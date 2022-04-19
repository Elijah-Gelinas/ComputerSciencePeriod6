import tkinter as tk
from messageClass import Message

def on_submit():
    message = message_var.get()
    message = message.lower()
    if message == "":
        return
    my_message = Message(message, 3)
    encoded_var.set(my_message.encrypted)

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x600")
root.columnconfigure(1,weight=1)

# 1st row
message_var = tk.StringVar(root)
message_label = tk.Label(
    root,
    text='Enter message to encode: ',
    bg='red',
    fg='white',
    font=("Arial 16 bold")
)
message_label.grid(row=0, column=0, sticky=(tk.E, tk.W))
message_input = tk.Entry(
    root,
    textvariable=message_var
)
message_input.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=10)

# 2nd row
encoded_var = tk.StringVar(root)
encoded_label = tk.Label(
    root,
    text='Here is your encoded message: ',
    bg='green',
    fg='white',
    font=("Arial 16 bold")
)
encoded_label.grid(row=1, column=0, sticky=tk.E)
encoded_input = tk.Entry(
    root,
    textvariable=encoded_var
)
encoded_input.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=10)

# 3rd row
submit_button = tk.Button(root, text="Encode")
submit_button.grid(row=2, column=1, padx=10,pady=25, sticky=(tk.E))
submit_button.configure(command=on_submit)



root.mainloop()