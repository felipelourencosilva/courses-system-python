class SaleView:

    def view_options(self) -> int:
        print("------- ESTATÍSTICAS -------")
        print("Escolha alguma opção:")
        print("1 - Gerar relatório")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 2):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def show_message(self, msg):
        print(msg)