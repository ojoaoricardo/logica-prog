vendas = 20000
if vendas > 15000:
    bonus = 500
elif vendas > 10000:  
       bonus = 150
elif vendas > 5000:
       bonus = 50           
else:
    bonus = 0

print ("Bonus", bonus)

if vendas > 5000:
      if vendas > 10000:
            if vendas > 15000:
                  bonus = 500
            else:
                  bonus = 150
      else: 
            bonus = 50
else:
      bonus = 0
print("Bonus", bonus)


vendas = 17000
vendas_empresa = 60000
meta_empresa = 50000
if not vendas_empresa > meta_empresa:
      bonus = 0
else:
            
    if vendas > 15000 and vendas_empresa > meta_empresa:
        bonus = 500
    elif vendas > 10000 and vendas_empresa > meta_empresa:  
       bonus = 150
    elif vendas > 5000 and vendas_empresa > meta_empresa:
       bonus = 50           
    else:
        bonus = 0
print("Bonus", bonus)

