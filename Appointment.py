from tkinter import *
from tkinter import scrolledtext, messagebox

from EnterUID_GUI import *
from JsonMng import loads, dumps

from Doctor import Doctor
from Patient import Patient


class Appointment:
    __rec_app = list()

    def __init__(self, patient=None, doctor=None, date=None):
        if patient and doctor and date is not None:
            self.patient = self.patient
            self.doctor = self.doctor
            self.date_ = self.date
        else:
            self.app_w = Tk()
            self.app_w.title("Appointment")
            self.app_w.geometry('960x540')
            self.pat_lbl = Label(self.app_w, text="UID of Patient:")
            self.pat_lbl.grid(column=0, row=0, padx=(10, 0))
            self.pat_id = Entry(self.app_w, width=50)
            self.pat_id.grid(column=1, row=0, padx=20, pady=10)

            self.doc_lbl = Label(self.app_w, text="UID of Doctor:")
            self.doc_lbl.grid(column=0, row=1, padx=(10, 0))
            self.doc_id = Entry(self.app_w, width=50)
            self.doc_id.grid(column=1, row=1, padx=20, pady=10)

            self.date_lbl = Label(self.app_w, text="Date:")
            self.date_lbl.grid(column=0, row=2, padx=(10, 0))
            self.date = Entry(self.app_w, width=50)
            self.date.grid(column=1, row=2, padx=20, pady=10)

            self.save = Button(self.app_w, text="Save", command=self.save)
            self.save.grid(column=0, row=5, padx=(40, 0), pady=10)

            self.exit = Button(self.app_w, text="Done", command=self.destroy)
            self.exit.grid(column=1, row=5, padx=(40, 0), pady=10)

            self.app_w.mainloop()

    # def __str__(self):
    #     return {"Patient": self.patient,
    #             "Doctor": self.doctor,
    #             "Date": self.date,
    #             }

    def destroy(self):
        self.app_w.quit()
        self.app_w.destroy()

    def save(self):
        self.patient = Patient.get_rec(int(self.pat_id.get()) - 1)
        self.doctor = Doctor.get_rec(int(self.doc_id.get()) - 1)
        self.date_ = self.date.get()
        if self.patient is None or self.doctor is None:
            self.destroy()

    @classmethod
    def add_rec(cls):
        a = Appointment()
        if a.doctor is None or a.patient is None:
            messagebox.showinfo("Appointment not created", "invalid entries")
        else:
            cls.__rec_app.append(a)
            messagebox.showinfo("Unique id", len(cls.__rec_app))

    @classmethod
    def mod_rec(cls):
        k_ = uid() - 1
        if cls.__rec_app[k_] != "Deleted":
            cls.__rec_app.insert(k_, Appointment())
        else:
            messagebox.showerror("Error!", "Record Deleted Cannot be Modified")

    @classmethod
    def del_rec(cls):
        if messagebox.askyesno("Deletion", "Are you sure"):
            cls.__rec_app.insert(uid() - 1, "Deleted")
            messagebox.showinfo("info", "Deleted")

    @classmethod
    def disp_rec(cls):
        t = uid() - 1
        if t < len(cls.__rec_app):
            if not isinstance(cls.__rec_app[t], str):
                ls = {"Patient ": cls.__rec_app[t].patient.str_value(),
                      "Doctor": cls.__rec_app[t].doctor.str_value(),
                      "Date": cls.__rec_app[t].date_,
                      }
            else:
                ls = cls.__rec_app[t]

            n_w = Tk()
            n_w.title("Record")
            n_w.geometry("500x250")
            sc_txt = scrolledtext.ScrolledText(n_w, width=50, height=20)
            sc_txt.grid(column=0, row=3)
            sc_txt.insert(INSERT, ls)
            n_w.mainloop()
        else:
            messagebox.showerror('No data found', 'There is no such entry in data base')

    @classmethod
    def load_json(cls):
        rec = loads("pat_rec.json")
        for i in rec:
            cls.__rec_app.append(Appointment(patient=i["Patient"], doctor=i["Doctor"], date=i["Date"]))

    @classmethod
    def write_json(cls):
        rec = list()
        for i in cls.__rec_app:
            rec.append({"Patient": i.patient,
                        "Doctor": i.doctor,
                        "Date": i.date})
        dumps("pat_rec.json", rec)


if __name__ == '__main__':
    app = Appointment()
    app.disp_rec()
