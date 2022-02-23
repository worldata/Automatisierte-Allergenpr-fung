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

    next(csv_reader)
    for column in csv_reader:
        Firmenname = (column[8])
        break

    def linefinder(x):
        
        for column in csv_reader:
            if column[6] == str(x):
                print("Lieferantenname: " + Firmenname)
                print()
                print("Artikel: " + column[9])
                print("Artikelnummer: " + column[6])
                print("Bestelleinheit: " + column[14])
                print("Preis der Bestelleinheit: " + column[20])
                print("Fixe Bestellmenge: " + column[31])
                print("Gewichtsartikelflag: " + column[18])
                print()
                print("Eine Packung enthält " + column[35] + " " + column[34] + ".")

    def artikel_suchen(x):

        for column in csv_reader:
            if column[6] == str(x):
                print("Artikelnummer = " + column[6])
                print("Artikelname = " + column[9])
                print(column)
                print(column[52])

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

            next(csv_reader)
            for column in csv_reader:
                Firmenname = (column[8])
                break

            print("Lieferantenname: " + Firmenname)
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
                    if column[42] == "1":
                        if (column[44] == "0" or column[44] == "1") and (column[45] == "0" or column[45] == "1") and (column[
                            46] == "0" or column[46] == "1") and (column[47] == "0" or column[47] == "1") and \
                                (column[48] == "0" or column[48] == "1") and (column[49] == "0" or column[49] == "1") and \
                                (column[50] == "0" or column[50] == "1") and (column[51] \
                                == "0" or column[51] == "1") and (column[52] == "0" or column[52] == "1") and (column[53] \
                                == \
                                "0" or column[53] == "1") and (column[54] == "0" or column[54] == "1") and (column[55] ==
                                                            "0" \
                                or column[55] == "1") \
                                and (column[56] == \
                                "0" or column[56] == "1") and (column[57] == "0" or column[57] == "1"):

                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print()
                            print("Angabe, ob Allergen enthalten: " + column[42])
                            print("(0 = keine Allergen, 1 = Allergene enthalten)")
                            print()
                            print(a_44 + " : " + column[44])
                            print(a_45 + " : " + column[45])
                            print(a_46 + " : " + column[46])
                            print(a_47 + " : " + column[47])
                            print(a_48 + " : " + column[48])
                            print(a_49 + " : " + column[49])
                            print(a_50 + " : " + column[50])
                            print(a_51 + " : " + column[51])
                            print(a_52 + " : " + column[52])
                            print(a_53 + " : " + column[53])
                            print(a_54 + " : " + column[54])
                            print(a_55 + " : " + column[55])
                            print(a_56 + " : " + column[56])
                            print(a_57 + " : " + column[57])
                            print(" 0 = nicht enthalten, 1 = in Spuren, 2 = enthalten")
                            print()
                            print(
                                "Sie haben angegeben, dass der Artikel Allergene enthält. Jedoch haben Sie Allergene als "
                                "- in Spuren enthalten - oder als - nicht enthalten - angegeben. Prüfen Sie bite, ob Allergene enthalten sind. Nach der LMIV "
                                "Verordnung ist in Spuren enthalten als keine Allergene "
                                "enthalten anzusehen.")

                        elif column[48] == "2" and column[52] == "2":
                            weizen_ent = any(
                                x in column[58].split(spitter) for x in ['A1', "A2", "A3", "A4", "A5", "A6", "A7", "A8"])
                            if weizen_ent == True:
                                nüsse_ent = any(x in column[58].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                                if nüsse_ent == True:
                                    pass
                                else:
                                    print("---------------------------------------------")
                                    print("Artikelnummer: " + column[6])
                                    print("Artikelname: " + column[9])
                                    print("Angegebene Allergene: " + column[58])
                                    print()
                                    print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[48] + "\"!")
                                    print("Angabe, ob Weizen enthalten ist: " + "\"" + column[52] + "\"!")
                                    print()
                                    print("Keine Nuss und keine Weizen Spezifikation angegeben! Bitte geben Sie H1 - H8 & A1 - A8 an.")

                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[6])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[58])
                                print()
                                print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[48] + "\"!")
                                print("Angabe, ob Weizen enthalten ist: " + "\"" + column[52] + "\"!")
                                print()
                                print("Keine Weizen Spezifikation angegeben! Bitte geben Sie A1 - A8 an.")
                                nüsse_ent = any(
                                    x in column[58].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                                if nüsse_ent == True:
                                    print()
                                else:
                                        print(
                                "Außerdem wurde auch keine Spezifikation von Nüssen angegeben! Bitte geben Sie H1 - H8 an.")

                        elif column[52] == "2":
                            weizen_ent = any(x in column[58].split(spitter) for x in ['A1', "A2", "A3", "A4", "A5", "A6", "A7", "A8"])
                            
                            if weizen_ent == True:
                                pass
                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[6])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[58])
                                print()
                                print("Angabe, ob Weizen enthalten ist: " + "\"" + column[52] + "\"!")
                                print()
                                print("Keine Weizen Spezifikation angegeben! Bitte geben Sie A1 - A8 an.")

                        elif column[48] == "2":
                            nüsse_ent = any(x in column[58].split(spitter) for x in ['H1', "H2", "H3", "H4", "H5", "H6", "H7", "H8"])
                            if nüsse_ent == True:
                                pass
                            else:
                                print("---------------------------------------------")
                                print("Artikelnummer: " + column[6])
                                print("Artikelname: " + column[9])
                                print("Angegebene Allergene: " + column[58])
                                print()
                                print("Angabe, ob Nüsse enthalten ist: " + "\"" + column[48] + "\"!")
                                print()
                                print("Keine Nuss Spezifikation angegeben! Bitte geben Sie H1 - H8 an.")


                    elif column[42] == "0":
                        if column[44] == "2" or  column[45] == "2"or column[46] == "2" or column[
                            47] == "2" or column[48] == "2" or column[49] == "2" or column[50] == "2" or column[51] == \
                                "2" or column[52] == "2" or column[53] == "2" or column[54] == "2"or column[55] == "2" or\
                                column[56] == "2" or column[57] == "2":
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print()
                            print("Angabe, ob Allergen enthalten: " + column[42])
                            print("(0 = kein Allergen, 1 = Allergene enthalten)")
                            print()
                            print(a_44 + " : " + column[44])
                            print(a_45 + " : " + column[45])
                            print(a_46 + " : " + column[46])
                            print(a_47 + " : " + column[47])
                            print(a_48 + " : " + column[48])
                            print(a_49 + " : " + column[49])
                            print(a_50 + " : " + column[50])
                            print(a_51 + " : " + column[51])
                            print(a_52 + " : " + column[52])
                            print(a_53 + " : " + column[53])
                            print(a_54 + " : " + column[54])
                            print(a_55 + " : " + column[55])
                            print(a_56 + " : " + column[56])
                            print(a_57 + " : " + column[57])
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
                    if column[43] == "1":
                        if column[59] != "":
                            continue
                        else:
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print("")  	    	        
                            print("Zusatzstoffe enthalten?: " + "\"" + column[43] + "\"")
                            print(" 0 = nicht enthalten, 1 = enthalten")
                            print("")
                            print("Folgende Zusatzstoffe wurden angegeben: "+  "\"" + column[59] + "\"")
                            print()
                            print("Sie haben angegeben, dass der Artikel Zusatzstoffe enthält. Allerdings haben Sie keine "
                                "Zusatzstoffe angegeben! Bitte passen Sie den Artikel an.")

                    elif column[43] == "0":
                        if column[59] != "":
                            print("---------------------------------------------")
                            print("Artikelnummer: " + column[6])
                            print("Artikelname: " + column[9])
                            print("")
                            print("Zusatzstoffe enthalten?: " + "\"" + column[43] + "\"")
                            print("(0 = keine Zusatzstoffe, 1 = Zusatzstoffe enthalten)")
                            print()
                            print("Folgende Zusatzstoffe wurden angegeben: " + "\""+ column[59] + "\"")
                            print()
                            print("Sie haben Zusatzstoffe angegeben, obwohl Sie mitgeteilt haben, dass der Artikel keine Zusatzstoffe enthält. Bitte entfernen Sie die Zusatzstoffe oder übergeben uns eine 1.")


                    elif column[43] == "":
                        print("---------------------------------------------")
                        print("Artikelnummer: " + column[6])
                        print("Artikelname: " + column[9])
                        print("Folgende Zusatzstoffe wurden angegeben: " + "\"" + column[43] + "\"")
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
