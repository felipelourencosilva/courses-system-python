class SystemView:

    def view_options(self) -> int:
        print("-------- SisCursos --------")
        print("Escolha alguma opção:")
        print("1 - Ir para tela de Usuário")
        print("2 - Ir para tela de Produtor")
        print("3 - Ir para tela de Afiliado")
        print("4 - Ir para tela de Relatórios")
        print("5 - Ir para tela de Cursos")
        print("0 - Sair")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 6):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)