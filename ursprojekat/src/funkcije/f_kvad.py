'''
Created on Jun 20, 2018

@author: Ljubica
'''
from cuvanje.cuvanje_vozila import cuvanje_kvada
from prvi.vrednosti import kvadovi
from pomocni_paket.pomocne_metode import prikaz_menija, provera_unosa,\
    unos_boolean
from prvi import  vrednosti
from prvi.pocetak import Kvad
def meni_kvadovi():
    while True:
        prikaz_menija("Koju opciju zelite: ", "1 - Unos kvada",
                      "2 - Prikaz kvada", "3 - Sortiranje kvada")
        opcija=provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 4:
            break
        elif opcija == 1:
            k=unos_kvada()
            vrednosti.kvadovi.append(k)
            cuvanje_kvada(vrednosti.kvadovi)
            print("Kvad uspesno kreiran {}".format(k))
        elif opcija == 2:
            prikaz_kvadova(vrednosti.kvadovi)
        elif opcija == 3:
            sortiranje_kvadova()
            
            
def unos_kvada():
    print("Unos vrednosti za kvad")
    oznaka=unos_oznake_kvada("Oznaka: ", False)
    opis=input("Opis: ")
    duzina=provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina=provera_unosa("Sirina: ", "Sirina mora biti decimlna vrednost", float)
    visina=provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    prostor_za_stvari=unos_boolean("Prostor za stvari: ", "Morate uneti da ili ne")
    k=Kvad(oznaka,opis,duzina,sirina,visina,prostor_za_stvari)
    return k

def prikaz_kvadova():
    print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format("Oznaka","Opis","Duzina","Sirina","Visina","Prostor za stvari"))
    
    for k in kvadovi:
        print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format(k.oznaka,k.opis,k.duzina,k.sirina,k.visina,k.prostor_za_stvari))

def unos_oznake_kvada(poruka,postoji):
    if postoji:
        greska = "Kvad sa oznakom ne postoji"
    else:
        greska = "Kvad sa oznakom vec postoji"
    
    while True:
        vrednost=input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            kvad=kvad_po_oznaci(vrednost)
            if kvad is None and postoji:
                print(greska)
            elif kvad is not None and not postoji:
                print(greska)
            else:
                return vrednost
            
def sortiranje_kvadova():
    while True:
        prikaz_menija("Sortiranje kvadova: ", "1 - po maksimalnoj brzini", "2 - po godini proizvodnje", "3 - Izlaz")
        opcija = provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 3:
            break
        elif opcija == 1:
            sortirani = sortiranje_po_maksimalnoj_brzini(vrednosti.kvadovi)
            prikaz_kvadova(sortirani)
        elif opcija == 2:
            sortirani = sortiranje_po_godini_proizvodnje(vrednosti.kvadovi)
            prikaz_kvadova(sortirani)
            
def sortiranje_po_maksimalnoj_brzini(kvadovi):
    nova_lista = []
    nova_lista.extend(kvadovi)
    nova_lista.sort(key=lambda x:x.maksimalna_brzina, reverse=False)
    return nova_lista

def sortiranje_po_godini_proizvodnje(kvadovi):
    nova_lista = []
    nova_lista.extend(kvadovi)
    nova_lista.sort(key=lambda x:x.godina_proizvodnje, reverse=False)

def kvad_po_oznaci(oznaka):
    for k in kvadovi:
        if k.oznaka == oznaka:
            return k  

if __name__ == '__main__':
    pass