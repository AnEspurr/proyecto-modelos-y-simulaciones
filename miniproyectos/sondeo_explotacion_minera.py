#--------------------------Formalidades---------------------------------
# Realizado por Pedro Díaz.
# Enunciado del ejercicio:
# Una petrolera pide una excavación de sondeo sobre un terreno para buscar petróleo.
# Se invierten aproximadamente 10000000 de dólares en la exploración del terreno.
# De acuerdo a estimaciones de expertos, hay un 40% fr probabilidades de encontrar petróleo en el terreno.
# En caso de encontrar petróleo, por ley se le debe entregar aproximadamente un 40% de lo que se encuentre.
# Teniendo el cuenta el valor del barril de petróleo (150$) y las estimaciones de barriles obtenibles de los posibles posos encontrados (300000)..
# Ver sí las exploraciones son una apuesta factible
# Conclusión: SI LO SON $$$$$$$$$$

import random
#----------------------constants/variables used----------------------------

success_pr = 0.40 #P(x)
failure_pr = 0.60 #Obtenido del complemento P(exito)
company_percent_wins = 0.60 #P(x)
state_percent_wins = 0.40 #complemento P(x)

net_barrels_worth = 300000
exploration_cost = 1000000
barrel_price = 150 #por barril, a casa platita
total_explorations = 10000

#---------------------------functions-----------------------------

#HAY PETRÓLEOOOOOOOOOOOO
def evaluateExploration():
    return random.choices([True, False], weights=[success_pr, failure_pr])[0]


def letsGoExploring():
    total_barrels = 0
    company_oil_balance = 0
    state_oil_balance = 0
    success_cases = 0
    success_rates = 0
    gains = 0
    i = 0
    while(i < total_explorations):
        company_oil_balance -= exploration_cost
        if(evaluateExploration()):
            success_cases += 1
            total_barrels += net_barrels_worth
            gains = net_barrels_worth * barrel_price #a casa platita
            # a cada quien le toca su parte del botín
            company_oil_balance += gains * company_percent_wins
            state_oil_balance += gains * state_percent_wins
        success_rates = success_cases/total_explorations
        i += 1
    print("ESTADÍSTICAS")
    print("TOTAL DE EXPLORACIONES REALIZADAS:", total_explorations)
    print("CANTIDAD DE BARRILES PROCESADOS: ", total_barrels)
    print("ESTADO DE CUENTA DE LA EMPRESA: ", company_oil_balance)
    print("LO QUE NOS ROBÓ EL ESTADO: ", state_oil_balance)
    print("TASA DE EXITO: ", (success_rates)*100, "%")



#---------------------------------main----------loop--------------------------------
letsGoExploring()
#------------------------END------OF------FILE------:rage:-------------------