#csv as list
import csv
with open('group_ARP.csv', mode='r') as in_file:                 # with-open - otwiera obiekt do obrobki plikow
    opened_file = csv.reader(in_file, delimiter = ',')
    line_count = 0
    n=0
    print(f'otwarcie pliku ')  # f string - pozwala na formatowanie stringu
    for row in opened_file:
        print('Grupe ' + str(row[0]) + ' nalezy zupdejtowac o '+ str(row[1:]))      # 1: pomija pierwszy element na liscie


