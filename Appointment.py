from Doctor import Doctor
from Patient import Patient
from Record import *


# TODO(Modify Appointment when doctor or Patient is deleted or modified)
# TODO(Manage dates using datetime library)
class Appointment(Record):
    __rec = list()

    def __init__(self, patient=None, doctor=None, date=None):
        if isinstance(patient, Patient) and isinstance(doctor, Doctor) and isinstance(date, str):
            self.patient = patient
            self.doctor = doctor
            self.date_ = date
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

    def str_value(self):
        return {"Patient ": self.patient.str_value(),
                "Doctor": self.doctor.str_value(),
                "Date": self.date_
                }

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
            cls.__rec.append(a)
            messagebox.showinfo("Unique id", len(cls.__rec))

    @classmethod
    def mod_rec(cls):
        k_ = uid() - 1
        x = cls.get_rec(k_)
        if x is not None:
            cls.__rec.insert(k_, Appointment())

    @classmethod
    def del_rec(cls):
        k_ = uid() - 1
        if k_ < len(cls.__rec):
            if messagebox.askyesno("Deletion", "Are you sure"):
                cls.__rec.insert(uid() - 1, "Deleted")
                messagebox.showinfo("info", "Deleted")
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
                messagebox.showerror("No Appointment with such ID",
                                     " The record of Appointment was deleted")
        else:
            messagebox.showerror("No Appointment with such ID",
                                 "The record of Appointment doesn't exist")

    @classmethod
    def load_json(cls):
        rec = loads("app_rec.json")
        for i in rec:
            cls.__rec.append(Appointment(patient=Patient(name=i["Patient"]["Name"], illness=i["Patient"]["Illness"],
                                                         age=i["Patient"]["Age"], gender=i["Patient"]["Gender"]),
                                         doctor=Doctor(name=i["Doctor"]["Name"], gender=i["Doctor"]["Gender"],
                                                       qualification=i["Doctor"]["Qualification"],
                                                       age=i["Doctor"]["Age"]),
                                         date=i["Date"]))

    @classmethod
    def write_json(cls):
        rec = list()
        for i in cls.__rec:
            rec.append(i.str_value())


if __name__ == '__main__':
    app = Appointment()
    app.disp_rec()
