def load_data(file):
    f = open(file + ".dat", "r")
    return f

def save_data(file):
    f = open(file + ".dat", "w")
    return f

def konfig():

    konf: bool = True

    while konf:
        print("--- Einstellungen ---")
        print("Was möchten Sie Anpassen?")
        print("[1] - Login Zeit")
        print("[2] - Logout Zeit")
        print("[3] - HO/VO Tage")
        print("[4] - Login Daten")
        print("[0] - Zurück\n")

        eingabe: int = int(input("-> "))

        match eingabe:
            case 1:
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
                f = load_data("day")
                print("HO = Home Office")
                print("VO = Vor Ort")
                print("F = Frei")
                print("Aktuelle Konfiguration:")
                print("Montag: " + f.readline())
                print("Dienstag: " + f.readline())
                print("Dienstag: " + f.readline())
                print("Mittwoch: " + f.readline())
                print("Freitag: " + f.readline())
                print("Samstag: " + f.readline())
                print("Sonntag: " + f.readline() + "\n")
                f.close()

                f = save_data("day")
                print("Gib nun die neuen Werte ein:")
                mo: str = input("Montag: ")
                di: str = input("Dienstag: ")
                mi: str = input("Mittwoch: ")
                do: str = input("Donnerstag: ")
                fr: str = input("Freitag: ")
                sa: str = input("Samstag: ")
                so: str = input("Sonntag: ")
                f.write(mo + "\n" + di + "\n" + mi + "\n" + do + "\n" + fr + "\n" + sa + "\n" + so)
                f.close()

            case 4:
                f = load_data("data")
                print("Aktuelle Konfiguration:")
                print("Username: " + f.readline())
                print("Passwort: " + "******" + "\n")
                f.close()

                f = save_data("data")
                print("Gib nun die neuen Werte ein:")
                username: str = input("Username: ")
                password: str = input("Password: ")
                
                print("Welcher Browser soll genutzt werden? [Standard: Edge]")
                print("[1] Edge")
                print("[2] Firefox")
                print("[3] Chrome")
                print("[4] Safari")
                int_browser: int = int(input("-> "))
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
            case _:
                konf = False