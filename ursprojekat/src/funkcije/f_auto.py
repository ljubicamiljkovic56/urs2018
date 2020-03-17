'''
Created on Jun 19, 2018

@author: Ljubica
'''
from pomocni_paket.pomocne_metode import prikaz_menija, provera_unosa,\
    unos_boolean
from prvi import vrednosti
from cuvanje.cuvanje_vozila import cuvanje_auta
from prvi.pocetak import Automobil
from prvi.vrednosti import automobili

def meni_automobili():
    while True:
        prikaz_menija("Koju opciju zelite: ", "1 - Unos automobila",
                      "2 - Prikaz automobila", "3 - Sortiranje automobila")
        opcija=provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 4:
            break
        elif opcija == 1:
            a=unos_automobila()
            vrednosti.automobili.append(a)
            cuvanje_auta(vrednosti.automobili)
            print("Automobil uspesno kreiran {}".format(a))
        elif opcija == 2:
            prikaz_automobila(vrednosti.automobili)
        elif opcija == 3:
            sortiranje_auta()
            
def unos_automobila():
    print("Unos vrednosti za automobil")
    oznaka=unos_oznake_automobila("Oznaka: ", False)
    opis=input("Opis: ")
    duzina=provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina=provera_unosa("Sirina: ", "Sirina mora biti decimlna vrednost", float)
    visina=provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    tip_menjaca=unos_boolean("Tip menjaca", "Morate da unesete da li je automatski ili manuelni")
    broj_sedista=provera_unosa("Broj sedista", "Broj sedista mora biti celobrojna vrednost", int)
    a=Automobil(oznaka,opis,duzina,sirina,visina,tip_menjaca,broj_sedista)
    return a

def prikaz_automobila():
    print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format("Oznaka", "Opis", "Duzina",
                                                             "Sirina", "Visina", "Tip menjaca", "Broj sedista"))
    for a in automobili:
        print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format(a.oznaka,a.opis,a.duzina,a.sirina,a.visina,a.tip_menjaca,a.broj_sedista))
   
def unos_oznake_automobila(poruka,postoji):
    if postoji:
        greska = "Automobil sa oznakom ne postoji"
    else:
        greska = "Automobil sa oznakom vec postoji"
        
    while True:
        vrednost=input(poruka)
        if vrednost is None or vrednost == "":
            break
        else:
            automobil=automobil_po_oznaci(vrednost)
            if automobil is None and postoji:
                print(greska)
            elif automobil is None and not postoji:
                print(greska)
            else:
                return vrednost
            
def sortiranje_auta():
    while True:
        prikaz_menija("Sortiranje automobila: ", "1 - po maksimalnoj brzini ", "2 - po broju sedista ", "3 - Izlaz")
        opcija=provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 3:
            break
        elif opcija == 1:
            sortirani=sortiranje_po_maksimalnoj_brzini(vrednosti.automobili)
            prikaz_automobila(sortirani)
        elif opcija == 2:
            sortirani=sortiranje_po_broju_sedista(vrednosti.automobili)
            prikaz_automobila(sortirani)
            
def sortiranje_po_maksimalnoj_brzini(automobili):
    nova_lista = [] 
    nova_lista.extend(automobili)
    nova_lista.sort(key=lambda x:x.maksimalna_brzina, reverse=False)
    return nova_lista

def sortiranje_po_broju_sedista(automobili):
    nova_lista = []
    nova_lista.extend(automobili)
    nova_lista.sort(key=lambda x:x.broj_sedista, reverse=False)
    return nova_lista

def automobil_po_oznaci(oznaka):
    for a in automobili:
        if a.oznaka == oznaka:
            return a   
            

if __name__ == '__main__':
    pass