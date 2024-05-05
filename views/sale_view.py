class SaleView:

    def view_options(self) -> int:
        print("-------- RELATÓRIOS --------")
        print("Escolha alguma opção:")
        print("1 - Gerar relatório completo")
        print("2 - Mostrar Curso mais vendido")
        print("3 - Mostrar Curso com maior lucro")
        print("4 - Mostrar Usuário com mais cursos")
        print("5 - Mostrar Produtor com mais vendas")
        print("6 - Mostrar Afiliado com maior lucro")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 7):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def show_message(self, msg):
        print(msg)