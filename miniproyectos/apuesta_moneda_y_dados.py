#--------------------------Formalidades---------------------------------
# Realizado por Pedro Díaz.
# Enunciado del ejercicio:
# Se propone una apuesta con una moneda y un dado con las siguientes reglas:
# 1. Sí se obtiene un número par en el dado Y cara en la moneda, se gana la apuesta
# 2. Sino, se pierde lo apostado
# Pero uno es ludópata, así que se redobla la apuesta cada que tenemos menos
# Conclusión: Ésta apuesta es una horrible idea xD

import random
import math
#----------------------constants/variables used----------------------------

goal = 2000
initial_money = 1000
bet = 200
total_wins = 0
total_losses = 0
attempts = 10
coin = ["head", "tails"] #tails never fails, that's what they say

#---------------------------functions-----------------------------
def parityCheck(number):
    check = True if (number % 2 == 0) else False
    return check

def gameProcess(total_coins, bet):
    dice = random.randint(1,6)
    check_coin_flip = random.choice(coin)
    if(parityCheck(dice) and check_coin_flip == "head"):
        return total_coins+bet
    return total_coins-bet

def increaseBet(total_coins, current_bet):
    if(total_coins < initial_money):
        return math.fabs(current_bet*2) #Para cuando las apuestas salen MUY mal
    else:
        return current_bet

def isGoalReached(total_coins):
    if(total_coins > goal and total_coins > 0):
        return True
    else:
        return False

def gameLoop():
    global initial_money
    global total_wins
    global total_losses
    global attempts
    global bet
    i = 0
    print("...con una apuesta inicial de ", str(initial_money), " monedas: ")
    #LETS GO GAMBLINNNNNNNN
    while(i < attempts):
        start = bet
        current_money = initial_money
        while(current_money < goal and current_money > 0):
            current_money = gameProcess(current_money, start)
            bet = increaseBet(current_money, start)
            if(isGoalReached(current_money)):
                total_wins += 1
            else:
                total_losses += 1
        i+=1 

    print("total de intentos: ", str(i))
    print("total de lanzamientos aciertos: ", str(total_wins))
    print("total de lanzamientos fallidos: ", str(total_losses))
    print("total obtenido: ", str(current_money))

#---------------------------------main----------loop--------------------------------

gameLoop()

#------------------------END------OF------FILE------:rage:-------------------