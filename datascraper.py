
import csv
import openpyxl
from openpyxl import load_workbook

# Eğer programın burasında bir bug ile karşılaşırsanız programın + datanın aynı repoda olup olmadığını kontrol edin
workbook = load_workbook(filename="prime_Data.xlsx")
sheet = workbook.active

i = 2


def Excel_import(entered_list, column, i=i):
    for value in range(53):
        entered_list.append(sheet[column + str(i)].value)
        i += 1
    return entered_list


morbidite_list = []
Excel_import(morbidite_list, "X")

e = 0
for val in morbidite_list:
    if val == None:
        morbidite_list.pop(e)
        morbidite_list.insert(e, 0)
    else:
        morbidite_list.pop(e)
        morbidite_list.insert(e, 1)

    e += 1

ameliyat_list = []
Excel_import(ameliyat_list, "A")

asa_skoru_list = []
Excel_import(asa_skoru_list, "B")

age_list = []
Excel_import(age_list, "C")

gender_list = []
Excel_import(gender_list, "D")

boy_list = []
Excel_import(boy_list, "E")

bmi_list = []
Excel_import(bmi_list, "F")

ybu_list = []
Excel_import(ybu_list, "H")

wbc_list = []
Excel_import(wbc_list, "J")

crp_list = []
Excel_import(crp_list, "K")

inr_list = []
Excel_import(inr_list, "L")

hb_list = []
Excel_import(hb_list, "M")

plt_list = []
Excel_import(plt_list, "N")

alb_list = []
Excel_import(alb_list, "O")

ht_list = []
Excel_import(ht_list, "P")

dm_list = []
Excel_import(dm_list, "Q")

kah_list = []
Excel_import(kah_list, "R")

koah_list = []
Excel_import(koah_list, "S")

patoloji_list = []
Excel_import(patoloji_list, "U")

L3_yuzey_list = []
Excel_import(L3_yuzey_list, "V")

L3_smi_list = []
Excel_import(L3_smi_list, "W")

grup_komplike_apandisit_list = []
Excel_import(grup_komplike_apandisit_list, "Z")

t = 0
for i in range(52):
    print(morbidite_list[t], ameliyat_list[t], asa_skoru_list[t], age_list[t], gender_list[t], boy_list[t], bmi_list[t], ybu_list[t], wbc_list[t], crp_list[t], inr_list[t], hb_list[t], plt_list[t], alb_list[t], ht_list[t], dm_list[t], kah_list[t], koah_list[t], patoloji_list[t], L3_yuzey_list[t], L3_smi_list[t], grup_komplike_apandisit_list[t])
    t += 1
