#csv as list
import csv
with open('Auta.csv', mode='r') as in_file:                 # with-open - otwiera obiekt do obrobki plikow
    opened_file = csv.reader(in_file, delimiter = ',')
    line_count = 0
    n=0
    for row in opened_file:
        if line_count == 0:
            print(f'kolumny w pliku: {" ".join(row)}')       #f string - pozwala na formatowanie stringu
            line_count += 1
        else:
            print(*row)                                     #drukuje elementy listy obok siebie