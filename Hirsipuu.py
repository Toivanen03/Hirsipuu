# Tuodaan tarvittavat moduulit.
#   - OS tuodaan, jotta voidaan käyttää CLS-komentoa näytön tyhjentämiseksi.
#   - Randomia hyödynnetään arvattavien sanojen sekä käyttäjälle tulostettavien kehujen arpomiseen
#   - Time-moduulia tarvitaan ohjelmassa käytettävien taukojen luomiseen sekä tilastoinnissa nopeimpien peliaikojen tallentamiseksi
#   - Keyboardilla saadaan määriteltyä mm. näppäimistön funktionäppäimet käytettäväksi pelissä pikanäppäiminä
#   - Getpass mahdollistaa kaksinpelissä syötteen piilottamisen arvattavaksi annettavaa sanaa kirjoittaessa

import os
import random
import time
import keyboard
import getpass


class Hirsipuu:

    def __init__(self, sana):
# Alustetaan pelin muuttujat
        self.sana = sana
        self.kirjaimet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
        self.vihje = []
        self.arvaukset = 8
        self.oikein_arvatut_kirjaimet = []
        self.vaarin_arvatut_kirjaimet = []
# Määritellään kehut, joista jokin tulostetaan satunnaisesti jokaisen oikean arvauksen jälkeen.
        self.kehut = ["Hyvä", "Hienoa", "Mahtavaa", "Upeaa", "Fantastista", "Superia", "Fantsua", "Kliffaa", "Vänkää", "Hieno homma", "Hyvin tehty", "Olet mestari", "Olet virtuoosi", "Äijä", "Kurko", "Äitisi on varmasti ylpeä sinusta"]       
# Pohjustetaan tilastointia varten muuttujat. Nopeimmat suoritukset näytetään TOP 10:ssä, mutta KAIKKI suoritukset tallennetaan tiedostoon.
        self.aloitusaika = 0
        self.lopetusaika = 0



    def pelin_aloitus(self):
        sekuntia = 6    # Alustaa muuttujan pelin aloitusnäyttöön

# Luodaan aloituksessa arvotun (tai kaksinpelissä valitun) sanan pohjalta aloitusvihje eli alaviivat, joista näkee arvattavan sanan kirjaimien lukumäärän.
# Oikeat kirjaimet päivittyvät tähän muuttujaan.    
        for k in self.sana:
            if k.upper() in self.kirjaimet:
                self.vihje.append("_")
            elif k == "-":
                self.vihje.append(k)

# "Vilkutusnäyttö", jossa kaksi sekunnin välein tulostuvaa näyttöä luovat vaikutelman, että osa tekstistä vilkkuisi näytöllä.
        os.system("cls")
        for x in range(3):

# Ensimmäinen osa tulostaa näytön kokonaan hirsipuineen päivineen...
            print("\n" * 5)
            print("                        *************************")
            print("                        ***  H I R S I P U U  ***")
            print("                        *************************")
            print("\n" * 5)
            print(" " * 65, "_____")
            print(" " * 64, "|   ","\|")
            print(" " * 63, "O      |")
            print(" " * 22, "PELI ALKAA !!!", sekuntia, "sekunnissa", " " * 11, "-|-     |")
            print(" " * 62, "/\     _⊥_")
            print(" " * 67, "oO   Oo")
            print(" " * 64, "oO        Oo")
            print(" " * 62, "oO            Oo")
            print("oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoO")
            print(f"\n\n\nArvauksia on yhteensä kahdeksan. Väärin arvattu kirjain TAI sana vähentää arvausvuoroja yhdellä.\n\nONNEA MATKAAN, {self.nimi.upper()} !!!")
            time.sleep(1)
            sekuntia -= 1

# ...toinen osa poistaa näytöstä hirsipuun ja "kivikon"
            os.system("cls")
            print("\n" * 5)
            print("                        *************************")
            print("                        ***  H I R S I P U U  ***")
            print("                        *************************")
            print("\n" * 8)
            print(" " * 22, "PELI ALKAA !!!", sekuntia, "sekunnissa")
            print(f"\n\n\n\n\n\n\n\nArvauksia on yhteensä kahdeksan. Väärin arvattu kirjain TAI sana vähentää arvausvuoroja yhdellä.\n\nONNEA MATKAAN, {self.nimi.upper()} !!!")
            time.sleep(1)
            sekuntia -= 1
            os.system("cls")
        self.aloitusaika = time.time()  # Pelin aloitusajan määrittely tilastointia varten
        self.arvaa_kirjain()    # Ohjaa metodiin, jossa pelaajaa pyydetään arvaamaan kirjain



# Tässä metodissa pyydetään kirjaimen arvausta ja tarkistetaan syötteen kelpoisuus.   
    def arvaa_kirjain(self):

        self.arvattu_kirjain = ""
# Jos väärin arvattuja kirjaimia on, niin tulostetaan tämä...
        if len(self.vaarin_arvatut_kirjaimet) > 0:
            print(f"Väärin arvatut kirjaimet: {', '.join(self.vaarin_arvatut_kirjaimet).upper()}, arvauksia jäljellä {self.arvaukset}.")

# ...muussa tapauksessa tämä.
        elif len(self.vaarin_arvatut_kirjaimet) == 0:
            print(f"Arvauksia jäljellä {self.arvaukset}.")
        print("\n" * 10)
        print(" " * 10, " ".join(self.vihje), "\n")

# Kirjainta pyydetään niin kauan, että syöte on kelpo.
        while len(self.arvattu_kirjain) != 1:
            self.arvattu_kirjain = input("Arvaa kirjain. Painamalla ENTER voit yrittää arvata sanan: ")
            if len(self.arvattu_kirjain) > 1:
                print("Näppäilyvirhe. Yritä uudelleen.")

# Enterin painalluksella eli tyhjällä syötteellä siirrytään sananarvausmetodiin
            elif self.arvattu_kirjain == "":
                self.arvaa_sana()

# Kirjaimen ollessa kelpo, siirrytään tarkistamaan sanan oikeellisuus.
            else:
                self.kirjain_tarkistus()



    def kirjain_tarkistus(self):

# Jokaista hirsipuun tulostetta varten on oma metodinsa. Metodeihin ohjaus tehdään listan avulla.
        animaatiot = [self.hirtetty, self.jalka, self.toinen_kasi, self.kasi, self.vartalo, self.paa, self.puu, self.kumpu]

# Alustetaan oikeat ja väärät kirjaimet omiin listoihinsa
        oikeat_kirjaimet = []
        vaarat_kirjaimet = []
        for i in self.sana:
            oikeat_kirjaimet.append(i.upper())
        for i in self.kirjaimet:
            if i not in oikeat_kirjaimet:
                vaarat_kirjaimet.append(i)
        os.system("cls")

# Päivitetään oikein arvatut kirjaimet isoina kirjaimina self.vihje-muuttujaan
        for ind in range(len(self.sana)):
            if self.arvattu_kirjain.lower() == self.sana[ind]:
                self.vihje[ind] = self.sana[ind].upper()

# Kirjain oikein       
        if self.arvattu_kirjain.upper() in oikeat_kirjaimet:
            if self.arvattu_kirjain.upper() in self.vihje and self.arvattu_kirjain.upper() in self.oikein_arvatut_kirjaimet:    # Tarkistetaan onko annettua kirjainta arvattu aiemmin
                print("Arvasit jo tämän kirjaimen oikein. Valitse uusi kirjain.")

# Tarkistetaan, onko kirjaimia vielä arvattavana. Jos sanaa ei ole vielä arvattu, on self.vihje-muuttujassa alaviivoja jäljellä.
            if "_" in self.vihje:
                if self.arvattu_kirjain.upper() in oikeat_kirjaimet:
                    if self.arvattu_kirjain.upper() not in self.oikein_arvatut_kirjaimet:   # Tässä varmistetaan, että annettu kirjain on uusi.
                        self.oikein_arvatut_kirjaimet.append(self.arvattu_kirjain.upper())  # Uudet arvatut kirjaimet lisätään arvattujen kirjaimien listaan
                        print(f"Kirjain löytyi sanasta! {random.choice(self.kehut)}, {self.nimi}!")

# Jos kaikki arvatut kirjaimet löytävät paikkansa:
            elif "_" not in self.vihje:                                                 # Muuttujassa ei ole enää alaviivoja jäljellä, eli kaikki kirjaimet on arvattu oikein.
                print(f"Hienoa, pelastuit hirsipuulta! Sana on {self.sana.upper()}.")
                self.peli["Pelin tulos"] = "Kaikki kirjaimet arvattu"                   # Pelin tulos tallennetaan sanakirjaan.
                self.pelin_lopetus()                                                    # Ohjataan lopetusmetodiin.

# Kirjain väärin
        elif self.arvattu_kirjain.upper() in vaarat_kirjaimet:                      # Tarkistetaan onko annettu kirjain aiemmin luodussa väärien kirjaimien listassa
            if self.arvattu_kirjain.upper() not in self.vaarin_arvatut_kirjaimet:   # Tarkistetaan onko annettua kirjainta arvattu aiemmin
                print(f"Arvattua kirjainta ei löydy.")

# Jo aiemmin väärin arvattu kirjain ei vähennä arvauksia...
            if self.arvattu_kirjain.upper() in self.vaarin_arvatut_kirjaimet:
                print("Kirjainta on jo arvattu. Sitä ei löytynyt sanasta. Anna uusi kirjain.")   

# ...uusi väärin arvattu kirjain vähentää.
            elif self.arvattu_kirjain.upper() not in self.vaarin_arvatut_kirjaimet:
                self.arvaukset -= 1                                                 # Vähennetään arvaus
                self.vaarin_arvatut_kirjaimet.append(self.arvattu_kirjain.upper())  # Väärin arvattu kirjain lisätään listaan
                if self.arvaukset >= 0 and self.arvaukset <= 7:                     # Tarkistetaan jäljellä olevien arvausten määrä
                    animaatio = animaatiot[self.arvaukset]                          # Jäljellä olevien arvausten määrää käytetään listan indeksinä hirsipuun tulostamiseksi.
                    animaatio()

# Tarkistetaan onko arvauksia jäljellä
            if self.arvaukset <= 0:
                self.arvaukset_loppu()

# Jos kirjaimia on vielä arvattavana, palataan pyytämään uutta kirjainta.
        if "_" in self.vihje:
            self.arvaa_kirjain()



# Metodin nimi kertoo oleellisen
    def arvaukset_loppu(self):
        print(f"Olet hirtetty! Sana oli {self.sana.upper()}.")
        self.peli["Pelin tulos"] = "Hirtetty"                   # Pelin tulos tallennetaan sanakirjaan.
        self.arvaukset = 8                                      # Arvauksien lukumäärä asetetaan alkuarvoon uutta peliä varten
        self.pelin_lopetus()



# Tänne voidaan siirtyä kirjaimenarvausmetodista tyhjällä syötteellä.
    def arvaa_sana(self):
        os.system("cls")
        print("\n" * 10)
        if len(self.vaarin_arvatut_kirjaimet) != 0:             # Tulostetaan viesti sen mukaan, onko väärin arvattuja kirjaimia tallennettu listaan.
            print(f"Arvauksia jäljellä {self.arvaukset}. Väärin arvatut kirjaimet ovat {', '.join(self.vaarin_arvatut_kirjaimet).upper()}")
        else:
            print(f"Arvauksia jäljellä {self.arvaukset}. Väärin arvattuja kirjaimia ei ole.")
        print("\n" * 3)
        print(" " * 10, " ".join(self.vihje), "\n")
        print()

# Pyydetään kokonaista sanaa. Tyhjällä syötteellä eli enterillä voidaan palata kirjaimen arvaukseen vähentämättä arvauskertoja.
        arvaus = input("Anna sana, jos haluat yrittää arvata sanaa. ENTER = Peruuta: ")
        if arvaus == "":
            os.system("cls")
            self.arvaa_kirjain()

# Jos sana arvataan oikein...
        elif arvaus.lower() == self.sana:
            print(f"Sana on oikein. Onneksi olkoon! {random.choice(self.kehut)}!")          # Arvotaan satunnainen kehu
            self.peli["Pelin tulos"] = "Sana arvattu"                                       # Pelin tulos tallennetaan sanakirjaan.
            self.pelin_lopetus()

# ...tai väärin. Tällöin tarjotaan mahdollisuutta arvata uudelleen tai palata kirjaimen arvaukseen.
        else:
            self.arvaukset -= 1                                                             # Väärin arvattu sana vähentää arvauskerran.
            uudelleen = input("Voi harmi, väärin meni. Haluatko arvata uudelleen? (K/E) ").lower()
            if self.arvaukset <= 0:
                self.arvaukset_loppu()                                                      # Jos arvaukset loppuvat, on pelin tulos hirtetty.
            if uudelleen == "k":
                os.system("cls")
                self.arvaa_sana()                                                           # Jos arvauksia on jäljellä, voidaan yrittää sanan arvausta uudelleen...
            elif uudelleen == "e":
                os.system("cls")
                self.arvaa_kirjain()                                                        # ...tai palata arvaamaan kirjaimia.



# Tässä metodissa peliaika pysähtyy. Kulunut peliaika tallentuu self.peli-muuttujaan ja tilastot tallennetaan tiedostoon.
    def pelin_lopetus(self):
        self.peli["Sana"] = self.sana.upper()                                   # Pelattu sana tallennetaan sanakirjaan.
        self.lopetusaika = time.time()                                          # Pelin lopetusaika
        peliaika = self.lopetusaika - self.aloitusaika                          # Lopetusajan ja aloitusajan erotus on käytetty peliaika...
        self.peli["Aika"] = time.strftime("%S", time.gmtime(peliaika))          # ...joka tallennetaan viimeiseksi sanakirjaan.

# Pelitietojen tallennus tiedostoon
        try:
            with open("tilastot.txt", "a", encoding="utf8") as tiedosto:
                tiedosto.write(f"{self.peli}\n")
        except Exception as e:
            print(f"Virhe tilastojen tallennuksessa: {e}")

# Muuttujat asetetaan tallennuksen jälkeen alkuarvoihinsa.
        self.oikein_arvatut_kirjaimet = []
        self.vaarin_arvatut_kirjaimet = []
        self.arvaukset = 8
        self.peli = {}
        self.vihje = []
        self.lopetus()



# Tänne siirrytään pelatun pelin jälkeen kaikissa tilanteissa.
    def lopetus(self):
        print("\n" * 5)
        print("Kiitos pelaamisesta!")
        print()
        input("Paina ENTER palataksesi päävalikkoon")
        self.aloitus()                                  # Palataan alkuvalikkoon, introa ei tulosteta pelatun pelin jälkeen uudelleen.



# Intro tulostuu vain ohjelman käynnistyksessä, uusintakierroksilla mennään suoraan aloitukseen.
    def intro(self):
        global ohita                                    # Määritetään globaali muuttuja sisäisen ohitusmetodin nähtäväksi
        ohita = False                                   # Muuttujan arvo on False, sillä intron ohitusta ei olla vielä pyydetty.
        self.peli = {}                                  # Luodaan sanakirja, johon pelitiedot tallentuvat
        num = 0                                         # Apumuuttuja intronäytön tulostamiseksi
        os.system("cls") 
        print("\n   Ohita intro painamalla ESC-näppäintä")



# Apumetodi, jonka avulla ESC keskeyttää intron tulostuksen
        def ohita_intro():
            global ohita                                
            ohita = True                                # Jos ESC-näppäintä painetaan, muuttujan arvoksi asetetaan True
            keyboard.unhook_all()                       # Vapautetaan pikanäppäimet, tässä tapauksessa ESC.
            return        
        

# ESC-näppäimen määritys ja intron luonti
        keyboard.add_hotkey("esc", ohita_intro)         # Määritetään pikanäppäin ja sille toiminto. Tässä tapauksessa ESC kutsuu apumetodia ohita_intro.    
        print("\n" * 8)
        rivit = [                                       # Intro-tulostuksen rivit listassa
            "                                                                        _____",
            "                                                                       |   \|",
            "                                                                       O    |",
            "                                                                      -|-   |",
            "                                                                       /\  _⊥_",
            "                                                                         oO   Oo",
            "                                                                       oO       Oo",
            "                                                                     oO           Oo",
            "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]

# Tämä tulostaa intronäytön rivi kerrallaan pitäen tauon rivien välillä.
        if ohita == False:                              # Tulostusta jatketaan rivi kerrallaan listan loppuun asti...
            for rivi in rivit:
                print(rivit[num])
                num += 1
                time.sleep(0.65)
                if ohita:                               # ...tai kunnes ESC painetaan.
                    break
            time.sleep(2)
        keyboard.unhook_all()                           # Pikanäppäimet vapautetaan tilanteessa, jossa ESC ei ole painettu.
        self.aloitus()



    def aloitus(self):

# Tilastojen luku ja tulostus, tarkistetaan onko tiedosto olemassa. F3 ohjaa tänne.

        def tulosta_tilastot():                         # Apumetodi, joka lukee tilastotiedot tiedostosta sekä tulostaa tiedoston sisällön määritellyn mukaisesti.
            os.system("cls") 
            try:
                with open("tilastot.txt", "r", encoding="utf8") as tiedosto2:
                    tilasto = tiedosto2.read()
                    if not tilasto:
                        raise ValueError("Tiedosto on tyhjä.")
                    tulos = tilasto.split("\n")
                os.system("cls")
                print("\n")
                print("                                               T O P   1 0\n")
                print("  Paina ESC poistuaksesi              *******************************                        Painamalla F10 voit poistaa tilastotiedot.")
                print("                                      ***  H A L L  O F  F A M E  ***")
                print("                                      *******************************\n\n")
                print("SIJA    PELAAJA                       TASO                          TULOS                         SANA                      AIKA (sek.)")
                print("-" * 135)
                print("\n")

# Siivotaan tiedoston tiedot ja muotoillaan sisältö takaisin sanakirjaksi
                poistot = ["Pelaaja", "Vaikeustaso", "Pelin tulos", "Sana", "Aika", ":", "'", " "]  # Lista poistettavista arvoista ja merkeistä.
                leveys = 30                                                                         # Apumuuttuja, jota käytetään myöhemmin tilastojen tulostuksessa
                nopeimmat = []                                                                      # Lista, johon tallennetaan tiedostosta luetut tiedot
                hirtetyt = []                                                                       # Tätä käytetään, mikäli tiedostossa ei ole onnistuneita suorituksia.
                for rivi in tulos:
                    rivi = rivi.strip("{}")                                                         # Siivotaan luettuja rivejä...
                    for poisto in poistot:
                        rivi = rivi.replace(poisto, "")
                    data = rivi.split(",")
                    try:
                        vertailu = int(data[-1])                                                    # Rivin viimeisen osan arvo on aika sekunteina.               
                        if data != "''":                                                            # Tiedoston loppuun tallentuneet ylimääräiset merkit jätetään huomiotta...
                            nopeimmat.append(data)                                                  # ...ja pelaajien tiedot tallennetaan listaan.                                               
                        if data != "''" and "Hirtetty" in data:                                     # Tehdään hirtetyistä oma listansa
                            hirtetyt.append(data)
                    except:
                        pass

# Tiedostoon tallentuvat kaikki suoritukset, tässä määritellään uuteen listaan TOP 10
                    for nopein in nopeimmat:
                        try:
                            if len(data) == 5:                                      # Varmistetaan rivien pituus
                                if vertailu < int(nopein[-1]):
                                    nopein = data
                        except:                                                     # Jos tiedoston sisältö on vääränlainen, tulostetaan virheilmoitus...
                            print("Tiedosto on viallinen.")
                            print("\nPaina ESC poistuaksesi.\n")
                            while True:
                                nappain = keyboard.read_event(suppress=True).name
                                if nappain == "esc":
                                    self.aloitus()                                  # ...ja palataan ESCillä aloitusvalikkoon.
                                keyboard.unhook_all()

# Suoritukset järjestykseen nopeimmasta alkaen
                lajiteltu = sorted(nopeimmat, key=lambda nopein: nopein[-1])                # Lajitellaan suodatetut arvot nopeusjärjestykseen
                luku = 0                                                                    # Apumuuttuja sijoitusten tulostukseen
                avaimet = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."]     # Sijoitukset luetaan listasta uuteen sanakirjaan avaimiksi
                sijoitukset = {avain: [] for avain in avaimet}                          
                for pelaaja in lajiteltu:
                    if luku < 10:

# Suodatetaan sanakirjaan vain onnistuneet suoritukset
                        if pelaaja[2] != "Hirtetty":
                            sijoitukset[avaimet[luku]].append(pelaaja)
                            luku += 1

# Jos tiedostossa on vain epäonnistuneita suorituksia, voidaan tarkastella hirtettyjen listaa.
                if luku == 0:
                    os.system("cls")
                    hirtetyt.reverse()                                                          # Käännetään lista takaperin, sillä uusimmat suoritukset tallentuvat tiedoston loppuun.
                    hirtetyt = hirtetyt[:10]
                    for hirtetty in hirtetyt:
                        if hirtetty[0] == "Nimetönpelaaja":
                            hirtetty[0] = "Nimetön pelaaja"                   
                    print("\nTIEDOSTOSSA EI OLE ONNISTUNEITA SUORITUKSIA\n")                        
                    jatka = ""                                                                    
                    while jatka != "k" or jatka != "e":
                        jatka = input("Haluatko nähdä listan hirtetyistä (K/E) ? ").lower()         
                        if jatka == "k":
                            os.system("cls")
                            print("\n")                                                         # Hirtettyjen listassa ei näytetä sijoitusta tai aikaa.
                            print("\n")
                            print("                                      *******************************")
                            print("                                      ***      10 viimeisintä     ***")
                            print("                                      ***    H I R T E T T Y Ä    ***")
                            print("                                      *******************************\n\n")
                            print("        PELAAJA                       TASO                          TULOS                         SANA")     
                            print("-" * 125)
                            print("\n")
                            for hirtetty in hirtetyt:
                                vali1 = " " * (8)
                                vali2 = " " * (leveys - len(hirtetty[0]))                       # Kaikki tulostukset saadaan siististi vähentämällä tulostettavien arvojen 
                                vali3 = " " * (leveys - len(hirtetty[1]))                       # pituus ennalta määritetystä sarakeleveydestä.
                                vali4 = " " * (leveys - len(hirtetty[2]))
                                print(f"{vali1}{hirtetty[0]}{vali2}{hirtetty[1]}{vali3}{hirtetty[2]}{vali4}{hirtetty[3]}\n")
                            jatka = input("\nPaina ENTER poistuaksesi. \n\n")
                            if jatka == "":
                                self.aloitus()
                            else:
                                self.aloitus()
                        if jatka == "e":                                         
                            self.aloitus()            

# TOP 10:n tulostus
                else:
                    for sija, pelaajat in sijoitukset.items():
                        for pelaaja in pelaajat:
                            for v in range(5):

    # Lisätään takaisin aiemmin poistetut välilyönnit oikeille paikoilleen
                                try:
                                    if pelaaja[2] == "Kaikkikirjaimetarvattu":
                                        pelaaja[2] = "Kaikki kirjaimet arvattu"
                                    if pelaaja[2] == "arvattu":
                                        pelaaja[2] = "Sana arvattu"
                                    if pelaaja[0] == "Nimetönpelaaja":
                                        pelaaja[0] = "Nimetön pelaaja"
                                    if pelaaja[4][0] == "0":                # Alle 10 sekunnin suorituksista poistetaan etunolla
                                        pelaaja[4] = pelaaja[4][-1]
                                except IndexError:                                  
                                    print("Tiedoston sisältö on vioittunut.")
                                    print("\nPaina ESC poistuaksesi.\n")
                                    while True:
                                        nappain = keyboard.read_event(suppress=True).name
                                        if nappain == "esc":
                                            self.aloitus()
                                        keyboard.unhook_all()

    # Määritellään sarakeleveydet ennen tulostusta
                                vali1 = " " * (8 - len(sija))
                                vali2 = " " * (leveys - len(pelaaja[0]))    # Kaikki tulostukset saadaan siististi vähentämällä tulostettavien arvojen 
                                vali3 = " " * (leveys - len(pelaaja[1]))    # pituus ennalta määritetystä sarakeleveydestä.
                                vali4 = " " * (leveys - len(pelaaja[2]))
                                vali5 = " " * (leveys - len(pelaaja[3]))
                            print(f"{sija}{vali1}{pelaaja[0]}{vali2}{pelaaja[1]}{vali3}{pelaaja[2]}{vali4}{pelaaja[3]}{vali5}{pelaaja[4]}\n")   # Tulostetaan lopuksi rivi kerrallaan Top 10.

# Tämä odottaa ESC:n painallusta ja tarjoaa mahdollisuuden tilastotiedoston poistoon
                while True:
                    nappain = keyboard.read_event(suppress=True).name
                    if nappain == "esc":
                        self.aloitus()                                  # ESCillä palataan aloitusvalikkoon...
                    elif nappain == "f10":                              # ... ja F10 poistaa tilastotiedot.
                        varmistus = ""
                        os.system("cls")
                        while varmistus != "k" and varmistus != "e":     # Varmistus vielä ennen tiedoston poistamista:
                            varmistus = input("\nHaluatko todella poistaa kaikki aiemmat tilastot?\n      TOIMINTOA EI VOI PERUUTTAA ! (K/E) ").lower()
                            if varmistus == "k":
                                if os.path.exists("tilastot.txt"):
                                    try:                                    
                                        os.system("del" + " " + "tilastot.txt")                                     # Määritetään komento tiedoston poistamiseksi
                                        takaisin = input("\nTilastotiedot poistettu\n\nPaina ENTER poistuaksesi.")
                                        if takaisin == "":
                                            self.aloitus()
                                            break
                                    except Exception as e:                      
                                        print(f"\nVirhe tiedoston poistossa: {e}")
                                        time.sleep(3)
                                        self.aloitus()
                                        break
                                else:
                                    print("\nTiedostoa ei löydy.")
                                    time.sleep(3)
                                    self.aloitus()
                                    break
                            elif varmistus == "e":
                                self.aloitus()
                        keyboard.unhook_all()
                        break

# Jos tilastotiedostoa ei löydy luettavaksi...
            except FileNotFoundError:
                print("Tiedostoa ei löydy.")
                print("\nEi aiempia tilastoja. Paina ESC poistuaksesi.\n")
                while True:
                    nappain = keyboard.read_event(suppress=True).name
                    if nappain == "esc":
                        self.aloitus()
                    keyboard.unhook_all()

# ...tai jos olemassa oleva tilastotiedosto on tyhjä.
            except ValueError as e:
                print(f"{e}")
                print("\nTiedosto on tyhjä. Paina ESC poistuaksesi.\n")
                while True:
                    nappain = keyboard.read_event(suppress=True).name
                    if nappain == "esc":
                        self.aloitus()
                    keyboard.unhook_all()



# F1 aloittaa yksinpelin           
        def yksi_pelaaja():

# Nimen syöttö. Tyhjällä syötteellä määritellään nimeksi "Nimetön pelaaja". Syötetyllä kirjainkoolla ei ole merkitystä,
# nimi muutetaan isolle alkukirjaimelle ja loput kirjaimet pieniksi.
            nimi = " "
            while len(nimi) == 1:
                nimi = input("Anna etunimesi tai nimikirjaimesi. Painamalla ENTER voit pelata nimettömänä. ")   # Nimeä käytetään pelinaikaisissa tulostuksissa
                if nimi == "":
                    self.nimi = "Nimetön pelaaja"                                                               # Tyhjällä syötteellä pelataan nimettömänä
                elif len(nimi) > 2 and len(nimi) < 20 and "." not in nimi:                                      # Syötetyssä nimessä tulee olla vähintään kolme kirjainta, mutta ei enempää kuin yhdeksäntoista.
                    self.nimi = nimi[0].upper() + nimi[1:].lower()                                              # Muutetaan nimen kirjoitusasu.
                elif "." in nimi:
                    if len(nimi) == 3:
                        self.nimi = nimi.upper() + "."
                    else:
                        self.nimi = nimi.upper()
                elif len(nimi) == 2:
                    if "." not in nimi:
                        self.nimi = nimi[0].upper() + "." + nimi[1].upper() + "."                               # Kahden nimikirjaimen syötteellä nimikirjaimet muutetaan isoiksi ja lisätään pisteet                      
            self.peli["Pelaaja"] = self.nimi                                                                    # Pelaajan nimi tallennetaan sanakirjaan                

# Vaikeustason valinta syötteen kelpoisuuden varmistuksineen
            vaikeustaso = input("Valitse (h)elppo tai (v)aikea taso: ").lower()
            if vaikeustaso not in ["h", "v"]:
                print("\nEpäkelpo valinta.")
                vaikeustaso = input("Valitse (h)elppo tai (v)aikea taso: ").lower()

# Helpolla tasolla listasta valitaan satunnainen 2-6 merkkiä pitkä sana...
            if vaikeustaso == "h":
                self.sana = random.choice([sana for sana in rivi1 if len(sana) >= 2 and len(sana) <= 6])        # Arvotaan 2-6 -kirjaiminen sana sanalistasta
                self.peli["Vaikeustaso"] = "Helppo"                                                             # Pelin vaikeustaso tallennetaan sanakirjaan

# ... ja vaikealla tasolla satunnainen vähintään seitsemän merkkiä pitkä sana
            elif vaikeustaso == "v":
                self.sana = random.choice([sana for sana in rivi1 if len(sana) > 6])                            # Arvotaan 7+ -kirjaiminen sana sanalistasta
                self.peli["Vaikeustaso"] = "Vaikea"                                                             # Pelin vaikeustaso tallennetaan sanakirjaan
            self.pelin_aloitus()                                                                                # Pelin käynnistys.



# F2 aloittaa kaksinpelin
        def kaksi_pelaajaa():
            keyboard.press_and_release("enter")                                                                 # Tyhjennetään näppäimistöpuskuri, ilman tätä
            input()                                                                                             # jää seuraavassa syötteessä ensimmäinen kirjain huomiotta
            nimi = " "    
            sana_vaarin = True
            nimi_vaarin = True
            print("\nPelaaja 2 on arvuuttaja, pelaaja 1 yrittää arvata sanaa.\n")
            self.sana = getpass.getpass(prompt="Pelaaja 2, anna sana arvattavaksi: ")                           # Syöte piilotetaan arvaajalta
            if self.sana.lower() in sanalista:
                sana_vaarin = False
            while sana_vaarin:                                                                                  # Oikean suomen kielen sanan syöttämisen jälkeen...
                self.sana = getpass.getpass(prompt="Anna sana: ")
                if self.sana.lower() in sanalista:
                    sana_vaarin = False
            while nimi_vaarin:                                                                                  # ...pyydetään sanaa arvaavan pelaajan nimeä.
                while len(nimi) == 1: 
                    nimi = input("Pelaaja 1, anna etunimesi tai nimikirjaimesi. Painamalla ENTER voit pelata nimettömänä. ")   
                    if nimi == "":
                        self.nimi = "Nimetön pelaaja" 
                        nimi_vaarin = False
                        break            
                    elif len(nimi) > 2 and len(nimi) < 20 and "." not in nimi:                                                     
                        self.nimi = nimi[0].upper() + nimi[1:].lower()
                        nimi_vaarin = False
                        break
                    elif "." in nimi:
                        if len(nimi) == 3:
                            self.nimi = nimi.upper() + "."
                            nimi_vaarin = False
                            break
                        else:
                            self.nimi = nimi.upper()       
                            nimi_vaarin = False
                            break                                
                    elif len(nimi) == 2:                                                                        
                        if "." not in nimi:
                            self.nimi = nimi[0].upper() + "." + nimi[1].upper() + "."
                            nimi_vaarin = False
                            break
            self.peli["Pelaaja"] = self.nimi                                    # Pelaajan nimi...
            self.peli["Vaikeustaso"] = "Kaksinpeli"                             # ...ja vaikeustaso tallennetaan pelin tietoihin sanakirjaan.    
            self.pelin_aloitus()



# Neljäs ja viimeinen apumetodi lopetus, johon tullaan painamalla ESC ja vahvistamalla poistuminen aloitusvalikossa.                        
        def poistu():
            exit()      
            


# Täällä luetaan sanalista, määritellään funktionäppäimet sekä tulostetaan avausruutu.    
        try:        
            with open("sanalista.txt", "r", encoding="utf-8") as tiedosto1:
                sanalista = tiedosto1.read()
                rivi1 = sanalista.split("\n")
        except:
            os.system("cls")
            print("\nSanalistaa ei löydy tai se on vioittunut\n\nOhjelma lopetetaan.\n")
            poistu()

        os.system("cls")
        print("\n" * 3)
        print("                        *************************")
        print("                        ***  H I R S I P U U  ***")
        print("                        *************************")
        print("\n" * 5)
        print("F1 - Yksinpeli\nF2 - Kaksinpeli\nF3 - Hall of fame\nESC - Poistu pelistä\n")

# Aloitusruudun pikanäppäinten määrittely ja odotustoiminnot
        while True:
            nappain = keyboard.read_event(suppress=True).name
            if nappain == "f1":
                yksi_pelaaja()
            elif nappain == "f2":
                kaksi_pelaajaa()
            elif nappain == "f3":
                tulosta_tilastot()
            elif nappain == "esc":
                vahvistus = ""


# Pelistä poistuminen
                while vahvistus != "k" or vahvistus != "e":
                    vahvistus = input("Haluatko varmasti poistua pelistä? (K/E) ").lower()
                    if vahvistus == "k":
                        print("\nTack för besöket och välkommen åter!\n")
                        time.sleep(2)
                        poistu()
                    elif vahvistus == "e":
                        self.aloitus()
            keyboard.unhook_all()



# Hirsipuun kahdeksan tulostusmetodia
    def hirtetty(self):                         # Hirtetyksi tullessa "animointi" on erilainen kuin muissa tulostuksissa.
        os.system("cls")
        print("\n" * 2)
        rivit = [
        "                                                                        _____",
        "              P E L I   P Ä Ä T T Y I                                  |   \|                                       G A M E   O V E R",
        "                                                                       O    |",
        "           J O U D U I T   H I R T E E N                              -|-   |                                Y O U ' V E   B E E N   H U N G",
        "                                                                       /\  _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for x in range(5):
            os.system("cls")
            for rivi in rivit:
                print(rivi)
                time.sleep(0.03)
            time.sleep(0.35)
        time.sleep(1)
        print("\n")



    def jalka(self):                            # Jos arvauksia on jäljellä, tilanteen mukainen "kuva" tulostuu näytölle rivi kerrallaan.
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                       |   \|",
        "                                                                       O    |",
        "                                                                      -|-   |",
        "                                                                       /   _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def toinen_kasi(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                       |   \|",
        "                                                                       O    |",
        "                                                                      -|-   |",
        "                                                                           _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def kasi(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                       |   \|",
        "                                                                       O    |",
        "                                                                      -|    |",
        "                                                                           _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def vartalo(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                       |   \|",
        "                                                                       O    |",
        "                                                                       |    |",
        "                                                                           _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def paa(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                       |   \|",
        "                                                                       O    |",
        "                                                                            |",
        "                                                                           _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def puu(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "                                                                        _____",
        "                                                                           \|",
        "                                                                            |",
        "                                                                            |",
        "                                                                           _⊥_",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



    def kumpu(self):
        os.system("cls")
        print("\n" * 10)
        rivit = [
        "",
        "",
        "",
        "",
        "                                                                           ___",
        "                                                                         oO   Oo",
        "                                                                       oO       Oo",
        "                                                                     oO           Oo",
        "oOOoOOooOOoooOOooOOOoooOOOoOOoOoOOoOOoOOoOOOoOOOOOoooOoOOoOoooOOOOoOoOOOoOOOOOOOOOOoOOOOOOooOoooOoOOooOoOoooOOOoOOOOOOOoooOoOOoOOOOOOoOOoooOoOOooOoOooOooOooOOoOooOooOoOoOoOoOoOOOOoOOO"]
        for rivi in rivit:
            print(rivi)
            time.sleep(0.15)
        time.sleep(2)
        os.system("cls")



if __name__=="__main__":
    hirsipuu = Hirsipuu("") # Hirsipuulle annetaan aloituksessa parametriksi tyhjä sana.
    hirsipuu.intro()