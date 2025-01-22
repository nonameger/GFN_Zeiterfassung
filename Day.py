import datetime

def day() -> str:
    weekday = datetime.datetime.today().weekday()

    f = open("day.dat", "r")
    montag: str = f.readline()
    dienstag: str = f.readline()
    mittwoch: str = f.readline()
    donnerstag: str = f.readline()
    freitag: str = f.readline()
    samstag: str = f.readline()
    sonntag: str = f.readline()
    f.close()

    match weekday:
        case 0:
            return montag
        case 1:
            return dienstag
        case 2:
            return mittwoch
        case 3:
            return donnerstag
        case 4:
            return freitag
        case 5:
            return samstag
        case 6:
            return sonntag
        case _:
            return "Error"

def get_day_name() -> str:
    weekday = datetime.datetime.today().weekday()

    match weekday:
        case 0:
            return "Montag"
        case 1:
            return "Dienstag"
        case 2:
            return "Mittwoch"
        case 3:
            return "Donnerstag"
        case 4:
            return "Freitag"
        case 5:
            return "Samstag"
        case 6:
            return "Sonntag"
        case _:
            return "Error"