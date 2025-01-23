from Auto_Log_In_Out import login_func
from Anwesenheit import aus
from Manuel_Login import m_login
from Manuel_Logout import m_logout
from konfigurieren import konfig
import os

def menu():
    exit = False

    while exit == False:
        os.system("cls")
        print("--- GFN Zeiterfassung ---")
        print("Was wollen Sie tun?")
        print("[1] Automatische Zeiterfassung")
        print("[2] Anwesenheit")
        print("[3] Zeiterfassung starten")
        print("[4] Zeiterfassung beenden")
        print("[5] Einstellungen")
        print("[0] Beenden\n")

        auswahl: int = int(input("-> "))

        match auswahl:
            case 0:
                exit = True
            case 1:
                os.system("cls")
                login_func()
            case 2:
                os.system("cls")
                aus()
            case 3:
                os.system("cls")
                m_login()
            case 4:
                os.system("cls")
                m_logout()
            case 5:
                os.system("cls")
                konfig()