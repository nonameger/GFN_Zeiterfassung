def remove(string) -> str:
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


def get_login():
    username: str = "Error"
    password: str = "Error"
    f = open("data.dat", "r", encoding="utf-8")
    while f.readline():
        if remove(f.readline()) == "[LOGIN]":
            username = remove(f.readline())
            password = remove(f.readline())

    f.close()
    return str(username), str(password)

def get_browser():
    browser: str = "Error"
    f = open("data.dat", "r", encoding="utf-8")
    while f.readline():
        if remove(f.readline()) == "[BROWSER]":
            browser = remove(f.readline())

    f.close()
    return str(browser)

