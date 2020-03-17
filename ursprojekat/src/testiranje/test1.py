'''
Created on Jun 21, 2018

@author: Ljubica
'''

from prvi import vrednosti
import pytest
from funkcije.ucitavanja import ucitavanje_automobila
from prvi.putanje import autoFajl
from prvi.putanje import prazanFajl
from funkcije.f_auto import automobil_po_oznaci
from prvi.pocetak import Automobil


@pytest.fixture(scope="module")
def pripremi_automobile():
    vrednosti.automobili=ucitavanje_automobila(autoFajl)
@pytest.fixture(scope="module")
def pripremi_automobile_prazan_fajl():
    vrednosti.automobili=ucitavanje_automobila(prazanFajl)
    
def test_za_pretragu_po_oznaci(pripremi_automobile):
    automobili=automobil_po_oznaci("a1")
    assert automobili!=None
    assert type(automobili) is list
    assert len(automobili) == 1
    assert type(automobili[0]) is Automobil
    assert automobili[0].oznaka == "a1"
    
def test_pogresna_vrednost(pripremi_automobile):
    automobili=automobil_po_oznaci("aa1")
    assert automobili!=None
    assert type(automobili) is list
    assert len(automobili) == 0
    
def test_pretraga_case(pripremi_automobile):
    automobili=automobil_po_oznaci("A1")
    assert automobili!=None
    assert type(automobili) is list
    assert len(automobili) == 1
    assert type(automobili[0]) is Automobil
    assert automobili[0].oznaka == "a1"
    
#def test_pretraga_none(pripremi_automobile):
    #with pytest.raises(ValueError):
        #automobil_po_oznaci(None) 
    
#def test_pretraga_int(pripremi_automobile):
    #with pytest.raises(TypeError):
        #automobil_po_oznaci(1)
           
if __name__ == '__main__':
    pass