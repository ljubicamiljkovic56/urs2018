'''
Created on Jun 20, 2018

@author: Ljubica
'''
from prvi.putanje import autoFajl, dzipFajl, kvadFajl
from prvi.pocetak import Automobil, Dzip, Kvad
from prvi.vrednosti import dzipovi, kvadovi
from prvi import vrednosti


def ucitavanje_automobila():
    automobili=[]
    with open(autoFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            maksimalna_brzina = int(fields[5])
            godina_proizvodnje  = int(fields[6])
            broj_sedista = int(fields[7])
            broj_vrata = int(fields[8])
            tip_menjaca = fields[9]
            automobili.append(Automobil(oznaka,opis,duzina,sirina,visina,maksimalna_brzina,godina_proizvodnje,broj_sedista,broj_vrata,tip_menjaca))
    return automobili        
            
def ucitavanje_dzipova():
    dzipovi=[]
    with open(dzipFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            konjskih_snaga = int(fields[5])
            broj_vrata = int(fields[6])
            spustajuca_zadnja_klupa = fields[7] 
            dzipovi.append(Dzip(oznaka,opis,duzina,sirina,visina,konjskih_snaga,broj_vrata,spustajuca_zadnja_klupa))
    return dzipovi                       

def ucitavanje_kvadova():
    kvadovi=[]
    with open(kvadFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            opis = fields[1]
            duzina = float(fields[2])
            sirina = float(fields[3])
            visina = float(fields[4])
            prostor_za_stvari = float[5]
            kvadovi.append(Kvad(oznaka,opis,duzina,sirina,visina,prostor_za_stvari))
    return kvadovi

def prikaz_vrednosti(lista):
    for i,el in enumerate(lista):
        print("{} {}".format(i, el))
if __name__ == '__main__':
    vrednosti.automobili=ucitavanje_automobila()
    vrednosti.dzipovi=ucitavanje_dzipova()
    vrednosti.kvadovi=ucitavanje_kvadova()
    
    print("Automobili")
    prikaz_vrednosti(vrednosti.automobili)
    print("Dzipovi")
    prikaz_vrednosti(vrednosti.dzipovi)
    print("Kvadovi")
    prikaz_vrednosti(vrednosti.kvadovi)