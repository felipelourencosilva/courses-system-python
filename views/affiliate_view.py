class AffiliateView:

    def view_options(self) -> int:
        print("------- AFILIADO -------")
        print("Escolha alguma opção:")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in [0]:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)