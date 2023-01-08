import openpyxl
import operator as op
import ville
import re

def nbr_par_commune () :

    workbook = openpyxl.load_workbook('exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
    
    valeur = []
    citi = []
    colonnes = []
    for r in onglet1['L3':'L272']:
        colonnes.append([cell.value for cell in r])
    
    for i in colonnes:
        c = str(i)
        a = re.sub(r"[^a-zA-Z0-9]","",c)
        citi.append(a)
    
    city = []
    for i in ville.ville():
        city.append(i)
    
    # x représente le nombre de communes        
    x = len(city)
    x = x-1     #position du dernier élément de la liste
    
    
    for j in (citi) :
        while x >=0 :     #Pour aller jusqu'à l'élément d'id 0 de la liste
           valeur.append(op.countOf(citi, city[x]))
           x = x-1
    return valeur
