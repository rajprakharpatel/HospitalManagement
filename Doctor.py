from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from EnterUID_GUI import *
from JsonMng import loads, dumps


class Doctor:
    __rec_doc = list()

    def __init__(self, name=None, qualification=None, gender=None, age=None):
        if name is not None:
            self.age_ = age
            self.gender = gender
            self.qualification = qualification
            self.name = name
        else:
            self.dc_w = Tk()
            self.dc_w.title("Doctor")
            self.dc_w.geometry('960x540')
            self.nm_lbl = Label(self.dc_w, text="Name:")
            self.nm_lbl.grid(column=0, row=0, padx=(10, 0))
            self.nm = Entry(self.dc_w, width=50)
            self.nm.grid(column=1, row=0, padx=20, pady=10)

            self.ad_lbl = Label(self.dc_w, text="Address")
            self.ad_lbl.grid(column=0, row=1, padx=(10, 0))
            self.adr = Entry(self.dc_w, width=50)
            self.adr.grid(column=1, row=1, padx=20, pady=10)

            self.age_lbl = Label(self.dc_w, text="Age:")
            self.age_lbl.grid(column=0, row=2, padx=(10, 0))
            self.age = Entry(self.dc_w, width=50)
            self.age.grid(column=1, row=2, padx=20, pady=10)

            self.sex_lbl = Label(self.dc_w, text="Gender:")
            self.sex_lbl.grid(column=0, row=3, padx=(10, 0))
            self.sex = Entry(self.dc_w, width=50)
            self.sex.grid(column=1, row=3, padx=20, pady=10)

            self.qul_lbl = Label(self.dc_w, text="Qualification:")
            self.qul_lbl.grid(column=0, row=4, padx=(10, 0))
            self.qual = Entry(self.dc_w, width=50)
            self.qual.grid(column=1, row=4, padx=20, pady=10)

            self.save = Button(self.dc_w, text="Save", command=self.save)
            self.save.grid(column=0, row=5, padx=(40, 0), pady=10)

            self.exit = Button(self.dc_w, text="Done", command=self.destroy)
            self.exit.grid(column=1, row=5, padx=(40, 0), pady=10)

            self.dc_w.mainloop()

    # def __str__(self):
    #     return {"Name": self.name,
    #             "Qualification": self.qualification,
    #             "Age": self.age_,
    #             "Gender": self.gender}

    def destroy(self):
        self.dc_w.quit()
        self.dc_w.destroy()

    def save(self):
        self.name = self.nm.get()
        self.qualification = self.qual.get()
        self.gender = self.sex.get()
        self.age_ = self.age.get()

    @classmethod
    def add_rec(cls):
        cls.__rec_doc.append(Doctor())
        messagebox.showinfo("Unique id", len(cls.__rec_doc))

    @classmethod
    def mod_rec(cls):
        k_ = uid() - 1
        if cls.__rec_doc[k_] != "Deleted":
            cls.__rec_doc.insert(k_, Doctor())
        else:
            messagebox.showerror("Error!", "Record Deleted Cannot be Modified")

    @classmethod
    def del_rec(cls):
        if messagebox.askyesno("Deletion", "Are you sure"):
            cls.__rec_doc.insert(uid() - 1, "Deleted")
            messagebox.showinfo("info", "Deleted")

    @classmethod
    def disp_rec(cls):
        t = uid() - 1
        x = cls.__rec_doc[t]
        if x is not str:
            ls = {"Name": cls.__rec_doc[t].name,
                  "Qualification": cls.__rec_doc[t].qualification,
                  "Age": cls.__rec_doc[t].age_,
                  "Gender": cls.__rec_doc[t].gender}
        else:
            ls = cls.__rec_doc[t]
        n_w = Tk()
        n_w.title("Record")
        n_w.geometry("500x250")
        sc_txt = scrolledtext.ScrolledText(n_w, width=50, height=20)
        sc_txt.grid(column=0, row=3)
        sc_txt.insert(INSERT, ls)
        n_w.mainloop()

    @classmethod
    def load_json(cls):
        rec = loads("doc_rec.json")
        for i in rec:
            cls.__rec_doc.append(Doctor(name=i["Name"], qualification=i["Qualification"],
                                        age=i["Age"], gender=i["Gender"]))

    @classmethod
    def write_json(cls):
        rec = list()
        for i in cls.__rec_doc:
            rec.append({"Name": i.name,
                        "Qualification": i.qualification,
                        "Age": i.age_,
                        "Gender": i.gender})
        dumps("doc_rec.json", rec)


if __name__ == '__main__':
    doc = Doctor()
