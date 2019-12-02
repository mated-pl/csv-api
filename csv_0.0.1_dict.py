#csv as dict
import csv
with open('Auta_dict.csv', mode='r') as in_file:                 # with-open - otwiera obiekt do obrobki plikow
    opened_file = csv.DictReader(in_file)
    line_count = 0
    n=0
    for row in opened_file:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')     #f string - pozwala na formatowanie stringu
            line_count += 1
        else:
            print('')                                     #drukuje elementy listy obok siebie