import openpyxl
import csv
from collections import defaultdict


def main():
    path = '../data/DRGT_AU_26_01_2023.xlsx'
    END_OF_FILE = 'Total Sans Region'

    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.worksheets[1]

    DOT = defaultdict(list)

    for cell in sheet_obj.iter_rows(min_row=1, min_col=1, max_col=2):
        dot, cmd = tuple(map(lambda item: item.value, cell))
        if dot == END_OF_FILE:
            break
        if cmd:
            DOT[dot].append(cmd)
    wb_obj.close()

    with open('DOTS.csv', 'w') as csvfile:
        fieldnames = ['DOT', 'USERS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dot in DOT:
            writer.writerow({'DOT': dot, 'USERS': DOT[dot]})


if __name__ == '__main__':
    main()
