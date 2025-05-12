#precos = [1500, 1000, 800, 2000]
#produtos = ["celular", "camera", "fone de ouvido", "monitor"]
#produto_procurado = input("Digite aqui um produto:")
#produto_procurado = produto_procurado.lower()

#if produto_procurado in produtos:
#    posicao = produtos.index(produto_procurado)
#    preco = precos[posicao]
#    print(f"Produto: {produto_procurado}, Preco: {preco}")
#else:
#    print("produto nao encontrado, tente novamente")
#
#
# DICIONARIO
#precos = [1500, 1000, 800, 2000]
#produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

#preco_celular = dic_precos["celular"]
#print(preco_celular)

#dic_precos["celular"] = 2000
#print(dic_precos)

#tamanho
#print(len(dic_precos))

#Exercicio Dicionario 
dic_precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
produto_procurado = input("Digite aqui o produto:")
produto_procurado = produto_procurado.lower()

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"Produto {produto_procurado}, Preco: {preco}")

else:
    print("Produto nao encontrado, tente novamente")    
