import random
options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Enter your command: ").lower()
    computer_choice = random.choice(options)

    resultados = {
    ("rock", "scissors"): "You won!",
    ("rock", "paper"): "You lost!",
    ("paper", "rock"): "You won!",
    ("paper", "scissors"): "You lost!",
    ("scissors", "paper"): "You won!",
    ("scissors", "rock"): "You lost!",
}
    
    if player_choice == computer_choice:
        print("Draw!")
    else:
        resultado = resultados.get((player_choice, computer_choice))
        print(f"{player_choice} vs {computer_choice} — {resultado}")