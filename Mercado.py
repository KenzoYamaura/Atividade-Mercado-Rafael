print("Mercadinho")

cadastros = [{"user": "Cliente", "senha": 123}, 
             {"user": "Adm", "senha": "admin"}]

carrinho = []
estoque = []

def login():
    while True:        
        user = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        if user in cadastros and cadastros[user] == senha:
            print("Login bem sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

def menuADM():
    print("-"*35)
    print("1 - Adicionar Produto")
    print("2 - Atualizar Estoque")
    print("3 - Listar Estoque")
    print("0 - Sair")
    print("-"*35)
    
def menuCliente():
    print("-"*35)
    print("1 - Adicionar ao Carrinho")
    print("2 - Remover do Carrinho")
    print("3 - Visualizar Carrinho")
    print("4 - Efetuar Pagamento")
    print("0 - Sair")
    print("-"*35)

logar = input("Está logando como adm ou cLiente?: ")

while True:
    if logar == "adm":
        menuADM()
        opcao = input("Oque deseja fazer?: ")
        if opcao == "1":
            produtos = {}
            produtos["código"] = int(input("código do Produto: "))
            produtos["nome"] = input("Nome do Produto: ")
            produtos["quantidade"] = int(input("quantidade do Produto: "))
            estoque.append(produtos)

        elif opcao == "2":
            add_remover = input("Deseja adicionar ou remover: ")
            if add_remover == "adicionar":
                nome_produto = input("Digite o nome: ")
                for i in estoque:
                    if i["nome"] == nome_produto:
                        add_quantidade = int(input("Insira a nova quantidade para o estoque: "))
                        i["quantidade"] += add_quantidade
                    else:
                        nome_produto = input("Digite o nome: ")
                        for i in estoque:
                            if i["nome"] == nome_produto:
                                remover_quantidade = int(input("Digite a saída: "))
                                i["quantidade"] -= remover_quantidade
            elif add_remover == "remover":
                nome_produto = input("Digite o nome: ")
                for i in estoque:
                    





            

    elif logar == "cliente":
        menuCliente()

    else:
        print("Opção inválida")







