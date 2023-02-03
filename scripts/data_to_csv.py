import openpyxl
import csv
from random import randint

def run(file):
    path = f'static/{file}'
    END_OF_FILE = 'Total Sans Region'
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.worksheets[1]
    date = randint(0, 100)

    with open(f'static/data_{date}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for cell in sheet_obj.iter_rows(min_row=13, min_col=1, max_col=13):
            dot, *row = tuple(map(lambda item: item.value, cell))
            if dot == END_OF_FILE:
                break
            if row[0]:
                writer.writerow(row)
