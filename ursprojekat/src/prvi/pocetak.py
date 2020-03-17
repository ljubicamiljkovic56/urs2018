'''
Created on May 13, 2018

@author: Ljubica
'''

class Identifikacija(object):
    def __init__(self, oznaka, opis, **kwargs):
        super().__init__(**kwargs)
        self.oznaka = oznaka
        self.opis = opis
    def __str__(self, *args, **kwargs):
        return "{} {} ".format(self.oznaka, self.opis)

class Dimenzije(object):
    def __init__(self, duzina, sirina, visina, **kwargs):
        super().__init__(**kwargs)
        self.duzina = duzina
        self.sirina = sirina
        self.visia = visina
        
    @property
    def duzina(self):
        return self.__duzina
    @duzina.setter
    def duzina(self, value):
        if value <= 0:
            raise ValueError("Vrednost duzine mora biti veca od nule.")
        self.__duzina = value
    @property
    def sirina(self):
        return self.__sirina
    @sirina.setter
    def sirina(self, value):
        if value <= 0:
            raise ValueError("Vrednost sirine mora biti veca od nule.")
        self.__sirina = value
    @property
    def visina(self):
        return self.__visina
    @visina.setter
    def visina(self, value):
        if value <= 0:
            raise ValueError("Vrednost visine mora biti veca od nule.")
        self.__visina = value
    def __str__(self):
        return "{} {} {}".format(self.duzina, self.sirina, self.visina)
    
class IzlozbeniProstor(Identifikacija):
    def __init__(self,oznaka, opis):
        super.__init__(oznaka=oznaka, opis=opis)
    
        
    @property
    
    def lokacija(self):
        return self.__lokacija
    
    def __str__(self):
        return "{}".format(self.lokacija)
    
class Vozilo(Identifikacija, Dimenzije):
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje, broj_vrata):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina,visina=visina)
        self.maksimalna_brzina = maksimalna_brzina
        self.godina_proizvodnje = godina_proizvodnje
        self.broj_vrata = broj_vrata
        
    def __str__(self):
        return "{} {}".format(self.maksimalna_brzina, self.godina_proizvodnje)
    
class PutnickoVozilo(Vozilo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje,  broj_vrata):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina, maksimalna_brzina=maksimalna_brzina,godina_proizvodnje=godina_proizvodnje, broj_vrata=broj_vrata)
        self.broj_vrata = broj_vrata
        
    def __str__(self):
        return Vozilo.__str__(self)
    
class TerenskoVozilo(Vozilo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, pogon_na_sva_cetiri_tocka):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina)
        self.pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka
        
    def __str__(self):
        return "{}".format(self.pogon_na_sva_cetiri_tocka)
    
class Automobil(PutnickoVozilo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje, broj_vrata, broj_sedista, tip_menjaca):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina, maksimalna_brzina=maksimalna_brzina, godina_proizvodnje=godina_proizvodnje, broj_vrata=broj_vrata)
        self.broj_sedista = broj_sedista
        self.tip_menjaca = tip_menjaca
        
    def __str__(self):
        return "{} {}".format(self.broj_sedista, self.tip_menjaca)
    
class Dzip(PutnickoVozilo, TerenskoVozilo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje,konjskih_snaga, broj_vrata, spustajuca_zadnja_klupa):
        super().__init__(oznaka=oznaka, opis=opis, duzina=duzina, sirina=sirina, visina=visina, maksimalna_brzina=maksimalna_brzina, godina_proizvodnje=godina_proizvodnje, broj_vrata=broj_vrata)
        self.konjskih_snaga = konjskih_snaga
        self.spustajuca_zadnja_klupa = spustajuca_zadnja_klupa
        
    def __str__(self):
        return "{} {}".format(self.konjskih_snaga, self.spustajuca_zadnja_klupa)

class Kvad(TerenskoVozilo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, prostor_za_stvari):
        super().__init__(oznaka=oznaka, opis=opis,duzina=duzina, sirina=sirina, visina=visina)
        self.prostor_za_stvari = prostor_za_stvari
        
    def __str__(self):
        return "{}".format(self.prostor_za_stvari) 