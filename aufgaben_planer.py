# Aufgaben-Planer: Ein erweitertes Tool zur Verwaltung von Aufgaben

# Erstellt von Elahe als Lernprojekt



def menue_anzeigen():

    print("\n--- MEIN AUFGABEN-PLANER ---")

    print("1. Neue Aufgabe hinzufügen")

    print("2. Alle Aufgaben anzeigen")

    print("3. Eine Aufgabe löschen") # Ghabeliyat-e jadid

    print("4. Programm beenden")



def hauptprogramm():

    while True:

        menue_anzeigen()

        auswahl = input("Bitte wählen Sie eine Option (1-4): ")



        if auswahl == '1':

            aufgabe = input("Was möchten Sie erledigen? ")

            with open("aufgaben_liste.txt", "a", encoding="utf-8") as datei:

                datei.write(aufgabe + "\n")

            print("Erfolg: Die Aufgabe wurde gespeichert!")

        

        elif auswahl == '2':

            print("\nIhre aktuellen Aufgaben:")

            try:

                with open("aufgaben_liste.txt", "r", encoding="utf-8") as datei:

                    inhalt = datei.readlines()

                    if not inhalt:

                        print("Die Liste ist momentan leer.")

                    else:

                        for index, zeile in enumerate(inhalt, start=1):

                            print(f"{index}. {zeile.strip()}")

            except FileNotFoundError:

                print("Hinweis: Es wurde noch keine Aufgabenliste erstellt.")

        

        elif auswahl == '3':

            # Bakhsh-e hazf kardan

            try:

                with open("aufgaben_liste.txt", "r", encoding="utf-8") as datei:

                    inhalt = datei.readlines()

                

                if not inhalt:

                    print("Keine Aufgaben zum Löschen vorhanden.")

                    continue



                for index, zeile in enumerate(inhalt, start=1):

                    print(f"{index}. {zeile.strip()}")

                

                nummer = int(input("Welche Nummer möchten Sie löschen? "))

                if 1 <= nummer <= len(inhalt):

                    del inhalt[nummer - 1]

                    with open("aufgaben_liste.txt", "w", encoding="utf-8") as datei:

                        datei.writelines(inhalt)

                    print("Aufgabe erfolgreich gelöscht!")

                else:

                    print("Ungültige Nummer.")

            except (FileNotFoundError, ValueError):

                print("Fehler beim Löschen.")



        elif auswahl == '4':

            print("Programm wird beendet. Auf Wiedersehen!")

            break

        else:

            print("Fehler: Ungültige Eingabe.")



if __name__ == "__main__":

    hauptprogramm()