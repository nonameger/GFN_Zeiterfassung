from Auto_Log_In_Out import login_func
from Anwesenheit import aus
from Manuel_Login import m_login
from Manuel_Logout import m_logout
from konfigurieren import konfig
from PyAkN import PyAkN
import os

def menu():

    while True:

        auswahl = int(PyAkN(0, 6, "--- GFN Zeiterfassung ---", ["Automatische Zeiterfassung", "Anwesenheit", "Zeiterfassung starten", "Zeiterfassung beenden", "Einstellungen", "Beenden"]))

        match auswahl:
            case 0:
                break;
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
            case _:
                break;
