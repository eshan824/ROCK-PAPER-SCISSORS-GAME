# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:17:35 2021

@author: Eshan
"""

import random
turns = ("Rock", "Paper", "Scissors")
player_win = 0
computer_win = 0
match_draw = 0
matches = 10

i=0
while i < 10:
    print("")
    print("")
    print("Choose From The Followings:")
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    player = input("Enter Choice: ")
    
    if player == "1" or player == "2" or player == "3":
        if player == "1":
            print("")
            print("Player's move is Rock")
        elif player == "2":
            print("")
            print("Player's move is Paper")
        elif player == "3":
            print("")
            print("Player's move is Scissors")
            
        computer = random.choice(turns)
        print ("Computer's move is ",computer)
    
        if player == "1" and computer == "Rock":
            print("")
            print("Match was a draw")
            player_win = player_win + 0
            computer_win = computer_win + 0
            match_draw = match_draw + 1
    
        elif player == "2" and computer == "Paper":
            print("")
            print("Match was a draw")
            player_win = player_win + 0
            computer_win = computer_win + 0
            match_draw = match_draw + 1
        
        elif player == "3" and computer == "Scissors":
            print("")
            print("Match was a draw")
            player_win = player_win + 0
            computer_win = computer_win + 0
            match_draw = match_draw + 1
        
        elif player == "1" and computer == "Paper":
            print("")
            print("Computer won.")
            player_win = player_win + 0
            computer_win = computer_win + 1
        
        elif player == "1" and computer == "Scissors":
            print("")
            print("Player Won.")
            player_win = player_win + 1
            computer_win = computer_win + 0
    
        elif player == "2" and computer == "Rock":
            print("")
            print("Player won.")
            player_win = player_win + 1
            computer_win = computer_win + 0
    
        elif player == "2" and computer == "Scissors":
            print("")
            print("Computer won.")
            player_win = player_win + 0
            computer_win = computer_win + 1
        
        elif player == "3" and computer == "Rock":
            print("")
            print("Computer won.")
            player_win = player_win + 0
            computer_win = computer_win + 1
        
        elif player == "3" and computer == "Paper":
            print("")
            print("Player won.")
            player_win = player_win + 1
            computer_win = computer_win + 0
        
    else:
        print("Invalid Input")
        print("{} matches are left of 10 matches.".format(matches - i))
        continue
      
    i = i+1    
    print("")
    print("{} matches are left of 10 matches.".format(matches - i))  
    

player_lost = 10 - (player_win + match_draw)
computer_lost = 10 - (computer_win + match_draw)

print("")
print("Match Ended !")
print("")
print("Player won {} times.".format(player_win))
print("Player lost {} times.".format(player_lost))

print("")
print("")

print("Computer won {} times.".format(computer_win))
print("Computer lost {} times.".format(computer_lost))

print("")
print("")

print("Match drew {} times".format(match_draw))