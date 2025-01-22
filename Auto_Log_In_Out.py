from Log import log
from data import get_browser

def login_func():
    login: bool = False

    if input("Wurde die Zeiterfassung bereits gestartet? - [y] = ja\n") == "y":
        login = True
    else:
        login = False

    while True:
        if login:
            f = open("t_out.dat", "r")
            out_h = int(f.readline())
            out_m = int(f.readline())
            out_s = int(f.readline())
            f.close()

            login = log(out_h, out_m, out_s, login, get_browser())
        elif not login:
            f = open("t_in.dat", "r")
            in_h: int = int(f.readline())
            in_m: int = int(f.readline())
            in_s: int = int(f.readline())
            f.close()

            login = log(in_h, in_m, in_s, login, get_browser())
        else:
            pass # Fehlermeldung Hinzufügen
