class SystemView:

    def view_options(self) -> int:
        print("------- MENU -------")
        print("Escolha alguma opção:")
        print("1 - Ir para tela de Usuário")
        print("2 - Ir para tela de Produtor")
        print("3 - Ir para tela de Afiliado")
        print("4 - Ir para tela de Estatísticas")
        print("0 - Sair")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in [0, 1, 2, 3, 4]:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)