senha = ""
contador = 0

while senha != "fdp":

    senha = input("Digite sua senha: ")
    contador += 1

    if senha == "fdp":
        print("Acesso Liberado")
        
    elif contador == 3:
        print("Sem mais tentativas")
        break

    
        





