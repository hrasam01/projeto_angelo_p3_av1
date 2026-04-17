class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")

    def vender(self, quantidade_vendida):
        if quantidade_vendida > self.quantidade:
            print("\nEstoque insuficiente para realizar a venda.")
            return False
        else:
            self.quantidade -= quantidade_vendida
            return True


# Entrada de dados
nome = input("Nome do produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade em estoque: "))
quantidade_vendida = int(input("Quantidade vendida: "))

# Criando objeto
produto = Produto(nome, preco, quantidade)

# Exibir antes da venda
print("\n--- Dados do Produto (ANTES da venda) ---")
produto.exibir_dados()

# Processar venda
resultado = produto.vender(quantidade_vendida)

# Exibir depois da venda (somente se a venda for válida)
if resultado:
    print("\n--- Dados do Produto (DEPOIS da venda) ---")
    produto.exibir_dados()
