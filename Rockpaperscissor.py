import random
def playgame():
    print("Welcomr to Gaming Arena!!")
    print("Rock--->1")
    print("Paper--->2")
    print("Scissor--->3")

    choices=["Rock","Paper","Scissor"]

    while(True):
        print("select one out of the three to start the game: ")
        n=int(input("enter your choice (1,2 or 3) : "))
        choices=["Rock","Paper","Scissor"]
        random_choice=random.choice(choices)

        if n == 1 and random_choice == "Paper":
            print("It is Rock vs Paper. You lose.")
        elif n == 1 and random_choice == "Scissor":
            print("It is Rock vs Scissor. You win!")
        elif n == 2 and random_choice == "Rock":
            print("It is Paper vs Rock. You win!")
        elif n == 2 and random_choice == "Scissor":
            print("It is Paper vs Scissor. You lose.")
        elif n == 3 and random_choice == "Rock":
            print("It is Scissor vs Rock. You lose.")
        elif n == 3 and random_choice == "Paper":
            print("It is Scissor vs Paper. You win!")
        else:
            print("It's a tie!")

        play_again= input("Do you want to play again (yes/no) :")
        if play_again != 'yes':
            break

if __name__=="__main__":
    playgame()  