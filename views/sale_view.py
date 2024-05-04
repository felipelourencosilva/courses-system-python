class SaleView:

    def view_options(self) -> int:
        print("------- ESTATÍSTICAS -------")
        print("Escolha alguma opção:")
        print("0 - Voltar")

        while True:
            chosen = input("Sua escolha: ")
            if not chosen.isnumeric() or int(chosen) not in [0]:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(chosen)