class LessonView:

    def view_options(self):
        print("-------- AULAS --------")
        print("Escolha alguma opção:")
        print("1 - Adicionar Aula")
        print("2 - Remover Aula")
        print("3 - Editar Aula")
        print("4 - Listar Aulas")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 6):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def show_message(self, msg):
        print(msg)
