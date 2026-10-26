# Exercícios de prática com while
# Complete os exercícios abaixo usando a estrutura while.

print("Exercícios de prática com while")
print("=" * 35)

# Exercício 1
# Peça ao usuário para digitar números até ele digitar 0.
# Mostre quantos números foram digitados.

def exercicio_1():
    print("\nExercício 1")
    print("Digite números até digitar 0")
    # Seu código aqui

    

    while True:
        user_input = int(input(""))
        
        
        if user_input == 0:
            print("Zero foi digitado, encerrando... ")
            break

        print("Tente novamente!")



# Exercício 2
# Leia números até o usuário digitar um número negativo.
# Mostre a soma dos números positivos digitados.

def exercicio_2():
    print("\nExercício 2")
    print("Digite números até digitar um número negativo")
    # Seu código aqui
    user_input = int(input(""))
    
    while user_input > 0:
        print(f"Digite números até digitar um numero negativo \nNumero digitado: {user_input}")
    
        if user_input < 0:
            print("Um numero negativo foi digitado, encerrando... ")
            break



# Exercício 3
# Peça ao usuário para digitar uma senha.
# Enquanto a senha estiver errada, continue pedindo.
# Quando acertar, mostre uma mensagem de sucesso.

def exercicio_3():
    print("\nExercício 3")
    print("Digite a senha correta")
    # Seu código aqui

    senha = "2234fgt"
    
    while True:
        user_input = input("Digite sua senha: ")

        if user_input == senha:
            print("Acesso liberado, encerrando...")
            break

        print("Senha incorreta, tente novamente!")



# Exercício 4
# Peça ao usuário para digitar números.
# Continue até ele digitar 100.
# Mostre quantos números foram digitados antes de chegar em 100.

def exercicio_4():
    print("\nExercício 4")
    print("Digite números até chegar em 100")
    # Seu código aqui

    
    while True:
        soma = int(input("Digite numeros até chegar a 100 \nExemplo: 99 e 1, 34 e 66 e etc: "))
        soma += soma

        if soma == 100:
            print("Numero alcançado, encerrando...")
            break


# Exercício 5
# Peça ao usuário para digitar uma palavra.
# Continue pedindo até ele digitar 'sair'.
# Mostre quantas palavras foram digitadas.

def exercicio_5():
    print("\nExercício 5")
    print("Digite palavras até escrever 'sair'")
    # Seu código aqui


# Exercício 6
# Peça ao usuário para digitar idades.
# Continue até ele digitar -1.
# Mostre a média das idades digitadas.

def exercicio_6():
    print("\nExercício 6")
    print("Digite idades até digitar -1")
    # Seu código aqui


# Exercício 7
# Peça ao usuário para digitar números.
# Conte quantos números pares e ímpares foram digitados.
# Termine quando ele digitar 0.

def exercicio_7():
    print("\nExercício 7\n")
    print("Digite números até digitar 0 \nNumeros impares e pares serão contabilizados")
    # Seu código aqui

    contador_par = 0
    contador_impar = 0

    while True:
        num = int(input(""))
        print(f"Numero digitado: {num} \nPar: {contador_par} \nImpar: {contador_impar}")

        if num % 2 == 0:
            contador_par =+ 1
           
        else:
            contador_impar =+1

        if num == 0:
            break

exercicio_7()

# Exercício 8
# Peça ao usuário para digitar uma resposta.
# Continue pedindo até ele responder 'sim' ou 'nao'.

def exercicio_8():
    print("\nExercício 8")
    print("Responda com 'sim' ou 'nao'")
    # Seu código aqui


# Dica:
# Use while para repetir ações até uma condição ser satisfeita.
# Lembre-se de atualizar a condição dentro do loop.
