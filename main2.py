from wirtschaft import Bestellung

bestellung_1 = Bestellung()
bestellung_1.setMenge(20)
bestellung_1.setPreis(3)
bestellung_1.setVersand(1)
bestellung_1.setBestellung(49391)
bestellung_1.setBezeichnung("Buch")
bestellung_2 = Bestellung()
bestellung_2.setBezeichnung("Sachen")

#print(bestellung_1.getMenge())
#print(bestellung_1.getPreis())
#print(bestellung_1.getVersand())
#print(bestellung_1.getBestellung())
#print(bestellung_1.getBezeichnung())
from wirtschaft import Kunde

kunde1 = Kunde()
kunde1.setVorname("Hans")
kunde1.setNachname("Meier")
kunde1.addBestellung(bestellung_1)
kunde1.addBestellung(bestellung_2)
