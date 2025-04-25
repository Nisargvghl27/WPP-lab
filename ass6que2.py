# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.

# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.

import random


class Rock_paper_scissors:
    choices = ["rock", "paper", "scissors"]

    def __init__(self, round):
        self.totalround = round
        self.compwin = 0
        self.userwin = 0
        self.currentround = 1

    def roundwinner(self, userchoice, compchoice):
        if (
            (userchoice == "rock" and compchoice == "scissors")
            or (userchoice == "scissors" and compchoice == "paper")
            or (userchoice == "paper" and compchoice == "rock")
        ):
            return "user"
        elif userchoice == compchoice:
            return "draw"
        else:
            return "computer"

    def play(self):
        print()
        print(f"Round {self.currentround} of {self.totalround}")
        userchoice = input("Enter choice form rock, paper, scissors : ").lower()
        if userchoice not in self.choices:
            print("Invalid choice!!! Try again...")
            return self.play()

        compchoice = random.choice(self.choices)
        print(f"Computer choice : {compchoice}")

        winner = self.roundwinner(userchoice, compchoice)
        if winner == "user":
            self.userwin += 1
            print("You win the round")
        elif winner == "computer":
            self.compwin += 1
            print("computer win the round")
        else:
            print("Draw the round")
        print()
        self.currentround += 1

    def gamewinner(self):
        print(f"score : user {self.userwin} , computer {self.compwin}")
        if self.userwin > self.compwin:
            print("Congratulation !!! You win the game")
        elif self.userwin < self.compwin:
            print("Computer win the game !!! Better luck next time.")
        else:
            print("Game is Tie.")

    def startgame(self):
        print("Welcome in the Rock-Paper-Scissors game")
        while self.currentround <= self.totalround:
            self.play()
        self.gamewinner()


n = int(input("Enter number of round : "))
a = Rock_paper_scissors(n)
a.startgame()