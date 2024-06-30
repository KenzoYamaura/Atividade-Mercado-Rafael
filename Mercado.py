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

cadastros = [{"user": "admin", "senha": "112233", "email": "admin@example.com"}]
carrinho = []
estoque = [
    {"nome": "arroz", "descricao": "Arroz branco, pacote de 1kg", "quantidade": 50, "preco R$": 5.00},
    {"nome": "feijao", "descricao": "Feijão preto, pacote de 1kg", "quantidade": 30, "preco R$": 6.50},
    {"nome": "macarrao", "descricao": "Macarrão tipo espaguete, pacote de 500g", "quantidade": 40, "preco R$": 4.00},
    {"nome": "oleo", "descricao": "Óleo de soja, garrafa de 1L", "quantidade": 25, "preco R$": 7.00},
    {"nome": "sal", "descricao": "Sal refinado, pacote de 1kg", "quantidade": 60, "preco R$": 2.00},
    {"nome": "acucar", "descricao": "Açúcar cristal, pacote de 1kg", "quantidade": 45, "preco R$": 3.50},
    {"nome": "cafe", "descricao": "Café em pó, pacote de 500g", "quantidade": 20, "preco R$": 8.00},
    {"nome": "leite", "descricao": "Leite integral, litro", "quantidade": 50, "preco R$": 3.00},
    {"nome": "biscoito", "descricao": "Biscoito de maisena, pacote de 200g", "quantidade": 35, "preco R$": 2.50},
    {"nome": "detergente", "descricao": "Detergente líquido, frasco de 500ml", "quantidade": 15, "preco R$": 1.50}
]
historico_compras = []

def adicionarProduto():
    produtos = {}
    produtos["nome"] = input("Nome do Produto: ")
    produtos["descricao"] = input("Digite a descrição do produto: ")
    produtos["quantidade"] = int(input("quantidade do Produto: "))
    produtos["preço R$"] = int(input("Preço R$: "))            
    estoque.append(produtos)
    print(f"Produto '{produtos['nome']}' adicionado com sucesso")

def adicionarRemover():
    add_remover = input("Deseja Adicionar ou Remover: ").lower()
    if add_remover == "adicionar":
        nome_produto = input("Digite o nome: ")
        for produto in estoque:
            if produto["nome"] == nome_produto:
                add_quantidade = int(input("Insira a nova quantidade para o estoque: "))
                produto["quantidade"] += add_quantidade
                print(f"Quantidade atualizada")
                return
        print(f"Produto {nome_produto} não encontrado")
    
    elif add_remover == "remover":
        nome_produto = input("Digite o nome do produto: ")
        for i, produto in enumerate(estoque):
            if produto["nome"] == nome_produto:
                remover_quantidade = int(input("Digite a quantidade a ser removida: "))
                if remover_quantidade >= produto["quantidade"]:
                    estoque.pop(i)
                    print(f"Produto '{nome_produto}' removido do estoque")
                else:
                    produto["quantidade"] -= remover_quantidade
                    print(f"Quantidade atualizada")
                return
            print(f"Produto '{nome_produto}' Não localizado")
    else:
        print("Opção Inválida. Digite 'adicionar' ou 'remover'")

def cadastrar():
    aux = {}
    aux["email"] = input("Insira seu E-mail: ")
    aux["nome"] = input("Seu Nome: ")
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
                return cad
        print("Usuário ou senha incorretos. Tente novamente.")

def adicionarAoCarrinho():
    nome_produto = input("Digite o nome do produto para adicionar no carrinho: ")
    for produto in estoque:
        if produto["nome"] == nome_produto:
            quantidade = int(input("Digite quantos deseja: "))
            if quantidade <= produto["quantidade"]:
                carrinho.append({"nome": nome_produto, "descrição": produto["preco"], "quantidade": quantidade, "preco": produto["preco R$"]})
                produto["quantidade"] -= quantidade
                print(f"{quantidade} {nome_produto} adicionado ao carrinho")
            else:
                print("Quantidade insuficiente no estoque.")
            return
    print(f"Produto '{nome_produto}' Não encontrado no estoque")


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
        
        