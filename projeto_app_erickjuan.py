'''
CRUD

Hamburgueria

Entrega o cardapio
Escolhe seu produto
pagar
retirar no caixa
Erick Juan
'''




print("..gestão da hambugueria")
print("1.. Cadastro")
print("2..Cardapio")
print("3.. Preços")
print("4..Pagamentos")

while True:
    escolha = input("\nEscolha uma opção")
    if escolha == '1':
        print("Novo cadastro")
    # codigo para entrega o cardapio


    elif escolha =='0': 
        print("saindo do sistema.até logo !")
    break


else:

    
    if escolha == '1':
        print("Fazer seu cadastro")
        #codigo para entrega o pedido

    elif escolha == '2':
        print("Cardapio")
        #codigo fazer seu pedido

    elif escolha == '3':
        print("Preços")
        # codigo anotar o pagamento do cliente
    
    elif escolha == '4':
        print("Pagamentos")
        # codigo embalar o produto
    
         

    if escolha == '1' :
        print("\n--- Novo Cadastro---")
        

    #dados solicitados ao cliente
    nome = input('nome :')
    email = input('email :')


    if escolha == '2':
        print("\n--- Cardapio---")
        input('escolha seu pedido')

        print("-BurgerX Pão, hambúrguer bovino , queijo mussarela, alface e tomate.")
        print("X-Salada Pão, hambúrguer bovino , queijo, alface, tomate e maionese da casa.")
        print("X-Bacon Pão, hambúrguer bovino , queijo, bacon crocante e maionese da casa.")
        print("X-Egg Pão, hambúrguer bovino , queijo e ovo frito.")
        print("X-Tudo Pão,hambúrguer bovino, queijo, bacon, ovo, alface, tomate, milho, batata palha e maionese.")
        print("Smash Burger Pão brioche, 2 smash burgers 80g, queijo cheddar e molho especial.")
        print("Bacon Supreme ão brioche, hambúrguer 150g, cheddar, bacon crocante e cebola caramelizada.")
        print("Cheddar Duplo ão brioche, 2 hambúrgueres, cheddar cremoso e molho especial.")
        print("Barbecue Burger Pão brioche, hambúrguer , queijo, bacon e molho barbecue.")

    print("Batata Frita Pequena")

    print("Batata Frita Grande")

    print("Batata com Cheddar e Bacon")

    print("Onion Rings (Anéis de cebola")

    print("Bebidas")

    print("Refrigerante em lata")

    print("Refrigerante 600ml")
    
    print("Aguá mineral")

    print("Suco natural")

    if escolha == '3':
        
        print("\n---Preços---")

        print(" X Burger")
        print("15$")

        print(" X salada")
        print("15$")

        print("X-Bacon")
        print("20$")

        print("X-Egg")
        print("15$")

        print("X- tudo")
        print("25$")

    print("\n---Hambugueres especias---")

    print("Smash Burger")
    print("25$")

    print("Bacon Supreme ")
    print("30$")

    print("Cheddar Duplo")
    print("30$")

    print("Barbecue Burger ")
    print("30$")

    print("\n---Batatas---")

    print("Batata Frita Pequena")
    print("10$")

    print("Batata Frita Grande")
    print("18$")

    print("Batata com Cheddar e Bacon")
    print("22$")

    print("Onion Rings (Anéis de cebola")
    print("22$")

    print("\n---Bebidas---")

    print("Refrigerante em lata")
    print("8$")

    print("Refrigerante 600ml")
    print("9$")
    
    print("Aguá mineral")
    print("5$")

    print("Suco natural")
    print("7$")

    