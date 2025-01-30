from genericpath import isfile
import os

def check_files():
    if not os.path.isfile("data.dat"):
        with open("data.dat", "w") as f:
            f.write("[SETTINGS]\n[LOGIN]\nLogin-Name\nPassword\n\n[BROWSER]\nEdge")

    if not os.path.isfile("day.dat"):
        with open("day.dat", "w") as f:
            f.write("VO\nVO\nVO\nVO\nHO\nF\nF")

    if not os.path.isfile("t_in.dat"):
        with open("t_in.dat", "w") as f:
            f.write("8\n10\n0")

    if not os.path.isfile("t_out.dat"):
        with open("t_out.dat", "w") as f:
            f.write("16\n35\n0")