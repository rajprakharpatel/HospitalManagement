from Record import *


class Patient(Record):
    __rec = list()

    def __init__(self, name=None, illness=None, gender=None, age=None):
        if name and illness and gender and age is not None:
            self.name = name
            self.illness = illness
            self.age_ = age
            self.gender = gender
        else:
            self.pa_w = Tk()
            self.pa_w.title("Patient")
            self.pa_w.geometry('960x540')
            self.nm_lbl = Label(self.pa_w, text="Name:")
            self.nm_lbl.grid(column=0, row=0, padx=(10, 0))
            self.nm = Entry(self.pa_w, width=50)
            self.nm.grid(column=1, row=0, padx=20, pady=10)

            self.ad_lbl = Label(self.pa_w, text="Address")
            self.ad_lbl.grid(column=0, row=1, padx=(10, 0))
            self.adr = Entry(self.pa_w, width=50)
            self.adr.grid(column=1, row=1, padx=20, pady=10)

            self.age_lbl = Label(self.pa_w, text="Age:")
            self.age_lbl.grid(column=0, row=2, padx=(10, 0))
            self.age = Entry(self.pa_w, width=50)
            self.age.grid(column=1, row=2, padx=20, pady=10)

            self.sex_lbl = Label(self.pa_w, text="Gender:")
            self.sex_lbl.grid(column=0, row=3, padx=(10, 0))
            self.sex = Entry(self.pa_w, width=50)
            self.sex.grid(column=1, row=3, padx=20, pady=10)

            self.ill_lbl = Label(self.pa_w, text="Illness:")
            self.ill_lbl.grid(column=0, row=4, padx=(10, 0))
            self.ill = Entry(self.pa_w, width=50)
            self.ill.grid(column=1, row=4, padx=20, pady=10)

            self.save = Button(self.pa_w, text="Save", command=self.save)
            self.save.grid(column=0, row=5, padx=(40, 0), pady=10)

            self.exit = Button(self.pa_w, text="Done", command=self.destroy)
            self.exit.grid(column=1, row=5, padx=(40, 0), pady=10)

            self.pa_w.mainloop()

    def str_value(self):
        return {"Name": self.name,
                "Illness": self.illness,
                "Age": self.age_,
                "Gender": self.gender}

    def destroy(self):
        self.pa_w.quit()
        self.pa_w.destroy()

    def save(self):
        self.name = self.nm.get()
        self.illness = self.ill.get()
        self.gender = self.sex.get()
        self.age_ = self.age.get()

    @classmethod
    def add_rec(cls):
        cls.__rec.append(Patient())
        messagebox.showinfo("Unique id", len(cls.__rec))

    @classmethod
    def mod_rec(cls):
        k_ = uid() - 1
        x = cls.get_rec(k_)
        if x is not None:
            cls.__rec.insert(k_, Patient())

    @classmethod
    def del_rec(cls):
        k_ = uid() - 1
        if k_ < len(cls.__rec):
            if messagebox.askyesno("Deletion", "Are you sure"):
                cls.__rec.insert(k_, "Deleted")
                messagebox.showinfo("Deleted", "Any associated appointments will have to be deleted manually")
        else:
            messagebox.showerror("Error!", "Record does not exist")

    @classmethod
    def disp_rec(cls):
        k_ = uid() - 1
        x = cls.get_rec(k_)
        if x is not None:
            recDisp(x.str_value())

    @classmethod
    def get_rec(cls, n):
        if n < len(cls.__rec):
            if cls.__rec[n] != "Deleted":
                return cls.__rec[n]
            else:
                messagebox.showerror("No Patient with such ID",
                                     " The record for that Patient was deleted")
        else:
            messagebox.showerror("No Patient with such ID",
                                 " The record for that Patient doesn't exist")

    @classmethod
    def load_json(cls):
        rec = loads("pat_rec.json")
        for i in rec:
            cls.__rec.append(Patient(name=i["Name"], illness=i["Illness"],
                                     age=i["Age"], gender=i["Gender"]))

    @classmethod
    def write_json(cls):
        rec = list()
        for i in cls.__rec:
            rec.append(i.str_value())


if __name__ == '__main__':
    pat = Patient()
    pat.disp_rec()
