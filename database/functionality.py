import sqlite3

connection = sqlite3.connect('database.db')
connection.commit()
connection.close()


class Functionality:
    def __init__(self):
        self.months = ['October', 'November', 'December',
                       'January', 'February', 'March', 'April', 'May', 'June']

    # add record function need 3 argument the fitst id the record witch is the student and the basec information,
    # the second one level witch is the level that this student is currently in
    # the last one are subject that this student are studying in the centre

    def add_record(self, record, level, sub, date):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()
        c.execute(f"INSERT INTO {level} VALUES (?,?,?,?,?,?)", record)
        for subject in sub:
            c.execute(f"INSERT INTO {level + '_' + subject} VALUES (?,?,?,?,?,?)", record)

        c.execute(f"INSERT INTO Payment_Table VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (record[0], record[1], record[3], 0, 0, 0, 0, 0, 0, date))

        for month in self.months:
            c.execute(f"INSERT INTO Payment_Table_{month} VALUES (?,?,?,?,?,?,?,?,?,?)",
                      (record[0], record[1], record[3], 0, 0, 0, 0, 0, 0, '0'))

        for month in self.months:
            c.execute(f"INSERT INTO Payment_Table_{level + '_' + month} VALUES (?,?,?,?,?,?,?,?,?,?)",
                      (record[0], record[1], record[3], 0, 0, 0, 0, 0, 0, '0'))

        connection.commit()
        connection.close()


    def delete_record(self, table, subjet, record_id, student_sub, ispayment):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        if ispayment == 0:
            if subjet != "Matieres":
                c.execute(f"DELETE FROM {table + '_' + subjet} WHERE student_id = :id",
                          {'id': record_id}
                          )

            else:
                c.execute(f"DELETE FROM {table} WHERE student_id = :id",
                          {'id': record_id}
                          )
                for subb in student_sub:
                    c.execute(f"DELETE FROM {table + '_' + subb} WHERE student_id = :id",
                              {'id': record_id}
                              )

        # else:
        #     c.execute(f"DELETE FROM Payment_{table} WHERE student_id = :id",
        #               {'id': record_id}
        #               )

        connection.commit()
        connection.close()

    # def Search_and_delete_delete_records(self, level, sub, all_sub, f_n, l_n):
    #     global connection
    #     connection = sqlite3.connect('database.db')
    #     c = connection.cursor()
    #
    #     for subjects in all_sub:
    #         row_id = c.execute(
    #             f"SELECT rowid FROM {level + '_' + subjects} WHERE first_name LIKE '%{f_n}%' AND last_name LIKE '%{l_n}%' ")
    #
    #         if row_id is not None:
    #             for subject in sub:
    #                 if level + '_' + subjects != level + '_' + subject:
    #                     self.delete_record(level + '_' + subjects, row_id)

    def update_record(self, level, new_record, row_id, sub, tablesub):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        if tablesub == 'Matieres':
            c.execute(f"""UPDATE {level}  SET
                student_name = :name,
                phone_number = :number,
                level = :level,
                subjects = :subject,
                studying = :isstudying
                
                WHERE student_id = :id """,
                      {
                          'name': new_record[1],
                          'number': new_record[2],
                          'level': new_record[3],
                          'subject': new_record[4],
                          'isstudying': new_record[5],
                          'id': row_id
                      })

            for subjects in sub:
                c.execute(f"""UPDATE {level + "_" + subjects} SET 
                    student_name = :name,
                    phone_number = :number,
                    level = :level,
                    subjects = :subject,
                    studying = :isstudying
                
                    WHERE student_id = :id """,
                          {
                              'name': new_record[1],
                              'number': new_record[2],
                              'level': new_record[3],
                              'subject': new_record[4],
                              'isstudying': new_record[5],
                              'id': row_id
                          })

        elif tablesub != 'Matieres':
            c.execute(f"""UPDATE {level + "_" + tablesub} SET 
                                student_name = :name,
                                phone_number = :number,
                                level = :level,
                                subjects = :subject,
                                studying = :isstudying

                                WHERE student_id = :id """,
                      {
                          'name': new_record[1],
                          'number': new_record[2],
                          'level': new_record[3],
                          'subject': new_record[4],
                          'isstudying': new_record[5],
                          'id': row_id
                      })

        # self.Search_and_delete_delete_records(level, sub, self.allsubjects, new_record[0], new_record[1])
        connection.commit()
        connection.close()

    def update_record_forpayment(self, level, month, new_record, date, tt):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        c.execute(f"INSERT INTO Payment_Table VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (new_record[0], new_record[1], level, new_record[2], new_record[3], new_record[4], new_record[5],
                   new_record[6], tt, date))

        # if month == "Mois":
        #     c.execute(f"""UPDATE Payment_Table  SET
        #                     student_name = :name,
        #                     level = :level,
        #                     Math = :Math,
        #                     Pc = :Pc,
        #                     Svt = :Svt,
        #                     Eng = :Eng,
        #                     Frc = :Frc,
        #                     Total = :Total,
        #                     Date = :Date
        #
        #                     WHERE student_id = :id """,
        #               {
        #                   'name': new_record[1],
        #                   'level': level,
        #                   'Math': new_record[2],
        #                   'Pc': new_record[3],
        #                   'Svt': new_record[4],
        #                   'Eng': new_record[5],
        #                   'Frc': new_record[6],
        #                   'Total': tt,
        #                   'Date': date,
        #                   'id': new_record[0]
        #               })

        if month != "Mois":
            c.execute(f"""UPDATE Payment_Table_{month}  SET
                student_name = :name,
                level = :level,
                Math = :Math,
                Pc = :Pc,
                Svt = :Svt,
                Eng = :Eng,
                Frc = :Frc,
                Total = :Total,
                Date = :Date
    
                WHERE student_id = :id """,
                      {
                          'name': new_record[1],
                          'level': level,
                          'Math': new_record[2],
                          'Pc': new_record[3],
                          'Svt': new_record[4],
                          'Eng': new_record[5],
                          'Frc': new_record[6],
                          'Total': tt,
                          'Date': date,
                          'id': new_record[0]
                      })

        if level != "Niveau":
            c.execute(f"""UPDATE Payment_Table_{level + '_' + month}  SET
                        student_name = :name,
                        level = :level,
                        Math = :Math,
                        Pc = :Pc,
                        Svt = :Svt,
                        Eng = :Eng,
                        Frc = :Frc,
                        Total = :Total,
                        Date = :Date
    
                        WHERE student_id = :id """,
                      {
                          'name': new_record[1],
                          'level': level,
                          'Math': new_record[2],
                          'Pc': new_record[3],
                          'Svt': new_record[4],
                          'Eng': new_record[5],
                          'Frc': new_record[6],
                          'Total': tt,
                          'Date': date,
                          'id': new_record[0]
                      })

        # self.Search_and_delete_delete_records(level, sub, self.allsubjects, new_record[0], new_record[1])
        connection.commit()
        connection.close()

    # the search method is a method that also take 4 argument the first one and second is the level and sub to know in witch table it have to look to
    # the other two to seatch and return the record that you want
    # the last argument is_payment is for to know if we show the payment table or the list table

    def search_record(self, level, sub, name, ispayment, date, mon):
        global connection
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        if ispayment == 0:
            if sub == "Matieres":
                if name != "":
                    c.execute(f"SELECT * FROM {level} WHERE student_name LIKE '%{name}%' ")

                    return c.fetchall()
                elif name == "":
                    c.execute(f"SELECT * FROM {level} ")

                    return c.fetchall()


            elif level != "Niveau" and sub != "Matieres":
                if name != "":
                    c.execute(f"SELECT * FROM {level + '_' + sub} WHERE student_name LIKE '%{name}%' ")

                    return c.fetchall()
                elif name == "":
                    c.execute(f"SELECT * FROM {level + '_' + sub}")

                    return c.fetchall()

            else:

                return "NOTHING TO BE FOUND"

        else:

            if mon == 'Mois' and name != "" and date == '':
                c.execute(f"SELECT * FROM Payment_Table WHERE student_name LIKE '%{name}%' ")

                return c.fetchall()

            elif mon == 'Mois' and name == "" and date != '':
                c.execute(f"SELECT * FROM Payment_Table WHERE Date LIKE '%{date}%' ")

                return c.fetchall()

            elif mon != "Mois" and name != "nom ou prenom":
                c.execute(f"SELECT * FROM Payment_Table_{mon} WHERE student_name LIKE '%{name}%' ")

                return c.fetchall()

            elif mon != "Mois" and level == "Niveau":
                c.execute(f"SELECT * FROM Payment_Table_{mon} ")

                return c.fetchall()

            elif mon != "Mois" and level != "Niveau":

                c.execute(f"SELECT * FROM Payment_Table_{level + '_' + mon} ")

                return c.fetchall()

        connection.commit()
        connection.close()
