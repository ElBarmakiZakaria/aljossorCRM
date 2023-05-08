import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

file = pathlib.Path('student_table.xlsx')

if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "ID"
    sheet['B1'] = "Étudiante"
    sheet['C1'] = "Téléphone"

    file.save('student_table.xlsx')

