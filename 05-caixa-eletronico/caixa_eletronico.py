saldo = float(1597.89)

print("O saldo atual é: R$:", saldo)

valor_saque = float(input("Qual o valor desejado para o saque? "))     
if valor_saque > saldo:
    print("Valor do saque excede o saldo atual!!")

elif valor_saque <= 0:
    print ("Saldo não pode ser igual ou inferior a zero")

else:
   saldo = (saldo - valor_saque)    
   print ("Saldo realizado! Saldo atual é:", saldo)