from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from Day import day, get_day_name
from data import get_login, get_browser
import os, keyboard


def remove(string) -> str:
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


def log_pre(username, password, bw):
    # Auswahl des zu nutzenden Browsers
    # bw = Browser auswahl

    match bw:
        case "Chrome":
            browser = webdriver.Chrome()
        case "Firefox":
            browser = webdriver.Firefox()
        case "Edge":
            browser = webdriver.Edge()
        case "Safari":
            browser = webdriver.Safari()
        case _:
            browser = webdriver.Edge()
            print("Fehler bei Eingabe, deshalb wird 'Edge' benutzt")

    # Webseite öffnen
    browser.get("https://lernplattform.gfn.de/login/index.php")
    sleep(1)
    # Username-Box finden und Nutzernamen einfügen
    username_box = browser.find_element("id", "username")
    username_box.send_keys(username)
    sleep(1)
    # Passwort-Box finden und Passwort einfügen
    password_box = browser.find_element("id", "password")
    password_box.send_keys(password)
    sleep(1)
    # Login Button finden
    login_button = browser.find_element("id", "loginbtn")
    # Betätigen des Login Button
    login_button.click()
    sleep(1)
    return browser


def logout(browser):
    # End zeiterfassung
    browser.get("https://lernplattform.gfn.de/?stoppen=1")
    sleep(2)
    # Browser schließen
    browser.close()


def login(browser):
    try:
        try:
            if WebDriverWait(browser, 5).until(EC.alert_is_present()):
                # switch_to.alert for switching to alert and accept
                # Alert(browser).accept()
                alert = browser.switch_to.alert
                alert.accept()
                # print("alert Exists in page")
        except TimeoutException:
            # print("alert does not Exist in page")
            pass

        if remove(day()) == "HO":
            # Homeoffice - Radiobutton finden und auswählen
            radio_button = browser.find_element("id", "flexRadioDefault1")
            radio_button.click()
        elif remove(day()) == "VO":
            # Standort - Radiobutton finden und auswählen
            radio_button = browser.find_element("id", "flexRadioDefault2")
            radio_button.click()
        sleep(1)

        # Start zeiterfassung
        start_button = browser.find_element("css selector", "input[value='Starten']")
        start_button.click()

        browser.get("https://lernplattform.gfn.de/?starten=1")
        sleep(2)
        # Browser schließen
        browser.close()
    except Exception as e:
        os.system("cls")
        browser.close()


# Auto Log In Out
def log(h_log, m_log, s_log, login_status, bw):
    current_time = datetime.now()
    h: int = int(current_time.strftime("%H"))
    m: int = int(current_time.strftime("%M"))
    # s: int = int(current_time.strftime("%S"))

    if login_status:
        status: str = "Beenden"
    elif not login_status:
        status: str = "Starten"
    else:
        status: str = "Fehler"

    day_name: str = get_day_name()

    match remove(day()):
        case "HO":
            einloggen_als: str = "Home Office"
        case "VO":
            einloggen_als: str = "Vor Ort"
        case "F":
            einloggen_als: str = "Wird übersprungen"
        case _:
            einloggen_als: str = "Fehler"

    # Menü Schleife
    while m != m_log or h != h_log:
        sleep(1)
        os.system("cls")
        print("Zeiterfassungsstatus:\n" + status + "\n")
        print("Ausgewählter Browser:\n" + bw + "\n")
        print("Aktueller Tag:\n" + day_name + "\n")
        print("Zeiterfassung starten als:\n" + einloggen_als + "\n")
        print(status + " um:")
        print(str(h_log) + ":" + str(m_log) + ":" + str(s_log))
        current_time = datetime.now()
        str_time = current_time.strftime("%H:%M:%S")
        h: int = int(current_time.strftime("%H"))
        m: int = int(current_time.strftime("%M"))
        # s: int = int(current_time.strftime("%S"))
        print("\nAktuelle Zeit:")
        print(str_time)

        if keyboard.is_pressed("esc"):
            print(
                "\nAutomatische Zeiterfassung beendet, drücke [ENTER] um zurück ins Menü zu kommen."
            )
            return "Exit"

        # Aktualisierung bei Tagesänderung
        if m == 0 or h == 0:
            sleep(60)
            return login_status

    # Einloggen/Ausloggen, wenn Tag nicht "Frei" ist
    if remove(day()) != "F":
        data = get_login()
        bw = get_browser()

        if (
            login_status
            and h_log >= int(current_time.strftime("%H"))
            and m_log >= int(current_time.strftime("%M"))
        ):
            logout(log_pre(data[0], data[1], bw))
            sleep(60)
            return False
        elif (
            not login_status
            and h_log >= int(current_time.strftime("%H"))
            and m_log >= int(current_time.strftime("%M"))
        ):
            login(log_pre(data[0], data[1], bw))
            sleep(60)
            return True
        else:
            pass  # Fehlermeldung Hinzufügen
    else:
        return login_status
    return login_status
