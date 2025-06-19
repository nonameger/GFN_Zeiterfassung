import os
from PyAkN import PyAkN

def load_data(file):
    f = open(file + ".dat", "r")
    return f

def save_data(file):
    f = open(file + ".dat", "w")
    return f

def konfig():

    while True:
        os.system('cls')

        eingabe = int(PyAkN(0, 5, "--- Einstellungen ---", ["Zeiterfassung Starten - Zeit", "Zeiterfassung Beenden - Zeit", "HO/VO Tage", "Login + Browser Daten", "Zurück"]))
        os.system('cls')

        match eingabe:
            case 1:
                os.system('cls')

                f = load_data("t_in")
                print("Aktuelle Konfiguration:")
                print("Stunde: " + f.readline())
                print("Minute: " + f.readline())
                print("Sekunde: " + f.readline() + "\n")
                f.close()

                f = save_data("t_in")
                print("Gib nun die neuen Werte ein:")
                h: str = input("Stunde: ")
                m: str = input("Minute: ")
                s: str = input("Sekunde: ")
                f.write(h + "\n" + m + "\n" + s)
                f.close()

            case 2:
                os.system('cls')

                f = load_data("t_out")
                print("Aktuelle Konfiguration:")
                print("Stunde: " + f.readline())
                print("Minute: " + f.readline())
                print("Sekunde: " + f.readline() + "\n")
                f.close()

                f = save_data("t_out")
                print("Gib nun die neuen Werte ein:")
                h: str = input("Stunde: ")
                m: str = input("Minute: ")
                s: str = input("Sekunde: ")
                f.write(h + "\n" + m + "\n" + s)
                f.close()

            case 3:
                os.system('cls')

                f = load_data("day")
                mo, di, mi, do, fr, sa, so = f.readline(),f.readline(),f.readline(),f.readline(),f.readline(),f.readline(),f.readline() + "\n"
                f.close()

                f = save_data("day")
                list_days = [mo, di, mi, do, fr, sa, so]
                counter = 0
                list_day_names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
                for day in list_days:

                    int_day = int(PyAkN(0, 3, f"Aktueller Wert für den Tag ({list_day_names[counter]}): {day}\nAuswahl des Tages: {list_day_names[counter]}", ["Vor Ort", "Home Office", "Frei"]))
                    match int_day:
                        case 1:
                            list_days[counter] = "VO"
                        case 2:
                            list_days[counter] = "HO"
                        case 3:
                            list_days[counter] = "F"
                        case _:
                            pass
                    counter += 1

                mo = list_days[0]
                di = list_days[1]
                mi = list_days[2]
                do = list_days[3]
                fr = list_days[4]
                sa = list_days[5]
                so = list_days[6]
                
                f.write(mo.upper() + "\n" + di.upper() + "\n" + mi.upper() + "\n" + do.upper() + "\n" + fr.upper() + "\n" + sa.upper() + "\n" + so.upper())
                f.close()

            case 4:
                os.system('cls')

                f = save_data("data")
                print("Gib nun die neuen Werte ein:")
                username: str = input("Username: ")
                password: str = input("Password: ")
                
                int_browser = int(PyAkN(0, 4, "Welcher Browser soll genutzt werden? [Standard: Edge]", ["Edge", "Firefox", "Chrome", "Safari"]))
                browser = "Edge"
                match int_browser:
                    case 1:
                        browser = "Edge"
                    case 2:
                        browser = "Firefox"
                    case 3:
                        browser = "Chrome"
                    case 4:
                        browser = "Safari"
                    case _:
                        pass

                f.write("[SETTINGS]\n" + "[LOGIN]\n" + username + "\n" + password + "\n\n" + "[BROWSER]\n" + browser)
                f.close()
                
                input("Press 'Enter' key to continue")
            case _:
                break;

        os.system('cls')