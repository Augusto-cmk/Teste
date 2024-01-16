import sys
import os
import readchar


class Menu:
    def __init__(self):
        self.fluxo = {
            1: self.__crash_by_id,
            2: self.__crash,
            3: self.__bug,
            4: self.__crash_manual,
            5: self.__crash_ios_pf_auto,
            6: self.__exit
        }
        self.options = [
            "Resolver crash pelo ID",
            "Resolver crash TOP 50",
            "Resolver um bug",
            "Resolver um crash manual",
            "Resolver crashes IOS PF automático",
            "Sair"
        ]
        self.selected_option = 0
        self.main()

    def menu(self):
        os.system("clear")
        print("""
        ██████╗  ███████╗  ██╗
        ██╔══██╗ ██╔════╝  ██║
        ██████╔╝ ███████╗  ██║
        ██╔══██╗      ██║  ██║
        ██████╔╝ ███████║  ██║
        ╚═════╝  ╚══════╝  ╚═╝
            """,end=" ")
        print("""
                                          ██║
                                        ██║
            ██║ ╔████████╗  █████╗   ██╗   ██╗
            ██║ ╚═══██╔══╝ ██╔══██╗  ██║   ██║
            ██║     ██║    ███████║  ██║   ██║
            ██║     ██║    ██║  ██║  ██║   ██║
            ██║     ██║    ██║  ██║   ██████╔╝
            ╚═╝     ╚═╝    ╚═╝  ╚═╝   ╚═════╝ 
            """)
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                print(f"\033[1;37;42m[*] {option}\033[m")
            else:
                print(f"[ ] {option}")

    def main(self):
        while True:
            self.menu()
            key = readchar.readchar()
            if key == "w":
                self.selected_option = (self.selected_option - 1) % len(self.options)
            if key == "s":
                self.selected_option = (self.selected_option + 1) % len(self.options)
            if key == "\n":
                self.fluxo[self.selected_option + 1]()

    def __crash_by_id(self):
        os.system("clear")
        print("Executando Resolver crash pelo ID")
        input("Any -> Voltar ao menu principal")

    def __crash(self):
        os.system("clear")
        print("Executando Resolver crash TOP 50")
        input("Any -> Voltar ao menu principal")

    def __bug(self):
        os.system("clear")
        print("Executando Resolver um bug")
        input("Any -> Voltar ao menu principal")

    def __crash_manual(self):
        os.system("clear")
        print("Executando Resolver um crash manual")
        input("Any -> Voltar ao menu principal")

    def __crash_ios_pf_auto(self):
        os.system("clear")
        print("Executando Resolver crashes IOS PF automático")
        input("Any -> Voltar ao menu principal")

    def __exit(self):
        print("Saindo do programa...")
        sys.exit(0)


Menu()
