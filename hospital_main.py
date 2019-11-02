from tkinter.ttk import *

from Appointment import *
from Doctor import *
from Patient import *

# TODO(Implement Database)
# TODO(improve UID implementation)
mainWindow = Tk()
mainWindow.title("Hospital Management System")
mainWindow.geometry('960x540')
Doctor.load_json()
Patient.load_json()
Appointment.load_json()
menu = Menu(mainWindow)
menu.add_command(label='Save to database', command=lambda: [Doctor.write_json(), Appointment.write_json(),
                                                            Patient.write_json()])
mainWindow.config(menu=menu)


def doctor():
    doc_mng = Tk()
    doc_mng.title("Doctor Management")
    doc_mng.geometry('960x540')

    def destroy_():
        doc_mng.quit()
        doc_mng.destroy()

    add_doc = Button(doc_mng, text="New Doctor Record", command=lambda: [destroy_(), Doctor.add_rec()])
    add_doc.grid(column=1, row=0, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    disp_doc = Button(doc_mng, text="Display Doctor Record", command=lambda: [destroy_(), Doctor.disp_rec()])
    disp_doc.grid(column=1, row=1, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    mod_doc = Button(doc_mng, text="Modify Doctor Record", command=lambda: [destroy_(), Doctor.mod_rec()])
    mod_doc.grid(column=1, row=2, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    del_doc = Button(doc_mng, text="Delete Doctor Record", command=lambda: [destroy_(), Doctor.del_rec()])
    del_doc.grid(column=1, row=3, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    ret = Button(doc_mng, text="Return", command=destroy_)
    ret.grid(column=2, row=4, padx=(400, 0), pady=20, ipady=20, ipadx=20)

    doc_mng.mainloop()


bt_doc = Button(mainWindow, text="Doctor", command=doctor)
bt_doc.grid(column=1, row=0, padx=400, pady=20, ipadx=20, ipady=20)


def patient():
    pat_mng = Tk()
    pat_mng.title("Patient Management")
    pat_mng.geometry('960x540')

    def destroy_():
        pat_mng.quit()
        pat_mng.destroy()

    add_pat = Button(pat_mng, text="New Patient Record", command=lambda: [destroy_(), Patient.add_rec()])
    add_pat.grid(column=1, row=0, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    disp_pat = Button(pat_mng, text="Display Patient Record", command=lambda: [destroy_(), Patient.disp_rec()])
    disp_pat.grid(column=1, row=1, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    mod_pat = Button(pat_mng, text="Modify Patient Record", command=lambda: [destroy_(), Patient.mod_rec()])
    mod_pat.grid(column=1, row=2, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    del_pat = Button(pat_mng, text="Delete Patient Record", command=lambda: [destroy_(), Patient.del_rec()])
    del_pat.grid(column=1, row=3, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    ret = Button(pat_mng, text="Return", command=destroy_)
    ret.grid(column=2, row=4, padx=(400, 0), pady=20, ipady=20, ipadx=20)

    pat_mng.mainloop()


bt_pat = Button(mainWindow, text="Patient", command=patient)
bt_pat.grid(column=1, row=1, padx=400, pady=20, ipadx=20, ipady=20)


def appointment():
    app_mng = Tk()
    app_mng.title("Appointment Management")
    app_mng.geometry('960x540')
    add_app = Button(app_mng, text="New Appointment Record", command=lambda: [destroy_(), Appointment.add_rec()])
    add_app.grid(column=1, row=0, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    disp_app = Button(app_mng, text="Display Appointment Record", command=lambda: [destroy_(), Appointment.disp_rec()])
    disp_app.grid(column=1, row=1, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    mod_app = Button(app_mng, text="Modify Appointment Record", command=lambda: [destroy_(), Appointment.mod_rec()])
    mod_app.grid(column=1, row=2, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    del_app = Button(app_mng, text="Delete Appointment Record", command=lambda: [destroy_(), Appointment.del_rec()])
    del_app.grid(column=1, row=3, padx=(200, 0), pady=20, ipadx=20, ipady=20)

    def destroy_():
        app_mng.quit()
        app_mng.destroy()

    ret = Button(app_mng, text="Return", command=destroy_)
    ret.grid(column=2, row=4, padx=(400, 0), pady=20, ipady=20, ipadx=20)

    app_mng.mainloop()


bt_app = Button(mainWindow, text="Appointment", command=appointment)
bt_app.grid(column=1, row=2, padx=400, pady=20, ipadx=20, ipady=20)


def destroy():
    mainWindow.quit()
    mainWindow.destroy()


bt_exit = Button(mainWindow, text="Exit", command=destroy)
bt_exit.grid(column=1, row=3, padx=400, pady=20, ipadx=20, ipady=20)

mainWindow.mainloop()
