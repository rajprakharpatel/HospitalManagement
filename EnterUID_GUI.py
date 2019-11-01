import tkinter as tk


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master, width=20, command=None)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


k = str()


def uid():
    msg = tk.Tk()
    msg.title("Enter Unique ID")
    msg.geometry('300x100')

    lbl = tk.Label(msg, text="UID:", font=("Arial Bold", 14))
    lbl.grid(column=0, row=0, padx=20, pady=20)
    id_ = EntryWithPlaceholder(msg, placeholder="Enter Unique ID")
    id_.grid(column=1, row=0, padx=20, pady=20)
    id_.focus()

    def destroy():
        global k
        k = id_.get()
        msg.quit()
        msg.destroy()

    btn = tk.Button(msg, text="OK", command=destroy)
    btn.grid(column=2, row=0, padx=10, pady=20)

    msg.mainloop()
    return int(k)


if __name__ == '__main__':
    print(uid())
