class SystemView:

    def __init__(self):
        pass

    def show_options(self) -> int:
        print("------- MENU -------")
        print("Escolha alguma opção:")
        print("1 - Ir para tela de Usuário")
        print("2 - Ir para tela de Estatísticas")
        print("0 - Sair")

        while True:
            chosen = input("Sua escolha: ")
            if not chosen.isnumeric or int(chosen) not in [0, 1, 2]:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(chosen)