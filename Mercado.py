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

logar = input("Está logando como ADM ou Cliente?: ").lower()

while True:
    if logar == "adm":
        menuADM()
        opcao = input("Oque deseja fazer?: ")
        if opcao == "1":
            produtos = {}
            produtos["nome"] = input("Nome do Produto: ")
            produtos["quantidade"] = int(input("quantidade do Produto: "))
            produtos["preço"] = int(input("Preço R$: "))            
            estoque.append(produtos)

        elif opcao == "2":
            add_remover = input("Deseja Adicionar ou Remover: ").lower()
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
                for i, produtos in estoque:
                    print(i, produtos)

        elif opcao == "3":
            for i in estoque:
                print(i)

'''elif atualizar == "Remover":
        nome_produto = input("Digite o produto que quer remover: ")
        for i, produto in enumerate(estoque): 
            if produto["nome"] == nome_produto:                
                del estoque[i] 
                print(f"O produto {nome_produto} foi deletado com sucesso")
            else:
                print(f"O produto {nome_produto} não encontrado")'''






