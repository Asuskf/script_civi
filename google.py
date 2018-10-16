#_*_ coding: utf-8 _*_
import pandas as pd
import numpy as np

archivo = 'civi.csv' #Nombre del archivo que contiene los datos
archivoExportado = 'subirUsuarios.csv' #Nombre del archivo que se va a exportar despues de las operaciones

datos = pd.read_csv(archivo,delimiter=',', encoding = 'utf8')
diccionario = dict(datos.to_dict(orient="index"))
nuevo = pd.DataFrame(diccionario)
nuevo.fillna(" ", inplace=True)
print(nuevo.keys())



exportar = open(archivoExportado,'w')
titulos = "Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value\n"
exportar.write(titulos)

for csv in nuevo.keys():
    Name = nuevo[csv]['Nombre']
    GivenName = str(nuevo[csv]['Segundo Nombre'])
    AdditionalName = int(nuevo[csv]['Casa-Teléfono-Mobile'])
    filas = Name+","+GivenName+","+AdditionalName+"\n"
    exportar.write(filas)
exportar.close()
