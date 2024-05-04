class LessonView:

    def view_options(self) -> int:
        print("------- AULA -------")
        print("Escolha alguma opção:")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 1):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)