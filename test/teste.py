def menuADM():
    print("-"*35)
    print("1 - Cadastrar Usuário")
    print("2 - Adicionar Produto")
    print("3 - Atualizar Estoque")
    print("4 - Listar Estoque")
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

print("Mercadinho")

'''cadastros = [{"user": "Cliente", "senha": 123}, 
             {"userAdm": "Adm", "senhaAdm": 321}]'''

cadastros = [{"user": "admin", "senha": "112233"}]
carrinho = []
estoque = []

def adicionarProduto():
    produtos = {}
    produtos["nome"] = input("Nome do Produto: ")
    produtos["quantidade"] = int(input("quantidade do Produto: "))
    produtos["preço"] = float(input("Preço R$: "))            
    estoque.append(produtos)

def adicionarRemover():
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
        nome_produto = input("Digite o nome: ").lower()
        for i, produtos in enumerate(estoque):
            if produtos["nome"] == nome_produto:
                del estoque[i]
                print(f"O produto {nome_produto} foi removido com sucesso")
            else:
                print(f"o produto {nome_produto} não localizado")

def cadastrar():
    aux = {}
    aux["email"] = input("Insira seu E-mail: ")
    aux["user"] = input("Seu Nome: ")
    aux["senha"] = input("Sua Senha: ")
    cadastros.append(aux)
    return aux

def login():
    while True:
        user = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        for cad in cadastros:
            if cad["user"] == user and cad["senha"] == senha:
                print("Login bem sucedido.")
                return True
            else:
                print("Usuário ou senha incorretos. Tente novamente.")
            

login()

logar = input("Está logando como ADM ou Cliente?: ").lower()

while True:
    if logar == "adm":
        menuADM()
        opcao = input("Oque deseja fazer?: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break

        elif opcao == "1":
            cadastrar()

        elif opcao == "2":
            adicionarProduto()

        elif opcao == "3":
            adicionarRemover()

        elif opcao == "4":
            for i in estoque:
                print(i)