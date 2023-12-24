import random
from random import randrange

def print_status(player1,random,i):
    print("Round #"+str(i)+", random number is  " + str(random) + ", "+player1[0]+" scored")

#phase 1:
def play_game1(player1,player2):
    point = 0
    player1 = [player1, point]
    player2 = [player2, point]
    i = 0
    while (player1[1] != 3 and player2[1] != 3):
        i += 1
        random_number = randrange(-5, 13)

        if random_number % 2 == 0:
            player1[1] += 1
            print_status(player1, random_number, i)
            print("Status: " + player1[0], player1[1], ",", player2[0], player2[1])
        else:
            player2[1] += 1
            print_status(player2, random_number, i)
            print("Status: " + player1[0], player1[1], ",", player2[0], player2[1])
    if player1[1] == 3:
        print(player1[0], "wins")
    else:
        print(player2[0], "wins")



#phase 2:
def play_round(player1,player2):
    random_number = randrange(-5, 13)

    if random_number % 2 == 0:
        player1[1] += 1
        print("Status: " + player1[0], player1[1], ",", player2[0], player2[1])
    else:
        player2[1] += 1
        print("Status: " + player1[0], player1[1], ",", player2[0], player2[1])


def play_with_boss(player1,boss):
    player1[1]=0

    while (player1[1] != 3 and boss[1] != 3):
        random_number = randrange(-5, 13)
        if random_number % 2 == 0 and random_number>=0:
            player1[1] += 1
            print("Status: " + player1[0], player1[1], ",", boss[0], boss[1])
        else:
            boss[1] += 1
            print("Status: " + player1[0], player1[1], ",", boss[0], boss[1])

    if player1[1] == 3:
        print(player1[0], "wins")
    else:
        print(boss[0], "wins")

#phase 2+3:
def play_tournament(players,bestof):
    boss = input("enter the name of the boss :")
    boss = [boss, 0]
    player1, player2 = random.sample(players, 2)
    while max(player1[1],player2[1])<(bestof+1)//2:
        play_round(player1,player2)
        player1, player2 = random.sample(players, 2)
        win_player=max(player1,player2)
    print(win_player[0],"wins")
    play_with_boss(win_player, boss)

def input_user():
    c = int(input("enter how many players will play:"))
    players = []
    i = 0
    while i != c:
        player = input("enter the name of first player :")
        player = [player, 0]
        players.append(player)
        i += 1
    return players


players=input_user()
play_tournament(players,5)