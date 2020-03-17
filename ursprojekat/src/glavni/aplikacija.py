'''
Created on Jun 20, 2018

@author: Ljubica
'''
from prvi import vrednosti
from glavni import glavni_meni
from funkcije.ucitavanja import ucitavanje_automobila, ucitavanje_dzipova,ucitavanje_kvadova,prikaz_vrednosti
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
    
    glavni_meni()
    print("Prekidanje izvrsavanja")