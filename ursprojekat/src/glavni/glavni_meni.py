'''
Created on Jun 19, 2018

@author: Ljubica
'''
from pomocni_paket.pomocne_metode import prikaz_menija, provera_unosa
from funkcije.f_auto import meni_automobili
from funkcije.f_dzip import meni_dzipovi
from funkcije.f_kvad import meni_kvadovi
def glavni_meni():
    while True:
        prikaz_menija("Koju opciju zelite: ", "1 - Automobili",
                      "2 - Dzipovi", "3 - Kvadovi", "4 - Izlaz")
        opcija = provera_unosa("Opcija: ", "Opcija mora biti celobrojna vrednost", int)
        if opcija == 4:
            break
        elif opcija == 1:
            meni_automobili()
        elif opcija == 2:
            meni_dzipovi()
        elif opcija == 3:
            meni_kvadovi() 