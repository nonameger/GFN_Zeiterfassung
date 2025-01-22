import twill.commands, os
from twill.commands import *
from data import get_login

def anwesenheit_funktion() -> str:
    go("https://lernplattform.gfn.de/login/index.php")

    data = get_login()

    formclear("1")
    fv("1", "username", data[0])
    fv("1", "password", data[1])

    submit("loginbtn")

    go("https://lernplattform.gfn.de/local/anmeldung/anwesenheit.php")
    Browser_url = twill.commands.browser.html

    temp = "temp.dat"

    f = open(temp, "w", encoding="utf-8")
    f.write(Browser_url)
    f.close()


    HO = 0
    VO = 0

    f = open(temp, "r", encoding="utf-8")
    for line in f:
        if "🏠" in line:
            HO = HO + 1
        elif "🏢" in line:
            VO = VO + 1
    f.close()

    os.system('cls')

    os.remove(temp)
    if HO == 0 or VO == 0:
        print(" -!- Keine Daten gefunden -!- ")
        print(" -!- Fehler beim Login? -!- ")
        print(" -!- Überpüfe deine Login-Informationen. -!- \n")
        return ("0", "0", "0", "0")
    else:
        sHO = (HO * 100) / (HO + VO)
        sVO = (VO * 100) / (HO + VO)

    return (str(HO), str(VO), str(round(sHO,2)), str(round(sVO,2)))


def aus():
    erg = anwesenheit_funktion()

    print("--- Anwesendheit ---")
    print("Home Office: \t" + erg[0] + " Tage")
    print(erg[2] + "%\n")
    print("Vor Ort: \t" + erg[1] + " Tage")
    print(erg[3] + "%\n")

    input("Press Enter..")