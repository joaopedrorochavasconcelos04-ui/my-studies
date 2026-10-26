n1 = int(input("Digite um número: "))
tamanho = []

for numeros in range(1, n1 + 1):
    if numeros % 2 == 0 and numeros > 10:

        tamanho.append(numeros)
        print(f"Numeros maiores que 10: {numeros} \nQuantidade de numeros pares maiores que 10: {len(tamanho)}")