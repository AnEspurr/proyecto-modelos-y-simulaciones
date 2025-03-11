#--------------------------Formalidades---------------------------------
# Realizado por Pedro Díaz.
# Enunciado del dilema del prisionero:
# La policía arresta a dos sospechosos. No hay pruebas suficientes para condenarlos
# y, tras haberlos separado, los visita a cada uno y les ofrece el mismo trato.
# Las posibles combinaciones de la sentencias pueden resumirse en la siguiente matriz:
# [ COMBINACIONES |                 TU CONFIESAS              |                 TU LO NIEGAS              ]
# [  EL CONFIESA  |       AMBOS SON CONDENADOS A 5 AÑOS       | TÚ ERES CONDENADO A 20 AÑOS Y EL ES LIBRE ]
# [  EL LO NIEGA  | ÉL ES CONDENADO A 20 AÑOS Y TU ERES LIBRE |        AMBOS SON CONDENADOS A 1 AÑO       ]
# donde se espera determinar la estrategia que va a terminar siendo usada.

import random

#clase prisionero
confesses = [True, False] #confiesa = testifica en tu contra
class prisoner:
    testifies = False
    def __init__(self):
        self.testifies
    def decides(self):
        self.testifies = random.choice(confesses)


def interrogate():
    pr_a = prisoner()
    pr_b = prisoner()
    pr_a.decides()
    pr_b.decides()
    print(pr_a.testifies)
    print(pr_b.testifies)
    if(pr_a.testifies == True and pr_b.testifies == True):
        print("AMBOS VAN A SER CONDENADOS A PASAR 5 AÑOS EN PRISION")
    elif(pr_a.testifies == True and pr_b.testifies == False):
        print("PRISIONERO A SALE LIBRE, PRISIONERO B ES CONDENADO A PASAR 20 AÑOS EN PRISION")
    elif(pr_a.testifies == False and pr_b.testifies == False):
        print("AMBOS SON CONDENADOS A PASAR SOLO UN AÑO EN PRISION")
    else:
        print("PRISIONERO B ES LIBERADO, PRISIONERO A ES CONDENADO A 20 AÑOS DE PRISION")
interrogate()
