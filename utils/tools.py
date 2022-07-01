"""
Updated on 2022-04-28 10:28:52 

@author: mathieu.lacroix@cea.fr
"""

from multiprocessing.dummy import Array
import sqlite3

from pandas import array
import streamlit as st




#--------------Fonction-------------
def readTable(Table : str):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()
    cur = conn.cursor()

    for row in cur.execute("SELECT * from '%s'" %Table):
        print(row)

def saveCheckSum(cs : str):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO CheckSum VALUES (NULL, '%s')" %cs)
    conn.commit()

#vérification si le checksum existe
def verifCheckSum(cs : str):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()

    cur.execute("SELECT Id_CheckSum From CheckSum Where Hexa_CheckSum = '%s'"%cs)
    stResult = cur.fetchone()

    if stResult != None:
        return stResult
    else :
        print('rien trouvé')
        return None

def saveData(list_ : str):
    result = False
    try:
        conn = sqlite3.connect('BD/test_1.db')
        cur = conn.cursor()
        part1 = "INSERT INTO Fichier VALUES "
        part2 = list_

        output = part1+part2
        cur.execute(output)
        conn.commit()

        print('envoie réussie')

        conn.close()
        result = True
        
    except sqlite3.Error as error:
        print("Erreur lors de l'insertion", error)
    return result
def recupNameFile(id : int):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()

    cur.execute("SELECT Nom_Fichier From Fichier Where CheckSum_Fichier = '%s'"%id)
    rs = cur.fetchone()
    return rs

def recupFileFromPath(pt : str):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()

    rq = f"SELECT Id_Fichier, Nom_Fichier , Path_Fichier FROM FICHIER WHERE Path_Fichier LIKE '{pt}%'"
    cur.execute(rq)
    rs = cur.fetchall()
    print(rs)
    return rs

def recupFileFromPath2():
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()

    rq = f"SELECT Id_Fichier, Nom_Fichier , Path_Fichier FROM FICHIER"
    cur.execute(rq)
    rs = cur.fetchall()
    print(rs)
    return rs

def recupAll(nf : str):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()
    rq = f"SELECT * FROM FICHIER WHERE Nom_Fichier = '{nf}'"
    cur.execute(rq)
    rs = cur.fetchall()
    #print(rs)
    return rs 

def removeChecksumFromDB(cs):
    conn = sqlite3.connect('BD/test_1.db')
    cur = conn.cursor()
    rq = f"DELETE FROM CheckSum WHERE Hexa_CheckSum = '{cs}'"
    cur.execute(rq)
    conn.commit()
    conn.close()


    

#------------------------------------




