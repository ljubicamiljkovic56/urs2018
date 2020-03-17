'''
Created on Jun 22, 2018

@author: Ljubica
'''
from prvi.vrednosti import automobili
from funkcije.ucitavanja import ucitavanje_automobila
from prvi.putanje import autoFajl, prazanFajl
from builtins import list
import pytest
from prvi.pocetak import Automobil

def test_ucitati_autoFajl():
    automobili=ucitavanje_automobila(autoFajl)
    assert automobili!=None
    assert type(automobili) is list
    
def test_ucitati_automobile_prazan_fajl():
    automobili=ucitavanje_automobila(prazanFajl)
    assert automobili!=None
    assert type(automobili) is list 
    assert len(automobili) == 0   
    assert type(automobili[0]) is Automobil
    assert automobili[0].oznaka == "a1"

#def test_ucitati_none():
    #with pytest.raises(ValueError):
        #ucitavanje_automobila(None)
        
#def test_ucitati_int():
    #with pytest.raises(TypeError):
        #ucitavanje_automobila(1)

if __name__ == '__main__':
    pass