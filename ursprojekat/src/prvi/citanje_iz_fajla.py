'''
Created on Jun 3, 2018

@author: Ljubica
'''
from prvi.putanje import autoFajl, dzipFajl, kvadFajl

def citanje_automobila():
    automobili=[]
    with open(autoFajl) as f:
        for line in f:
            fields=line.split("|")
            oznaka=fields[0]
            opis=fields[1]
    return automobili

def citanje_dzipova():
    dzipovi=[]
    with open(dzipFajl) as f:
        for line in f:
            fields=line.split("|")
            oznaka=fields[0]
            opis=fields[1]
    return dzipovi

def citanje_kvadova():
    kvadovi=[]
    with open(kvadFajl) as f:
        for line in f:
            fields=line.split("|")
            oznaka=fields[0]
            opis=fields[1]
    return kvadovi

if __name__ == '__main__':
    pass