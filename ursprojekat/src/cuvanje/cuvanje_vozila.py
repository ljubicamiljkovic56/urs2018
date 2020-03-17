'''
Created on Jun 18, 2018

@author: Ljubica
'''
from prvi.vrednosti import automobili, dzipovi, kvadovi
from prvi.putanje import autoFajl, dzipFajl, kvadFajl
def cuvanje_auta(automobili):
    with open(autoFajl, "w") as f:
        for a in automobili:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.opis))
            f.write("{}|".format(a.duzina))
            f.write("{}|".format(a.sirina))
            f.write("{}|".format(a.visina))
            f.write("{}|".format(a.tip_menjaca))
            f.write("{}|".format(a.broj_sedista))
            
def cuvanje_dzipa(dzipovi):
    with open(dzipFajl, "w") as f:
        for d in dzipovi:
            f.write("{}|".format(d.oznaka))
            f.write("{}|".format(d.opis))
            f.write("{}|".format(d.duzina))
            f.write("{}|".format(d.sirina))
            f.write("{}|".format(d.visina))
            f.write("{}|".format(d.konjskih_snaga))
            f.write("{}|".format(d.spustajuca_zadnja_klupa))
            
def cuvanje_kvada(kvadovi):
    with open(kvadFajl, "w") as f:
        for k in kvadovi:
            f.write("{}|".format(k.oznaka))
            f.write("{}|".format(k.opis))
            f.write("{}|".format(k.duzina))
            f.write("{}|".format(k.sirina))
            f.write("{}|".format(k.visina))
            f.write("{}|".format(k.prostor_za_stvari))            
        

if __name__ == '__main__':
    pass