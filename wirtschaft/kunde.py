class Kunde:
    __vorname = ""
    __nachname = ""
    __e_mail = ""
    __tel_nummer = ""
    __strasse = ""
    __hausnummer = ""
    __plz = ""
    __ort = ""
    __bestellungen = []

    def addBestellung(self, bestellung):
        self.__bestellungen.append(bestellung)
    def stornoAlle(self):
        self.__bestellungen.clear()
    def getBestellung(self):
        return self.__bestellungen
    def __init__(self):
        print("Objekt wurde erzeugt.")

    def setVorname(self,vorname):
        self.__vorname = vorname
    def getVorname(self):
        return self.__vorname
    def setNachname(self,nachname):
        self.__nachname = nachname
    def getNachname(self):
        return self.__nachname
    def setEmail(self,e_mail):
        self.__e_mail = e_mail
    def getEmail(self):
        return self.__e_mail
    def setTel(self,tel_nummer):
        self.__tel_nummer = tel_nummer
    def getTel(self):
        return self.__tel_nummer
    def setStrasse(self,strasse):
        self.__strasse = strasse
    def getStrasse(self):
        return self.__strasse
    def setHausnummer(self,hausnummer):
        self.__hausnummer = hausnummer
    def getHausnummer(self):
        return self.__hausnummer
    def setPlz(self,plz):
        self.__plz = plz
    def getPlz(self):
        return self.__plz
    def setOrt(self,ort):
        self.__ort = ort
    def getOrt(self):
        return self.__ort