'''
Created on Jun 19, 2018

@author: Ljubica
'''

def prikaz_menija(*meni_opcije):
    for i in range(3):
        print()
    for i in meni_opcije:
        print(i)
        
def unos_stringa(poruka, greska):
    while True:
        vrednost=input(poruka)
        if vrednost is None or vrednost == "":
            print(greska)
        else:
            return vrednost
        
def unos_boolean(poruka, greska):
    while True:
        vrednost=input(poruka + "[d/n]:")
        if vrednost is None or vrednost == "":
            print(greska)
        else:
            b=True if vrednost == "d" else False
            return b
        
def provera_unosa(poruka, greska, convert):
    while True:
        try:
            return convert(input(poruka))
        except:
            print(greska)
            
def vrednost_za_pretragu(poruka, convert):
    try:
        return convert(input(poruka))
    except:
        return None
        

if __name__ == '__main__':
    pass