cliente_premium = True
valor_compra = float(20.0)
cliente_inadimplente = False
percentual_desconto = 10
valor_frete = 0
tem_cupom = False

calculo_frete = int(input("A que distancia você mora da loja? (km): "))

if calculo_frete <= 5:
    valor_frete = float(0)

elif calculo_frete <= 10:
    valor_frete = float(50)

else:
    valor_frete = float(75)

if cliente_inadimplente:
    print(
        f"Desconto e frete gratis indisponiveis \nValor compra: {valor_compra} \nValor frete: {valor_frete} \nValor total (Compra + Frete): {valor_compra + valor_frete: .2f}"
    )

if cliente_premium:
    valor_frete = 0
    print(
        f"Frete gratís disponiveis! \nValor compra: {valor_compra: .2f} \nValor frete: {valor_frete: .2f}"
    )

    if valor_compra >= 500 or tem_cupom:
        desconto = valor_compra * (percentual_desconto / 100)
        valor_final = valor_compra - desconto

        print(
            f"Desconto e freter gratís disponiveis! \nValor original: {valor_compra: .2f} \nValor compra (-10%) {valor_final: .2f} \nValor frete: {valor_frete: .2f}"
        )

elif valor_compra >= 500 or tem_cupom:
    desconto = valor_compra * (percentual_desconto / 100)
    valor_final = valor_compra - desconto

    print(
        f"Desconto obtido de 10%! \nValor original: {valor_compra: .2f} \nValor compra (-10%): {valor_final: .2f} \nValor frete: {valor_frete: .2f} \nValor total (Compra + Frete): {valor_final + valor_frete: .2f}"
    )

else:
    print(
        f"Descontos e frete gratís não disponiveis. \nValor compra: {valor_compra: .2f} \nValor frete: {valor_frete: .2f} \nValor total (Compra + Frete): {valor_compra + valor_frete: .2f}"
    )
