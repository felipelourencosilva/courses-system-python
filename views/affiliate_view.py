class AffiliateView:

    def view_options(self) -> int:
        print("------- AFILIADO -------")
        print("Escolha alguma opção:")
        print("1 - ...")
        print("2 - ...")
        print("0 - Voltar")

        while True:
            chosen = input("Sua escolha: ")
            if not chosen.isnumeric or int(chosen) not in [0, 1, 2]:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(chosen)