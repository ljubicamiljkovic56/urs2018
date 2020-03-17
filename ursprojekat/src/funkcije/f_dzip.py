'''
Created on Jun 20, 2018

@author: Ljubica
'''
from cuvanje.cuvanje_vozila import cuvanje_dzipa
from pomocni_paket.pomocne_metode import provera_unosa, unos_boolean
from prvi.pocetak import Dzip
from prvi import vrednosti
from pomocni_paket.pomocne_metode import prikaz_menija
from prvi.vrednosti import dzipovi

def meni_dzipovi():
    while True:
        prikaz_menija("Koju opciju zelite: ", "1 - Unos dzipa",
                      "2 - Prikaz dzipa", "3 - Sortiranje dzipa")
        opcija=provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 4:
            break
        elif opcija == 1:
            d=unos_dzipa()
            vrednosti.dzipovi.append(d)
            cuvanje_dzipa(vrednosti.dzipovi)
            print("Dzip uspesno kreiran {}".format(d))
        elif opcija == 2:
            prikaz_dzipova(vrednosti.dzipovi)
        elif opcija == 3:
            sortiranje_dzipa()
            
def unos_dzipa():
    print("Unos vrednosti za dzip")
    oznaka=unos_oznake_dzipa("Oznaka: ", False)
    opis=input("Opis: ")
    duzina=provera_unosa("Duzina: ", "Duzina mora biti decimalna vrednost", float)
    sirina=provera_unosa("Sirina: ", "Sirina mora biti decimlna vrednost", float)
    visina=provera_unosa("Visina: ", "Visina mora biti decimalna vrednost", float)
    konjskih_snaga=provera_unosa("Konjskih snaga: ", "Konjske snage moraju biti celobrojna vrednost", int)
    spustajuca_zadnja_klupa=unos_boolean("Spustajuca zadnja klupa: ", "Morate upisati da ili ne")
    d=Dzip(oznaka,opis,duzina,sirina,visina,konjskih_snaga,spustajuca_zadnja_klupa)
    return d

def prikaz_dzipova():
    print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format("Oznaka","Opis","Duzina","Sirina","Visina","Konjskih snaga","Spustajuca zadnja klupa"))
    
    for d in dzipovi:
        print("{:10}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}".format(d.oznaka,d.opis,d.duzina,d.sirina,d.visina,d.konjskih_snaga,d.spustajuca_zadnja_klupa))

def unos_oznake_dzipa(poruka, postoji):
    if postoji:
        greska = "Dzip sa oznakom ne postoji"
    else:
        greska = "Dzip sa oznakom vec postoji"
    
    while True:
        vrednost=input(poruka)
        
        if vrednost is None or vrednost == "":
            break
        else:
            dzip=dzip_po_oznaci(vrednost)
            if dzip is None and postoji:
                print(greska)
            elif dzip is not None and not postoji:
                print(greska)
            else:
                return vrednost
            
def sortiranje_dzipa():
    while True:
        prikaz_menija("Sortiranje dzipova","1 - po maksimalnoj brzini", "2 - po broju konjskih snaga", "3 - Izlaz")
        opcija=provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrendost", int)
        if opcija == 3:
            break
        elif opcija == 1:
            sortirani=sortiranje_po_maksimalnoj_brzini(vrednosti.dzipovi)
            prikaz_dzipova(sortirani)
        elif opcija == 2:
            sortirani= sortiranje_po_konjskim_snagama(vrednosti.dzipovi)
            prikaz_dzipova(sortirani)
            
def sortiranje_po_maksimalnoj_brzini(dzipovi):
    nova_lista = []
    nova_lista.extend(dzipovi)
    nova_lista.sort(key=lambda x:x.maksimalna_brzina, reverse=False)
    return nova_lista

def sortiranje_po_konjskim_snagama(dzipovi):
    nova_lista = []
    nova_lista.extend(dzipovi)
    nova_lista.sort(key=lambda x:x.konjskih_snaga, reverse=False)
    return nova_lista 

def dzip_po_oznaci(oznaka):
    for d in dzipovi:
        if d.oznaka == oznaka:
            return d  

if __name__ == '__main__':
    pass