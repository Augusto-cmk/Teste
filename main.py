import os
import keyboard
import sys

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
        os.system("cls")
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
            key = keyboard.read_event(suppress=True)
            if key.event_type == keyboard.KEY_DOWN:
                if key.name == "up":
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif key.name == "down":
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif key.name == "enter":
                    self.fluxo[self.selected_option + 1]()
                    input("Pressione Enter para voltar ao menu principal...")
                    os.system("cls")

    def __crash_by_id(self):
        os.system("cls")
        print("Executando Resolver crash pelo ID")

    def __crash(self):
        os.system("cls")
        print("Executando Resolver crash TOP 50")

    def __bug(self):
        os.system("cls")
        print("Executando Resolver um bug")

    def __crash_manual(self):
        os.system("cls")
        print("Executando Resolver um crash manual")

    def __crash_ios_pf_auto(self):
        os.system("cls")
        print("Executando Resolver crashes IOS PF automático")

    def __exit(self):
        os.system("cls")
        print("Saindo do programa...")
        sys.exit(0)
Menu()