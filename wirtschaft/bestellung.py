class Bestellung:
    __menge = ""
    __preisprostueck = ""
    __versandkosten = ""   # __ für keinen Zugriff von Außen
    __bestellnummer = ""
    __bezeichnung = ""

    #Konstruktor
    def __init__(self):
        print("Objekt wurde erzeugt.")

    def setMenge(self, menge):
        self.__menge = menge

    def getMenge(self):
        return self.__menge

    def setPreis(self, preisprostueck):
        self.__preisprostueck = preisprostueck

    def getPreis(self):
        return self.__preisprostueck

    def setVersand(self, versandkosten):
        self.__versandkosten = versandkosten

    def getVersand(self):
        return self.__versandkosten

    def setBestellung(self, bestellnummer):
        self.__bestellnummer = bestellnummer

    def getBestellung(self):
        return self.__bestellnummer

    def setBezeichnung(self, bezeichunung):
        self.__bezeichnung = bezeichunung

    def getBezeichnung(self):
        return self.__bezeichnung
