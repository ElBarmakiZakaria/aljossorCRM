from tkinter import *
from tkinter import ttk
from database import studenttables
from database import functionality
import datetime

root = Tk()
root.title("Al-Jossor CRM")
root.geometry("910x635")
root.resizable(False, False)


icon_image = PhotoImage(file="icon.png")
root.iconphoto(False, icon_image)

style = ttk.Style()


class InfoPage:

    def __init__(self):
        # search frame
        search_frame = Frame(root)
        search_frame.grid(row=0, column=0, pady=20, padx=10)

        # Levels Dropdawn
        level_clicked = StringVar()
        level_clicked.set("Niveau")

        level_drop = OptionMenu(search_frame, level_clicked, 'Niveau', 'P_COLLEGE', 'D_COLLEGE', 'T_COLLEGE', 'TC',
                                'P_BAC',
                                'D_BAC')
        level_drop.configure(width=10)
        level_drop.grid(row=0, column=0, padx=15)

        # subjects Dropdawn
        sub_clicked = StringVar()
        sub_clicked.set("Matieres")

        sub_drop = OptionMenu(search_frame, sub_clicked, "Matieres", "MATH", "PC", "FRC", "ENG", "SVT")
        sub_drop.configure(width=10)
        sub_drop.grid(row=0, column=1, padx=15)

        # name entry
        name_label = Label(search_frame, text="NOM ET PRENOM:")
        name_label.grid(row=0, column=2)

        name_entry = Entry(search_frame, borderwidth=3)
        name_entry.grid(row=0, column=3, padx=15)

        # search buttom
        search_butt = Button(search_frame, text="Search", padx=10, background="#035397", foreground="#FCD900",
                             command=lambda: self.search_fun(level_clicked.get(), sub_clicked.get(), name_entry.get()))
        search_butt.grid(row=0, column=4, padx=5)

        # tree frame
        tree_frame = Frame(root)
        tree_frame.grid(row=1, column=0, padx=20)

        # Scroll bar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree_table = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")

        # pack
        self.tree_table.pack()

        # configure the scrollbar
        tree_scroll.configure(command=self.tree_table.yview)
        style.theme_use("clam")
        style.configure("Treeview",
                        foreground="black",
                        rowheight=30
                        )

        style.map('Treeview',
                  background=[('selected', '#035397')],
                  foreground=[('selected', '#FCD900')]
                  )

        # Define our Columns
        self.tree_table['columns'] = ("Student_ID", "Student_name", "phone_number", "level", "subjects", "studying")

        # Formate our columns
        self.tree_table.column("#0", width=40)
        self.tree_table.column("Student_ID", width=60, anchor=W, minwidth=30)
        self.tree_table.column("Student_name", width=150, anchor=W, minwidth=30)
        self.tree_table.column("phone_number", width=150, anchor=W, minwidth=30)
        self.tree_table.column("level", width=120, anchor=W, minwidth=30)
        self.tree_table.column("subjects", width=120, anchor=CENTER, minwidth=30)
        self.tree_table.column("studying", width=80, anchor=W, minwidth=30)

        # Create Heading
        self.tree_table.heading("#0", text="Num")
        self.tree_table.heading("Student_ID", text="ID", anchor=W)
        self.tree_table.heading("Student_name", text="Étudiante", anchor=W)
        self.tree_table.heading("phone_number", text="Téléphone", anchor=W)
        self.tree_table.heading("level", text="Niveau", anchor=W)
        self.tree_table.heading("subjects", text="Matières", anchor=CENTER)
        self.tree_table.heading("studying", text="Active", anchor=CENTER)

        # paneau frame
        boxes_frame = LabelFrame(root, text="panneau de commande", padx=20, pady=15)
        boxes_frame.grid(row=2, column=0, pady=7, padx=10)

        # Lebel
        student_id = Label(boxes_frame, text="ID")
        student_id.grid(row=0, column=0)

        student_name = Label(boxes_frame, text="Étudiante")
        student_name.grid(row=0, column=1)

        student_number = Label(boxes_frame, text="Téléphone")
        student_number.grid(row=0, column=2)

        student_level = Label(boxes_frame, text="Niveau")
        student_level.grid(row=0, column=3)

        student_subject = Label(boxes_frame, text="Matières")
        student_subject.grid(row=0, column=4)

        isstudying = Label(boxes_frame, text="Active")
        isstudying.grid(row=0, column=5)

        # entry
        student_ide = Entry(boxes_frame, borderwidth=3)
        student_ide.grid(row=1, column=0, padx=5)

        student_namee = Entry(boxes_frame, borderwidth=3)
        student_namee.grid(row=1, column=1, padx=5)

        student_numbere = Entry(boxes_frame, borderwidth=3)
        student_numbere.grid(row=1, column=2, padx=5)

        student_levele = Entry(boxes_frame, borderwidth=3)
        student_levele.grid(row=1, column=3, padx=5)

        student_subjecte = Entry(boxes_frame, borderwidth=3)
        student_subjecte.grid(row=1, column=4, padx=5)

        isstudyinge = Entry(boxes_frame, borderwidth=3)
        isstudyinge.grid(row=1, column=5, padx=5)

        # Add Record
        def add_record():
            current_date = datetime.date.today()

            student_information = [student_ide.get(), student_namee.get(), student_numbere.get(), student_levele.get(),
                                   student_subjecte.get(), isstudyinge.get()]

            student_level = student_levele.get()

            student_sub = student_subjecte.get().split(",")

            fun = functionality.Functionality()
            fun.add_record(student_information, student_level, student_sub, current_date)

            student_ide.delete(0, END)
            student_namee.delete(0, END)
            student_numbere.delete(0, END)
            student_subjecte.delete(0, END)
            isstudyinge.delete(0, END)
            student_levele.delete(0, END)

        # sace record
        def save_record():
            # grab record number
            # selected = self.tree_table.focus()

            table_subject = sub_clicked.get()

            student_current_id = student_ide.get()

            student_information = [student_ide.get(), student_namee.get(), student_numbere.get(), student_levele.get(),
                                   student_subjecte.get(), isstudyinge.get()]

            student_level = student_levele.get()

            student_sub = student_subjecte.get().split(",")

            fun = functionality.Functionality()
            fun.update_record(student_level, student_information, student_current_id, student_sub, table_subject)

            # # save nez data
            # self.tree_table.item(selected, text="", values=(
            #     student_namee.get(), student_numbere.get(), student_levele.get(),
            #     student_subjecte.get(),
            #     isstudyinge.get()))

            student_ide.delete(0, END)
            student_namee.delete(0, END)
            student_numbere.delete(0, END)
            student_subjecte.delete(0, END)
            isstudyinge.delete(0, END)
            student_levele.delete(0, END)

        # remove record
        def remove_record(level, subject):
            # level_clicked.get(), sub_clicked.get(), name_entry.get()
            # delete_record(self, table, subjet, record_id, student_sub)

            funremove = functionality.Functionality()
            student_sub = student_subjecte.get().split(",")

            funremove.delete_record(level, subject, student_ide.get(), student_sub, 0)

            student_ide.delete(0, END)
            student_namee.delete(0, END)
            student_numbere.delete(0, END)
            student_subjecte.delete(0, END)
            isstudyinge.delete(0, END)
            student_levele.delete(0, END)

        # update record
        def update_record(e):
            student_ide.delete(0, END)
            student_namee.delete(0, END)
            student_numbere.delete(0, END)
            student_subjecte.delete(0, END)
            isstudyinge.delete(0, END)
            student_levele.delete(0, END)

            # grab record number
            selected = self.tree_table.focus()
            # grab record values
            values = self.tree_table.item(selected, 'values')

            # output to entry boxes
            student_ide.insert(0, values[0])
            student_namee.insert(0, values[1])
            student_numbere.insert(0, values[2])
            student_subjecte.insert(0, values[4])
            isstudyinge.insert(0, values[5])
            student_levele.insert(0, values[3])

        # calling
        self.tree_table.bind("<ButtonRelease-1>", update_record)

        f_frame = Frame(boxes_frame)
        f_frame.grid(row=2, column=0, columnspan=6, pady=5)
        Add_Record_butt = Button(f_frame, text="ajouter", padx=20, background="#035397", foreground="#FCD900",
                                 command=add_record)
        Add_Record_butt.grid(row=0, column=0, pady=5, padx=5)

        delete_butt = Button(f_frame, text="Effacer", padx=20, background="#035397", foreground="#FCD900",
                             command=lambda: remove_record(level_clicked.get(), sub_clicked.get()))
        delete_butt.grid(row=0, column=3, pady=5, padx=5)
        save_butt = Button(f_frame, text="enregistrer", padx=20, background="#035397", foreground="#FCD900",
                           command=save_record)
        save_butt.grid(row=0, column=2, pady=5, padx=180)

        s_frame = Frame(root)
        s_frame.grid(row=3, column=0, pady=7, padx=10)
        create_table_butt = Button(s_frame, text="Create Table", padx=20, background="#C84B31", foreground="#BFFFF0",
                                   command=self.create_tables)
        create_table_butt.grid(row=0, column=0, pady=5, padx=5)
        extract_butt = Button(s_frame, text="Extract Data", padx=20, background="#3E7C17", foreground="#BFFFF0")
        extract_butt.grid(row=0, column=1, pady=5, padx=5)
        d_db_butt = Button(s_frame, text="D. DP", padx=20, background="#001E6C", foreground="#BFFFF0")
        d_db_butt.grid(row=0, column=2, pady=5, padx=5)
        u_db_butt = Button(s_frame, text="U. DP", padx=20, background="#001E6C", foreground="#BFFFF0")
        u_db_butt.grid(row=0, column=3, pady=5, padx=5)

        l_frame = Frame(root)
        l_frame.grid(row=4, column=0, padx=10, sticky=E)

        payment_butt = Button(l_frame, text="Payment Page", background="#035397", foreground="#FCD900",
                              command=self.payment_call)
        payment_butt.configure(
            width=20,
            height=1
        )
        payment_butt.pack()

    def payment_call(self):
        for widget in root.winfo_children():
            widget.destroy()

        PaymentPage()

    def create_tables(self):
        info_table = studenttables.StudentTable()
        info_table.table_based_on_levels()
        info_table.table_based_on_levelsandsubject()
        info_table = studenttables.PaymentTable()
        info_table.payment_table_by_levels()

    def search_fun(self, levels, subs, names):
        count = 0

        for rec in self.tree_table.get_children():
            self.tree_table.delete(rec)

        search = functionality.Functionality()
        student_list = search.search_record(levels, subs, names, 0, 'none', 'none')
        activ_student = []
        inactiv_student = []

        for rec in student_list:
            if rec[5] == 1:
                activ_student.append(rec)

            else:
                inactiv_student.append(rec)

        for record in activ_student:
            self.tree_table.insert(parent='', index='end', iid=str(count), text=f"{count + 1}",
                                   values=(record[0], record[1], record[2], record[3], record[4], record[5]))

            count += 1

        for record in inactiv_student:
            self.tree_table.insert(parent='', index='end', iid=str(count), text=f"{count + 1}",
                                   values=(record[0], record[1], record[2], record[3], record[4], record[5]))

            count += 1


class PaymentPage:
    count = 0

    def __init__(self):
        # # margingframe
        # marging_frame = Frame(root)
        # marging_frame.grid(row=0, column=0, padx=10)

        # searchframe
        search_frame = Frame(root)
        search_frame.grid(row=0, column=1, pady=20, padx=10)

        # level Dropdown
        level_clicked = StringVar()
        level_clicked.set("Niveau")

        level_drop = OptionMenu(search_frame, level_clicked, 'Niveau', 'P_COLLEGE', 'D_COLLEGE', 'T_COLLEGE', 'TC',
                                'P_BAC',
                                'D_BAC')
        level_drop.configure(width=10)
        level_drop.grid(row=0, column=0, padx=15)

        # months Dropdown
        month_clicked = StringVar()
        month_clicked.set("Mois")

        month_drop = OptionMenu(search_frame, month_clicked, 'Mois', "October", "November", "December",
                                "January", "February", "March", "April", "May", "June")
        month_drop.configure(width=10)
        month_drop.grid(row=0, column=1, padx=15)

        # name entry

        name_entry = Entry(search_frame, borderwidth=3, foreground='#888888')
        name_entry.grid(row=0, column=2, padx=15)
        name_entry.insert(0, 'nom ou prenom')

        def focuson(e):
            name_entry.configure(foreground='black')
            if name_entry.get() == 'nom ou prenom':
                name_entry.delete(0, 'end')

        def focusout(e):

            if name_entry.get() == '':
                name_entry.configure(foreground='#888888')
                name_entry.insert(0, 'nom ou prenom')

        name_entry.bind("<FocusIn>", focuson)
        name_entry.bind("<FocusOut>", focusout)

        # date selection
        day_entry = Entry(search_frame, borderwidth=3, foreground='#888888', width=5)
        day_entry.grid(row=0, column=3)
        day_entry.insert(0, 'jour')

        def focuson(e):
            day_entry.configure(foreground='black')
            if day_entry.get() == 'jour':
                day_entry.delete(0, 'end')

        def focusout(e):

            if day_entry.get() == '':
                day_entry.configure(foreground='#888888')
                day_entry.insert(0, 'jour')

        day_entry.bind("<FocusIn>", focuson)
        day_entry.bind("<FocusOut>", focusout)

        month_clickeds = StringVar()
        month_clickeds.set("Mois")

        month_drop = OptionMenu(search_frame, month_clickeds, 'Mois', "Oct.", "Nov.", "Dec.",
                                "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.")
        month_drop.configure(width=3)
        month_drop.grid(row=0, column=4)

        year_entry = Entry(search_frame, borderwidth=3, foreground='#888888', width=6)
        year_entry.grid(row=0, column=5)
        year_entry.insert(0, 'année')

        def focuson(e):
            year_entry.configure(foreground='black')
            if year_entry.get() == 'année':
                year_entry.delete(0, 'end')

        def focusout(e):

            if year_entry.get() == '':
                year_entry.configure(foreground='#888888')
                year_entry.insert(0, 'année')

        year_entry.bind("<FocusIn>", focuson)
        year_entry.bind("<FocusOut>", focusout)

        dates = year_entry.get() + '-' + month_clickeds.get() + '-' + day_entry.get()
        if dates == 'année-Mois-jour':
            dates = ''

        # search buttom
        Search_butt = Button(search_frame, text="Search", padx=10, background="#035397", foreground="#FCD900",
                             command=lambda: self.search_fun(level_clicked.get(), "none", name_entry.get(), dates,
                                                             month_clicked.get()))
        Search_butt.grid(row=0, column=6, padx=15)

        # tree frame
        tree_frame = Frame(root)
        tree_frame.grid(row=1, column=1, padx=20)

        # Scroll bar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree_table = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")

        # pack
        self.tree_table.pack()

        # configure the scrollbar
        tree_scroll.configure(command=self.tree_table.yview)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30
                        )

        style.map('Treeview',
                  background=[('selected', '#035397')],
                  foreground=[('selected', '#FCD900')]
                  )

        # Define our Columns
        self.tree_table['columns'] = (
            "Student_id", "Student_name", "level", "MATH", "PC", "SVT", "ENG", "FRC", "TMP", "Time")

        # Formate our columns
        self.tree_table.column("#0", width=40)
        self.tree_table.column("Student_id", width=80, anchor=W, minwidth=30)
        self.tree_table.column("Student_name", width=130, anchor=W, minwidth=30)
        self.tree_table.column("level", width=60, anchor=W, minwidth=30)
        self.tree_table.column("MATH", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("PC", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("SVT", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("ENG", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("FRC", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("TMP", width=70, anchor=CENTER, minwidth=30)
        self.tree_table.column("Time", width=130, anchor=W, minwidth=30)

        # Create Heading
        self.tree_table.heading("#0", text="Num")
        self.tree_table.heading("Student_id", text="ID", anchor=W)
        self.tree_table.heading("Student_name", text="Étudiante", anchor=W)
        self.tree_table.heading("level", text="Niveau", anchor=W)
        self.tree_table.heading("MATH", text="MATH", anchor=CENTER)
        self.tree_table.heading("PC", text="PC", anchor=CENTER)
        self.tree_table.heading("SVT", text="SVT", anchor=CENTER)
        self.tree_table.heading("ENG", text="ENG", anchor=CENTER)
        self.tree_table.heading("FRC", text="FRC", anchor=CENTER)
        self.tree_table.heading("TMP", text="Total", anchor=CENTER)
        self.tree_table.heading("Time", text="Date", anchor=W)

        # main label
        frame = Frame(root)
        frame.grid(row=2, column=1, pady=7, padx=10)

        # total frame
        totalframe = Frame(frame)
        totalframe.grid(row=0, column=0, columnspan=2)
        self.mathTotal = Label(totalframe, text="MATH TOTAL: ")
        self.mathTotal.grid(row=0, column=0, padx=9)

        self.pcTotal = Label(totalframe, text="PC TOTAL: ")
        self.pcTotal.grid(row=0, column=1, padx=9)

        self.svtTotal = Label(totalframe, text="SVT TOTAL: ")
        self.svtTotal.grid(row=0, column=3, padx=9)

        self.engTotal = Label(totalframe, text="ENG TOTAL: ")
        self.engTotal.grid(row=0, column=4, padx=9)

        self.frcTotal = Label(totalframe, text="FRC TOTAL: ")
        self.frcTotal.grid(row=0, column=5, padx=9)

        self.totalamounth = Label(totalframe, text="TOTAL: ")
        self.totalamounth.grid(row=0, column=6, padx=9)

        # paneau frame
        boxes_frame = LabelFrame(frame, text="panneau de commande", padx=20, pady=10)
        boxes_frame.grid(row=1, column=0, pady=2, padx=10)

        # label
        student_id = Label(boxes_frame, text="ID")
        student_id.grid(row=0, column=0)

        student_name = Label(boxes_frame, text="Étudiante")
        student_name.grid(row=0, column=2)

        level = Label(boxes_frame, text="Niveau")
        level.grid(row=0, column=4)

        # entry
        student_ide = Entry(boxes_frame, borderwidth=3)
        student_ide.grid(row=0, column=1, padx=2)

        student_namee = Entry(boxes_frame, borderwidth=3)
        student_namee.grid(row=0, column=3, padx=2)

        levelinput = Entry(boxes_frame, borderwidth=3)
        levelinput.grid(row=0, column=5, padx=2)

        # month frame
        month_frame = Frame(boxes_frame)
        month_frame.grid(row=1, column=0, columnspan=6)

        # moths checkboxes
        math = Label(month_frame, text="MATH")
        math.grid(row=0, column=0)

        pc = Label(month_frame, text="PC")
        pc.grid(row=0, column=1)

        svt = Label(month_frame, text="SVT")
        svt.grid(row=0, column=2)

        eng = Label(month_frame, text="ENG")
        eng.grid(row=0, column=3)

        frc = Label(month_frame, text="FRC")
        frc.grid(row=0, column=4)

        mathe = Entry(month_frame, borderwidth=3)
        mathe.grid(row=1, column=0)

        pce = Entry(month_frame, borderwidth=3)
        pce.grid(row=1, column=1, padx=7)

        svte = Entry(month_frame, borderwidth=3)
        svte.grid(row=1, column=2)

        enge = Entry(month_frame, borderwidth=3)
        enge.grid(row=1, column=3, padx=7)

        frce = Entry(month_frame, borderwidth=3)
        frce.grid(row=1, column=4)

        # update record
        def update_record(e):
            student_ide.delete(0, END)
            student_namee.delete(0, END)
            levelinput.delete(0, END)
            mathe.delete(0, END)
            pce.delete(0, END)
            svte.delete(0, END)
            enge.delete(0, END)
            frce.delete(0, END)

            # grab record number
            selected = self.tree_table.focus()
            # grab record values
            values = self.tree_table.item(selected, 'values')

            # output to entry boxes
            student_ide.insert(0, values[0])
            student_namee.insert(0, values[1])
            levelinput.insert(0, values[2])
            mathe.insert(0, values[3])
            pce.insert(0, values[4])
            svte.insert(0, values[5])
            enge.insert(0, values[6])
            frce.insert(0, values[7])

        # calling
        self.tree_table.bind("<ButtonRelease-1>", update_record)

        # sace record
        def save_record():
            # grab record number
            # selected = self.tree_table.focus()

            # GET DATE FROM COMPUTER
            current_date = datetime.date.today()
            mon = month_clicked.get()
            date = str(current_date) + "/" + mon

            student_information = [student_ide.get(), student_namee.get(), mathe.get(), pce.get(),
                                   svte.get(), enge.get(), frce.get()]

            total = 0
            for sub in [mathe.get(), pce.get(), svte.get(), enge.get(), frce.get()]:
                total = total + int(sub)

            fun = functionality.Functionality()
            fun.update_record_forpayment(levelinput.get(), mon, student_information, date, total)

            student_ide.delete(0, END)
            student_namee.delete(0, END)
            levelinput.delete(0, END)
            mathe.delete(0, END)
            pce.delete(0, END)
            svte.delete(0, END)
            enge.delete(0, END)
            frce.delete(0, END)

        # remove record
        # def remove_record():
        #     # level_clicked.get(), sub_clicked.get(), name_entry.get()
        #     # delete_record(self, table, subjet, record_id, student_sub)
        #
        #     student_level = level_clicked.get()
        #     funremove = functionality.Functionality()
        #     funremove.delete_record(student_level, "none", student_ide.get(), "none", 1)
        #
        #     student_ide.delete(0, END)
        #     student_namee.delete(0, END)
        #     sep_check.deselect()
        #     oct_check.deselect()
        #     nov_check.deselect()
        #     dec_check.deselect()
        #     jan_check.deselect()
        #     feb_check.deselect()
        #     mar_check.deselect()
        #     apr_check.deselect()
        #     may_check.deselect()
        #     jun_check.deselect()

        f_frame = Frame(frame)
        f_frame.grid(row=1, column=1, pady=5, padx=5)

        # delete_butt = Button(f_frame, text="Effacer", padx=20, background="#035397", foreground="#FCD900")
        # delete_butt.configure(width=10)
        # delete_butt.grid(row=1, column=0, pady=5)

        save_butt = Button(f_frame, text="enregistrer", padx=20, background="#035397", foreground="#FCD900",
                           command=save_record)
        save_butt.configure(width=10)
        save_butt.grid(row=0, column=0, pady=5)

        s_frame = Frame(root)
        s_frame.grid(row=3, column=1, pady=7, padx=10)
        # create_table_butt = Button(s_frame, text="Create Table", padx=20, background="#C84B31",
        #                            foreground="#BFFFF0", command=self.create_tables)
        # create_table_butt.grid(row=0, column=0, pady=5, padx=5)
        d_db_butt = Button(s_frame, text="D. DP", padx=20, background="#001E6C", foreground="#BFFFF0")
        d_db_butt.grid(row=0, column=1, pady=5, padx=5)
        u_db_butt = Button(s_frame, text="U. DP", padx=20, background="#001E6C", foreground="#BFFFF0")
        u_db_butt.grid(row=0, column=2, pady=5, padx=5)

        l_frame = Frame(root)
        l_frame.grid(row=4, column=1, padx=50, sticky=E)

        payment_butt = Button(l_frame, text="Info Page", background="#035397", foreground="#FCD900",
                              command=self.info_call)
        payment_butt.configure(
            width=20,
            height=1
        )
        payment_butt.pack()

    def search_fun(self, levels, subs, names, date, month):
        count = 0

        for rec in self.tree_table.get_children():
            self.tree_table.delete(rec)

        search = functionality.Functionality()
        student_list = search.search_record(levels, subs, names, 1, date, month)

        mathtotal = 0
        pctotal = 0
        svttotal = 0
        engtotal = 0
        frctotal = 0
        total = 0

        for record in student_list:
            mathtotal = mathtotal + int(record[3])
            pctotal = pctotal + int(record[4])
            svttotal = svttotal + int(record[5])
            engtotal = engtotal + int(record[6])
            frctotal = frctotal + int(record[7])
            total = total + int(record[8])

            self.tree_table.insert(parent='', index='end', iid=str(count), text="",
                                   values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                           record[6], record[7], record[8], record[9]))

            count += 1

        self.mathTotal.configure(text=f"MATH TOTAL : {mathtotal}")
        self.pcTotal.configure(text=f"PC TOTAL : {pctotal}")
        self.svtTotal.configure(text=f"SVT TOTAL : {svttotal}")
        self.engTotal.configure(text=f"ENG TOTAL : {engtotal}")
        self.frcTotal.configure(text=f"FRC TOTAL : {frctotal}")
        self.totalamounth.configure(text=f"TOTAL : {total}")

    def info_call(self):
        for widget in root.winfo_children():
            widget.destroy()

        InfoPage()

    # def create_tables(self):
    #     info_table = studenttables.PaymentTable()
    #     info_table.payment_table_by_levels()


if __name__ == '__main__':
    InfoPage()

    root.mainloop()
