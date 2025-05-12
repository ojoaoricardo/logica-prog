faturamento = 1000
custo = 800

lucro = faturamento - custo

if lucro > 0:
    print(lucro)
else:
    print("Prejuizo!!")
    print(lucro)

produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite aqui o produto:")
novo_produto = novo_produto.lower()
if novo_produto in produtos:
    print("Produto já cadastrado")
else:
    print("Produto cadastrado com sucesso")
    produtos.append(novo_produto)

print(produtos)        

