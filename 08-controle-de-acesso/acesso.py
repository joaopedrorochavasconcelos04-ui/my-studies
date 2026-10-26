nivel_acesso = 2
usuarios = ["João", "Lucas", "Pedro", "Roberta", "Heitor"]
senha = 1652

digite_usuario = (input("Digite seu usuario: "))
digite_senha = (int(input("Digite sua senha: ")))

# Niveis de acesso:
# 1 - Comum
# 2 - Medio
# 3 - Avançado

if (nivel_acesso in (1,2,3)) and (digite_usuario in usuarios) and (senha == digite_senha):
    print(f"Seu nivel de acesso é: {nivel_acesso} \nBem vindo {digite_usuario}!")

    if nivel_acesso >= 2:

     print(f"Seu nivel de acesso é {nivel_acesso} \nBem vindo a area restrita, {digite_usuario}")

else:

    print("Acesso negado")

