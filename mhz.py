import sys
import colorama
from colorama import Fore
import socket
import os

class MHZ:
    colorama.init(autoreset=True)
    g = Fore.LIGHTGREEN_EX
    r = Fore.LIGHTRED_EX
    y = Fore.LIGHTYELLOW_EX
    b = Fore.LIGHTBLUE_EX
    p = Fore.LIGHTMAGENTA_EX
    reset = Fore.RESET

    _hostname_ = socket.gethostname().lower()

    _info_ = "[" + g + "INFO" + reset + "]"
    _error_ = "[" + r + "Error" + reset + "]"
    _sugg_ = "[" + b + "*" + reset + "]"

    def Logo(self=0, g=g, r=r):
        print(g + """
███╗   ███╗██╗  ██╗███████╗    ███████╗██████╗  ██████╗ 
████╗ ████║██║  ██║╚══███╔╝    ██╔════╝██╔══██╗██╔═══██╗
██╔████╔██║███████║  ███╔╝     █████╗  ██████╔╝██║   ██║
██║╚██╔╝██║██╔══██║ ███╔╝      ██╔══╝  ██╔══██╗██║▄▄ ██║
██║ ╚═╝ ██║██║  ██║███████╗    ██║     ██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚══▀▀═╝  """)
        print(r + "─" * 50)

    def Input(self=0, g=g, reset=reset, y=y, r=r, b=b, _hostname_=_hostname_, p=p):
        _root_ = g + "┌" + g + "[" + r + f"mhz@{_hostname_}" + g + "]" + b + "~" + g + "[" + p + "menu" + g + "]" + reset

        print(f"   [{g + '1' + reset}] {y + 'Per vedere tutte le frequenze disponibili (Mhz)'}")
        print(f"   [{g + '2' + reset}] {y + 'Per Ricevere frequenze (Mhz)'}")
        print(f"   [{g + '3' + reset}] {y + 'Per Trasmettere frequenze (Mhz)'}")
        print(f"   [{g + '4' + reset}] {y + 'Per vedere la documentazione'}")
        print(f"   [{g + 'E' + reset}] {y + 'Per uscire'}")

        while True:
            print("")
            print(_root_)
            root = input(g + "└──> " + reset)

            if root == "1":
                print("   ")

            elif root == "E" or root == "e":
                sys.exit()


if __name__ == "__main__":
    os.system("cls")
    MHZ.Logo()
    MHZ.Input()

#print(g + "┌")
#print(g + "└──")

