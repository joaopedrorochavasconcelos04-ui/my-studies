valor_compra = (float(800.0))
percentual_desconto = 20
socio = True
usuario_bloqueado = True

if usuario_bloqueado:
    print(f"Desconto indisponivel! Valor a pagar: {valor_compra}")

elif socio or valor_compra >= 200:
    valor_desconto = (valor_compra * (percentual_desconto / 100))
    preco_final = (valor_compra - valor_desconto)

    print (f"Desconto obtido! Valor a ser pago {preco_final: .2f}")

else: 
    print(f"Desconto de 200 reais não disponivel")





