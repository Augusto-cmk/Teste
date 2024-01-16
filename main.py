import termcolor
import sys
import tty
import termios

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
        print(termcolor.colored("""
        ██████╗  ███████╗  ██╗
        ██╔══██╗ ██╔════╝  ██║
        ██████╔╝ ███████╗  ██║
        ██╔══██╗      ██║  ██║
        ██████╔╝ ███████║  ██║
        ╚═════╝  ╚══════╝  ╚═╝
            """, "green"), end=" ")
        print(termcolor.colored("""
                                          ██║
                                        ██║
            ██║ ╔████████╗  █████╗   ██╗   ██╗
            ██║ ╚═══██╔══╝ ██╔══██╗  ██║   ██║
            ██║     ██║    ███████║  ██║   ██║
            ██║     ██║    ██║  ██║  ██║   ██║
            ██║     ██║    ██║  ██║   ██████╔╝
            ╚═╝     ╚═╝    ╚═╝  ╚═╝   ╚═════╝ 
            """, "green"))

        for i, option in enumerate(self.options):
            if i == self.selected_option:
                print(termcolor.colored(f"[*] {option}", "white", "on_green"))
            else:
                print(f"[ ] {option}")

    def main(self):
        while True:
            self.menu()
            key = self.get_key()
            if key == "up":
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif key == "down":
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif key == "enter":
                self.fluxo[self.selected_option + 1]()
                input("Pressione Enter para voltar ao menu principal...")

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def __crash_by_id(self):
        print("Executando Resolver crash pelo ID")

    def __crash(self):
        print("Executando Resolver crash TOP 50")

    def __bug(self):
        print("Executando Resolver um bug")

    def __crash_manual(self):
        print("Executando Resolver um crash manual")

    def __crash_ios_pf_auto(self):
        print("Executando Resolver crashes IOS PF automático")

    def __exit(self):
        print("Saindo do programa...")
        sys.exit(0)

Menu()
