'''
CRUD

Hamburgueria

Entrega o cardapio
Escolhe seu produto
pagar
retirar no caixa
Erick Juan
'''

print("=== Gestão da Hamburgueria ===")

while True:
    print("\nMenu")
    print("1 - Cadastro")
    print("2 - Cardápio")
    print("3 - Preços")
    print("4 - Pagamentos")
    print("5 - Entrega")
    print("6.feedback")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\nNovo Cadastro")

        nome = input("Nome: ")
        email = input("Email: ")
        print("Cadastro realizado com sucesso!")

    elif escolha == "2":
        print("\nCardápio")

        print("\nHambúrgueres:")

        print("1 - X-Burger (Pão, hambúrguer bovino, queijo mussarela, alface e tomate)")
        print("2 - X-Salada (Pão, hambúrguer bovino, queijo, alface, tomate e maionese)")
        print("3 - X-Bacon (Pão, hambúrguer bovino, queijo, bacon crocante)")
        print("4 - X-Egg (Pão, hambúrguer bovino, queijo e ovo frito)")
        print("5 - X-Tudo (Pão, hambúrguer bovino, queijo, bacon, ovo, alface e tomate)")

        print("\nHambúrgueres Especiais:")
        print("6 - Smash Burger")
        print("7 - Bacon Supreme")
        print("8 - Cheddar Duplo")
        print("9 - Barbecue Burger")

        print("\nBatatas:")
        print("10 - Batata Frita Pequena")
        print("11 - Batata Frita Grande")
        print("12 - Batata com Cheddar e Bacon")
        print("13 - Onion Rings")

        print("\nBebidas:")
        print("14 - Refrigerante lata")
        print("15 - Refrigerante 600ml")
        print("16 - Água mineral")
        print("17 - Suco natural")

    elif escolha == "3":
        print("\nPreços")

        print("\nHambúrgueres:")
        print("X-Burger - R$15")
        print("X-Salada - R$15")
        print("X-Bacon - R$20")
        print("X-Egg - R$15")
        print("X-Tudo - R$25")

        print("\nHambúrgueres Especiais:")
        print("Smash Burger - R$25")
        print("Bacon Supreme - R$30")
        print("Cheddar Duplo - R$30")
        print("Barbecue Burger - R$30")

        print("\nBatatas:")
        print("Batata Frita Pequena - R$10")
        print("Batata Frita Grande - R$18")
        print("Batata com Cheddar e Bacon - R$22")
        print("Onion Rings - R$22")

        print("\nBebidas:")
        print("Refrigerante lata - R$8")
        print("Refrigerante 600ml - R$9")
        print("Água mineral - R$5")
        print("Suco natural - R$7")

    elif escolha == "4":
        print("\nPagamentos")

        print("1 - Dinheiro")
        print("2 - Cartão")
        print("3 - Pix")
        pagamento = input("Escolha a forma de pagamento: ")
        print("Pagamento registrado!")

    elif escolha == "5" :

        print("entrega")
        print("\n Entrega :")
        input("Confirmar sua entrega com sim ou não :")
        print('Seu pedido saiu para entrega ')
        print('seu pedido saiu para entregar')
        input('seu pedido foi entregue com sucesso')


    elif escolha == "6":
        print('mande sua gestação')
        print('manda seu feedback')

        input('mande seu feedback\sua sugestão para nossa loja')
        print('obrigado pela sua sugestão\feedback')











    elif escolha == "0":
        print("Saindo do sistema.obrigado por visitar nossa hambugueria.")
        break