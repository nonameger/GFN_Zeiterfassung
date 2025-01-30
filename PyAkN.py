import keyboard, os
from time import sleep

def __c_menu(selection: int, menu: int, titel: str, menu_titels):

    if menu != len(menu_titels):
        print(f"Given Menu: {menu}")
        print(f"Given Titels: {len(menu_titels)}")
        return print("Error, menu and titles need the same number")

    m = {}
    
    for i in range(menu):
        m[f"m{i}"] = "[ ]"
    

    for i in range(menu):
        if i == selection:
            m[f"m{i}"] = "[x]"


    os.system('cls')

    print(titel)
    for i in range(menu):
        print(m[f"m{i}"] + menu_titels[i])

    sleep(0.1)

def PyAkN(menu_selection:int, menu:int,titel:str, menu_titels: str):
    __c_menu(menu_selection, menu, titel, menu_titels)
    while True:


        if keyboard.is_pressed("down"):

            if menu_selection == menu - 1:
                menu_selection = 0
            else:
                menu_selection = menu_selection + 1

            __c_menu(menu_selection, menu, titel, menu_titels)

        if keyboard.is_pressed("up"):
        
            if menu_selection == 0:
                menu_selection = menu - 1
            else:
                menu_selection = menu_selection - 1
    
            __c_menu(menu_selection, menu, titel, menu_titels)

        if keyboard.is_pressed("esc"):
            return 0

        if keyboard.is_pressed("enter"):
            return menu_selection + 1
