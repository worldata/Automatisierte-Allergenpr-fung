import csv
import glob
import locale
locale.setlocale(locale.LC_ALL, 'de_DE')
import os.path, time
from datetime import datetime


for file in glob.glob("C:\\Users\\Maximilian.Rasch\\Desktop\\Kataloge_Rechnungen\\Kataloge/*.csv"):
    p = file

# Pfad eingeben

time = os.path.getmtime(p)
Katalogdatum = datetime.fromtimestamp(time).strftime('%d.%m.%Y')


with open(p, "r", newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    def linefinder(x):


        for column in csv_reader:
            if column[6] == str(x):
                print("Lieferantenname: " + Firmenname)
                print()
                print("Artikel: " + column[9])
                print("Artikelnummer: " + column[8])
                print("Bestelleinheit: " + column[18])
                print("Preis der Bestelleinheit: " + column[30])
                print("Fixe Bestellmenge: " + column[25])
                print("Gewichtsartikelflag: " + column[22])
                print()
                print("Eine Packung enthält " + column[35] + " " + column[34] + ".")

    def artikel_suchen(x):

        for column in csv_reader:
            if column[6] == str(x):
                print("Artikelnummer = " + column[8])
                print("Artikelname = " + column[9])
                print(column)
                print(column[76])

                break
        else:
            print(str(x) + " wurde nicht gefunden!")
    # für x einfach Artikelnummer eingeben


    def Preisrechner():
        Summe = 0
        for column in csv_reader:
            Summe += locale.atof(column[20])
        print(Summe)
    # nur ausführen

    def Artikelüberprüfung_inhaltlich(x):
        for column in csv_reader:
            if column[6] == str(x):
                print("Artikelnummer = " + column[6])
                print("Artikelname = " + column[9])
                print("Der Artikel " + column[9] + " wird in der Einheit " + column[14] + " bestellt. Die Bestellung ""ist in " + column[35] +"er Schritten möglich. Demnach kosten " + column[35] + " " + column[14] + " " + column[20] +  "€.")
                print()
                if column[31] == "":
                    print("Es wurde keine fixe Bestellmenge angegeben. Dadurch kann die Bestellung in jeglichen "
                          "Mengen, z.B. 1,5 Stück oder 2,33 KG erfolgen. Wenn dies ein Problem darstellt bitte ich "
                          "Sie, bei KG Artikeln eine 1 und bei Stückartikeln die Mindestbestellmenge anzugeben.")
                else:
                    print("Sie haben bei dem Artikel " + column[9] + " die folgende fixe Bestellmenge angegeben: " +
                          column[31])
                    print()


                    fixeb_vielfaches = []
                    for e in range(1, 6):
                        fixeb_vielfaches.append(int(column[31]) * e)
                    print("Bitte beachten Sie, dass ein Vielfaches der angegebenen fixen Bestellmenge bestellt werden kann. Also in folgenden Schritten: " + str(fixeb_vielfaches))

    # für x einfach Artikelnummer eingeben


    def Allergenprüfung():

        with open(p, "r", newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            for column in csv_reader:
                global Firmenname
                Firmenname = column[6]
                break

            print("Lieferantenname: " + str(column[6]))
            print()
            print("Allergenprüfung:")
            print()
            print("Folgende Mängel wurden in Ihrem Katalog vom " + str(Katalogdatum) + " festgestellt.")


            a_44 = "Krebstiere und daraus gewonnen Erzeugnisse (AC)"
            a_45 = "Eier und daraus gewonnene Erzeugnisse (AE)"
            a_46 = "Fisch oder daraus gewonnene Erzeugnisse (AF)"
            a_47 = "Milch und Milcherzeugnisse (AM)"
            a_48 = "Nüsse und daraus gewonnene Erzeugnisse (AN)"
            a_49 = "Erdnüsse und daraus Erzeugnisse (AP)"
            a_50 = "Sesamsamen und daraus gewonnene Erzeugnisse (AS)"
            a_51 = "Schwefeldioxid und Sulphite (AU)"
            a_52 = "Glutenhaltiges Getreide sowie daraus hergestellte Erzeugnisse (AW)"
            a_53 = "Sojabohnen und daraus gewonnene Erzeugnisse (AY)"
            a_54 = "Sellerie und daraus gewonnene Erzeugnisse (BC)"
            a_55 = "Senf und daraus gewonnene Erzeugnisse (BM)"
            a_56 = "Lupine und daraus gewonnene Erzeugnisse (NL)"
            a_57 = "Weichtiere und daraus gewonnene Erzeugnisse (UM)"

            spitter = ","

            for column in csv_reader:
                if column != []:
                    if column[66] == "1":
                        if (column[68] == "0" or column[68] == "1") and (column[69] == "0" or column[69] == "1") and (column[
                            70] == "0" or column[70] == "1") and (column[71] == "0" or column[71] == "1") and \
                                (column[72] == "0" or column[72] == "1") and (column[73] == "0" or column[73] == "1") and \
                                (column[74] == "0" or column[74] == "1") and (column[75] \
                                == "0" or column[75] == "1") and (column[76] == "0" or column[76] == "1") and (column[77] \
                                == \
                                "0" or column[77] == "1") and (column[78] == "0" or column[78] == "1") and (column[79] ==
                                                            "0" \
                                or column[79] == "1") \
                                and (column[80] == \
                                "0" or column[80] == "1") and (column[81] == "0" or column[81] == "1"):

                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[8])
                            print("Artikelname: " + column[9])
                            print()
                            print("Angabe, ob Allergen enthalten: " + column[66])
                            print("(0 = keine Allergen, 1 = Allergene enthalten)")
                            print()
                            print(a_44 + " : " + column[68])
                            print(a_45 + " : " + column[69])
                            print(a_46 + " : " + column[70])
                            print(a_47 + " : " + column[71])
                            print(a_48 + " : " + column[72])
                            print(a_49 + " : " + column[73])
                            print(a_50 + " : " + column[74])
                            print(a_51 + " : " + column[75])
                            print(a_52 + " : " + column[76])
                            print(a_53 + " : " + column[77])
                            print(a_54 + " : " + column[78])
                            print(a_55 + " : " + column[79])
                            print(a_56 + " : " + column[80])
                            print(a_57 + " : " + column[81])
                            print(" 0 = nicht enthalten, 1 = in Spuren, 2 = enthalten")
                            print()
                            print(
                                "Sie haben angegeben, dass der Artikel Allergene enthält. Jedoch haben Sie Allergene als "
                                "- in Spuren enthalten - oder als - nicht enthalten - angegeben. Prüfen Sie bite, ob Allergene enthalten sind. Nach der LMIV "
                                "Verordnung ist in Spuren enthalten als keine Allergene "
                                "enthalten anzusehen.")

                        elif column[72] == "2" and column[76] == "2":
                            weizen_ent = any(
                                x in column[82].split(spitter) for x in ['A1', "A2", "A3", "A4", "A5", "A6", "A7", "A8"])
                            if weizen_ent == True:
                                nüsse_ent = any(x in column[82].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                                if nüsse_ent == True:
                                    pass
                                else:
                                    print("---------------------------------------------")
                                    print("Artikelnummer: " + column[6])
                                    print("Artikelname: " + column[9])
                                    print("Angegebene Allergene: " + column[82])
                                    print()
                                    print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[72] + "\"!")
                                    print("Angabe, ob Weizen enthalten ist: " + "\"" + column[82] + "\"!")
                                    print()
                                    print("Keine Nuss und keine Weizen Spezifikation angegeben! Bitte geben Sie H1 - H8 & A1 - A8 an.")

                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[8])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[82])
                                print()
                                print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[72] + "\"!")
                                print("Angabe, ob Weizen enthalten ist: " + "\"" + column[82] + "\"!")
                                print()
                                print("Keine Weizen Spezifikation angegeben! Bitte geben Sie A1 - A8 an.")
                                nüsse_ent = any(
                                    x in column[82].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                                if nüsse_ent == True:
                                    print()
                                else:
                                        print(
                                "Außerdem wurde auch keine Spezifikation von Nüssen angegeben! Bitte geben Sie H1 - H8 an.")

                        elif column[52] == "2":
                            weizen_ent = any(x in column[82].split(spitter) for x in ['A1', "A2", "A3", "A4", "A5", "A6", "A7", "A8"])
                            
                            if weizen_ent == True:
                                pass
                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[6])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[82])
                                print()
                                print("Angabe, ob Weizen enthalten ist: " + "\"" + column[82] + "\"!")
                                print()
                                print("Keine Weizen Spezifikation angegeben! Bitte geben Sie A1 - A8 an.")

                        elif column[72] == "2":
                            nüsse_ent = any(x in column[82].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                            if nüsse_ent == True:
                                pass
                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[6])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[82])
                                print()
                                print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[72] + "\"!")
                                print()
                                print("Keine Nuss Spezifikation angegeben! Bitte geben Sie H1 - H8 an.")


                    elif column[66] == "0":
                        if column[68] == "2" or  column[69] == "2"or column[70] == "2" or column[
                            71] == "2" or column[72] == "2" or column[73] == "2" or column[74] == "2" or column[75] == \
                                "2" or column[76] == "2" or column[77] == "2" or column[78] == "2"or column[79] == "2" or\
                                column[80] == "2" or column[81] == "2":
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print()
                            print("Angabe, ob Allergen enthalten: " + column[66])
                            print("(0 = kein Allergen, 1 = Allergene enthalten)")
                            print()
                            print(a_44 + " : " + column[68])
                            print(a_45 + " : " + column[69])
                            print(a_46 + " : " + column[70])
                            print(a_47 + " : " + column[71])
                            print(a_48 + " : " + column[72])
                            print(a_49 + " : " + column[73])
                            print(a_50 + " : " + column[74])
                            print(a_51 + " : " + column[75])
                            print(a_52 + " : " + column[76])
                            print(a_53 + " : " + column[77])
                            print(a_54 + " : " + column[78])
                            print(a_55 + " : " + column[79])
                            print(a_56 + " : " + column[80])
                            print(a_57 + " : " + column[81])
                            print(" 0 = nicht enthalten, 1 = in Spuren, 2 = enthalten")
                            print()
                            print(
                                "Sie haben angegeben, dass der Artikel keine Allergene enthält. Jedoch haben Sie Allergene "
                                "angegeben. Bitte prüfen Sie diesen Artikel, vielen Dank!")

                else:
                    pass




    def Zusatzstoffprüfung():

        with open(p, "r", newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            next(csv_reader)
            for column in csv_reader:
                Firmenname = (column[8])
                break

            print()
            print("Zusatzstoffprüfung:")
            print()
            print("Folgende Mängel wurden beim Ihrem Katalog vom " + Katalogdatum + " festgestellt.")
            print()
            for column in csv_reader:
                if column != []:
                    if column[67] == "1":
                        if column[59] != "":
                            continue
                        else:
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print("")  	    	        
                            print("Zusatzstoffe enthalten?: " + "\"" + column[67] + "\"")
                            print(" 0 = nicht enthalten, 1 = enthalten")
                            print("")
                            print("Folgende Zusatzstoffe wurden angegeben: "+  "\"" + column[59] + "\"")
                            print()
                            print("Sie haben angegeben, dass der Artikel Zusatzstoffe enthält. Allerdings haben Sie keine "
                                "Zusatzstoffe angegeben! Bitte passen Sie den Artikel an.")

                    elif column[67] == "0":
                        if column[59] != "":
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print("")
                            print("Zusatzstoffe enthalten?: " + "\"" + column[67] + "\"")
                            print("(0 = keine Zusatzstoffe, 1 = Zusatzstoffe enthalten)")
                            print()
                            print("Folgende Zusatzstoffe wurden angegeben: " + "\""+ column[59] + "\"")
                            print()
                            print("Sie haben Zusatzstoffe angegeben, obwohl Sie mitgeteilt haben, dass der Artikel keine Zusatzstoffe enthält. Bitte entfernen Sie die Zusatzstoffe oder übergeben uns eine 1.")


                    elif column[67] == "":
                        print("---------------------------------------------")
                        print("Artikelnummer: " + column[6])
                        print("Artikelname: " + column[9])
                        print("Folgende Zusatzstoffe wurden angegeben: " + "\"" + column[67] + "\"")
                        print()
                        print("Bitte füllen Sie das Feld für die Angabe, ob der Artikel Zusatzstoffe enthält. 0 für keine Zusazstoffe und eine 1 für enthält Zusatzstoffe. Vielen Dank")
                else:
                    pass
    PrüfungAllergene = Allergenprüfung()
    Prüfung_Zusatzstoffe = Zusatzstoffprüfung()

datum_now = datetime.now().strftime('%d.%m.%Y')

# Output Pfad für die Prüfung
o = "C:\\Users\\Maximilian.Rasch\\Desktop\\Kataloge_Rechnungen\\Kataloge\\" + "Prüfung_Allergene_Zusatzstoffe_" + str(Firmenname) + "_" + str(datum_now)\
    + ".txt"


import sys

class StdoutRedirection:
    """Standard output redirection context manager"""

    def __init__(self, path):
        self._path = path

    def __enter__(self):
        sys.stdout = open(self._path, mode="w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = sys.__stdout__

with StdoutRedirection(o):
    Allergenprüfung()
    Zusatzstoffprüfung()
