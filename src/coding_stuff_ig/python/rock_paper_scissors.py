from random import choice

win_cpu=0
win_player=0

while True:
    print("Rock!", "Paper!", "Scissors!\n")
    cpu=choice(["rock", "paper", "scissors"])
    player=input("Choose one or 'q' to quit: \n").lower()

    if player=="q":
        break
    elif player not in ["rock", "paper", "scissors", "q"]:
        print("Invalid input. Please try again.\n")
        continue
    
    elif player==cpu:
        print(f"It's a TIE\n")
        print(f"Player: {player}")
        print(f"CPU: {cpu}")
        
    elif player=="rock" and cpu=="scissors":
        print("Player wins!\n")
        win_player+=1
        print(f"Player: {player}")
        print(f"CPU: {cpu}")
        
    elif player=="paper" and cpu=="rock":
        print("Player wins!\n")
        win_player+=1
        print(f"Player: {player}")
        print(f"CPU: {cpu}")
        
    elif player=="scissors" and cpu=="paper":
        print("Player wins!\n")
        win_player+=1
        print(f"Player: {player}")
        print(f"CPU: {cpu}")
        
    else:
        print("CPU wins!\n")
        win_cpu+=1
        print(f"Player: {player}")
        print(f"CPU: {cpu}")
        
    if win_player==3:
        print("Player wins!\n")
        break
    
    elif win_cpu==3:
        print("CPU wins!\n")
        break

    print(f"Score: Player: {win_player} | CPU: {win_cpu}")