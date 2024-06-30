cadastros = [{"user": "admin", "senha": "112233", "email": "admin@example.com"}]
carrinho = []
estoque = []
historico_compras = []

def menuADM():
    print("-" * 35)
    print("1 - Cadastrar Usuário")
    print("2 - Adicionar Produto")
    print("3 - Atualizar Estoque")
    print("4 - Listar Estoque")
    print("0 - Sair")
    print("-" * 35)
    
def menuCliente():
    print("-" * 35)
    print("1 - Adicionar ao Carrinho")
    print("2 - Remover do Carrinho")
    print("3 - Visualizar Carrinho")
    print("4 - Efetuar Pagamento")
    print("5 - Histórico de Compras")
    print("0 - Sair")
    print("-" * 35)

def adicionarProduto():
    produto = {}
    produto["nome"] = input("Nome do Produto: ")
    produto["descricao"] = input("Descrição do Produto: ")
    produto["quantidade"] = int(input("Quantidade do Produto: "))
    produto["preco"] = float(input("Preço R$: "))            
    estoque.append(produto)
    print(f"Produto '{produto['nome']}' adicionado ao estoque.")

def atualizarEstoque():
    nome_produto = input("Digite o nome do produto: ")
    for produto in estoque:
        if produto["nome"] == nome_produto:
            quantidade = int(input("Insira a nova quantidade para o estoque: "))
            produto["quantidade"] += quantidade
            print(f"Quantidade atualizada para {produto['quantidade']}")
            return
    print(f"Produto '{nome_produto}' não encontrado no estoque.")

def cadastrar():
    aux = {}
    aux["email"] = input("Insira seu E-mail: ")
    aux["user"] = input("Seu Nome: ")
    aux["senha"] = input("Sua Senha: ")
    cadastros.append(aux)
    print(f"Usuário '{aux["user"]}' cadastrado com sucesso.")
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

# Funções para o cliente
def adicionarAoCarrinho():
    nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
    for produto in estoque:
        if produto["nome"] == nome_produto:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= produto["quantidade"]:
                carrinho.append({"nome": nome_produto, "quantidade": quantidade, "preco": produto["preco"]})
                produto["quantidade"] -= quantidade
                print(f"{quantidade} {nome_produto}(s) adicionado(s) ao carrinho.")
            else:
                print("Quantidade insuficiente no estoque.")
            return
    print(f"Produto '{nome_produto}' não encontrado no estoque.")

def removerDoCarrinho():
    nome_produto = input("Digite o nome do produto que deseja remover do carrinho: ")
    for item in carrinho:
        if item["nome"] == nome_produto:
            carrinho.remove(item)
            print(f"{item['quantidade']} {nome_produto}(s) removido(s) do carrinho.")
            return
    print(f"Produto '{nome_produto}' não encontrado no carrinho.")

def visualizarCarrinho():
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print("Carrinho:")
        for item in carrinho:
            print(item)
        total = sum(item["quantidade"] * item["preco"] for item in carrinho)
        print(f"Total: R$ {total:.2f}")

def efetuarPagamento(usuario):
    if not carrinho:
        print("O carrinho está vazio.")
        return
    visualizarCarrinho()
    confirmacao = input("Deseja finalizar a compra? (s/n): ").lower()
    if confirmacao == 's':
        historico_compras.append({"usuario": usuario["user"], "carrinho": carrinho.copy()})
        carrinho.clear()
        print("Pagamento efetuado com sucesso. Carrinho esvaziado.")
    else:
        print("Compra não finalizada.")

def exibirHistoricoCompras(usuario):
    print("Histórico de Compras:")
    for compra in historico_compras:
        if compra["usuario"] == usuario["user"]:
            print(compra["carrinho"])

# Início do programa
print("Mercadinho")
usuario = login()
logar = input("Está logando como ADM ou Cliente?: ").lower()

while True:
    if logar == "adm":
        menuADM()
        opcao = input("O que deseja fazer?: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break
        elif opcao == "1":
            cadastrar()
        elif opcao == "2":
            adicionarProduto()
        elif opcao == "3":
            atualizarEstoque()
        elif opcao == "4":
            print("Estoque:")
            for produto in estoque:
                print(produto)

    elif logar == "cliente":
        menuCliente()
        opcao = input("O que deseja fazer?: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break
        elif opcao == "1":
            adicionarAoCarrinho()
        elif opcao == "2":
            removerDoCarrinho()
        elif opcao == "3":
            visualizarCarrinho()
        elif opcao == "4":
            efetuarPagamento(usuario)
        elif opcao == "5":
            exibirHistoricoCompras(usuario)
    else:
        print("Opção inválida.")
