import random
import xlsxwriter
from datetime import datetime

print("Podaj ilość graczy: ", end="")
lgraczy=int(input())

for i in range (lgraczy):

    data=datetime.today().strftime('%d.%m.%Y')
    pytania_tab=[]
    plik_tekstowy=open("pytania.txt", "r")

    for i in plik_tekstowy:
        pytania_tab.append(i)
    plik_tekstowy.close()

if len(pytania_tab) != 25:
    print("\nBłąd: Plik z pytaniami musi zawierać 25 pozycji!")
    input()
    exit()

    print("Imię zawodnika: ", end="")
    nazwa_tabeli=input()

    plik_excel=xlsxwriter.Workbook(nazwa_tabeli+" "+data+".xlsx")
    strona_excel = plik_excel.add_worksheet()
    formatowanie = plik_excel.add_format({'align': 'center', 'valign':'vcenter', 'fg_color':'FF0115', 'border':6})
    strona_excel.set_column(0, 4, 30)

    kolumna=0
    for i in range (5):
        rzad=0
        for k in range(5):
            wybor=random.randrange(0, len(pytania_tab))
            strona_excel.write(rzad, kolumna, pytania_tab[wybor], formatowanie)
            del pytania_tab[wybor]
            strona_excel.set_row(rzad, 40)
            rzad+=1
        kolumna+=1

    plik_excel.close()

    print("\nBINGO!")
    print("Plik stworzony!")
input()
