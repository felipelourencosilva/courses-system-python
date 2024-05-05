class ModuleView:

    def view_options(self):
        print("-------- MÓDULOS --------")
        print("Escolha alguma opção:")
        print("1 - Adicionar Modulo")
        print("2 - Remover Módulo")
        print("3 - Editar Módulos")
        print("4 - Listar Módulos")
        print("5 - Ir para tela de Aulas")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 6):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def show_message(self, msg):
        print(msg)
