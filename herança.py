class Produto:
    '''Classe Produto padrão.'''
    
    def __init__(self, nome, preco, quantidade):
        '''Inicializa o produto com nome, preço e quantidade.'''
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def altera_quantidade(self, quantidade):
        '''Altera a quantidade em estoque.'''
        self.quantidade += quantidade
    
    def altera_preco(self, novo_preco):
        '''Altera o preço do produto.'''
        self.preco = novo_preco
    
    def __str__(self):
        '''Retorna uma string representando o produto.'''
        return f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}"


class ProdutoCritico(Produto):
    '''Classe ProdutoCritico, estende Produto.'''
    
    def __init__(self, nome, preco, quantidade, estoque_minimo):
        '''Inicializa um produto crítico, com um estoque mínimo.'''
        super().__init__(nome, preco, quantidade)
        self.estoque_minimo = estoque_minimo
    
    def altera_quantidade(self, quantidade):
        '''Altera a quantidade em estoque, respeitando o estoque mínimo.'''
        if self.quantidade + quantidade < self.estoque_minimo:
            print(f"Erro: Quantidade não pode ficar abaixo do estoque mínimo de {self.estoque_minimo}.")
        else:
            super().altera_quantidade(quantidade)
    
    def altera_preco(self, novo_preco):
        '''Altera o preço do produto, respeitando o limite de 10% de variação.'''
        limite_superior = self.preco * 1.10
        limite_inferior = self.preco * 0.90
        
        if novo_preco > limite_superior or novo_preco < limite_inferior:
            print(f"Erro: Alteração de preço não pode exceder 10% para cima ou para baixo. Limite: {limite_inferior} - {limite_superior}.")
        else:
            super().altera_preco(novo_preco)


# Teste
p1 = ProdutoCritico("Teclado", 100.00, 20, 5)

# Alterar quantidade dentro do limite
p1.altera_quantidade(-10)
print(p1)

# Tentar alterar quantidade abaixo do estoque mínimo
p1.altera_quantidade(-10)
print(p1)

# Alterar preço dentro do limite
p1.altera_preco(105.00)
print(p1)

# Tentar alterar preço fora do limite (mais de 10%)
p1.altera_preco(150.00)
print(p1)
