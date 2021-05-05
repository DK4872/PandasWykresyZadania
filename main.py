# #import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# #import xlrd
# #import openpyxl
#
# # ZAD1
# a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
# grupa = a.groupby(["Rok"]).agg({'Liczba': ['sum']})
#
# wykres1 = grupa.cumsum()
# print(wykres1)
# wykres1.plot()
# plt.show()
#
# # ZAD2
# a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
#
# grupa = a.groupby(["Plec"]).agg({'Liczba': ['sum']})
# wykres2 = grupa.plot.bar()
# wykres2.set_ylabel('Mld')
# wykres2.legend()
# plt.xticks(rotation=0)
# plt.title('Urodzone dzieci')
# plt.show()
# # ZAD3
# a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
# b = a[(a['Rok'] >= 2012)]
# grupa = b.groupby(["Plec"]).agg({'Liczba': ['sum']})
# wykres3 = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=15, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc='lower right')
# plt.show()
# # ZAD4
# a = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# grupa = a.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
#
# wykres4 = grupa.plot.bar()
# plt.show()
# plt.savefig('zad4.png')
