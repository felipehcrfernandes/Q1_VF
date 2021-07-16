import pandas as pd
import os
import glob
import numpy as np
import datetime

path = "Compras"
csv_files = glob.glob(os.path.join(path, "*.csv"))
d = {"item":[], "valor":[],"data da compra":[]}
D = pd.DataFrame(data=d)

for f in csv_files:      
    # read the csv file
    df = pd.read_csv(f,names=["item","valor","data da compra"])
    D = D.append(df,ignore_index=True)
#print(D)
#duplicate = D[D.duplicated(keep='last')]
lista = []
problemas = []
for i in D.item:
    if i not in lista:
        lista.append(i)  
for i in lista:
    x = D.loc[D.item == i]         
    minValue = x['valor'].min()
    limite = 1.25*minValue
    for j in x['valor']:
        aux = j
        aux = float(aux)
        if aux > limite:
            problemas.append(i)
            break
print(problemas)
f = open("relatorio.txt","w")
s =''

for i in problemas:
    line = ''
    x = D.loc[D.item == i]
    line = line + i + ","
    #count = 1
    for j in x["valor"]:
        c = x.loc[x.valor == j, 'data da compra']
        c = pd.to_datetime(c)
        aux_2 = str(c)
      
        print(c)              
        j = str(j)       
        line = line + j + ", " + aux_2[4:14] + ", "
      #  count = count + 1
    s = s + line + "\n"


'''
for i in problemas:
    x = D.loc[D.item == i]
    aux_1 = x 
    aux_1 = aux_1.to_string(index=False)
    s = s + aux_1 + "\n"
'''
f.write(s)
f.close()

 
