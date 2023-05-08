import sqlite3

connection = sqlite3.connect('database.db')
connection.commit()
connection.close()


class StudentTable:
    def __init__(self):
        self.levels = ['P_COLLEGE', 'D_COLLEGE', 'T_COLLEGE', 'TC', 'P_BAC', 'D_BAC']
        self.subjects = ["MATH", "PC", "FRC", "ENG", "SVT"]

    #
    # def connect_to_db(self):
    #     global connection
    #     connection = sqlite3.connect('database.db')

    def table_based_on_levels(self):

        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        for level in self.levels:
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                    student_id text,
                    student_name text,
                    phone_number text,
                    level text,
                    subjects text,
                    studying integer
               )""".format(level))

        connection.commit()
        connection.close()

    def table_based_on_levelsandsubject(self):

        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        for level in self.levels:
            for subject in self.subjects:
                c.execute(f"""CREATE TABLE IF NOT EXISTS {level + "_" + subject} (
                    student_id text,
                    student_name text,
                    phone_number text,
                    level text,
                    subjects text,
                    studying integer
                   )""")

        connection.commit()
        connection.close()


class PaymentTable:
    def __init__(self):
        self.levels = ['P_COLLEGE', 'D_COLLEGE', 'T_COLLEGE', 'TC', 'P_BAC',
                       'D_BAC']
        self.months = ['October', 'November', 'December',
                    'January', 'February', 'March', 'April', 'May', 'June']

    def payment_table_by_levels(self):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()


        c.execute(f"""CREATE TABLE IF NOT EXISTS Payment_Table (
                student_id text,
                student_name text,
                level text,
                Math integer,
                Pc integer,
                Svt integer,
                Eng integer,
                Frc integer,
                Total integer,
                Date text
           )""")


        for month in self.months:
            c.execute(f"""CREATE TABLE IF NOT EXISTS Payment_Table_{month} (
                    student_id text,
                    student_name text,
                    level text,
                    Math integer,
                    Pc integer,
                    Svt integer,
                    Eng integer,
                    Frc integer,
                    Total integer,
                    Date text
               )""")

        for level in self.levels:
            for month in self.months:
                c.execute(f"""CREATE TABLE IF NOT EXISTS Payment_Table_{level +'_'+ month} (
                                    student_id text,
                                    student_name text,
                                    level text,
                                    Math integer,
                                    Pc integer,
                                    Svt integer,
                                    Eng integer,
                                    Frc integer,
                                    Total integer,
                                    Date text
                               )""")


        connection.commit()
        connection.close()
