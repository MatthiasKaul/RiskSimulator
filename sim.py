from random import randint
import sys


def playRound(attackers, defenders):
    effectiveAttackers = min(3, attackers)
    effectiveDefenders = min(2, defenders)

    atkDice = []
    defDice = []

    for _ in range(effectiveAttackers):
        atkDice.append(randint(1,6))

    for _ in range(effectiveDefenders):
        defDice.append(randint(1,6))

    atkDice.sort()
    atkDice = atkDice[::-1]
    defDice.sort()
    defDice = defDice[::-1]

    atkLoss = 0
    defLoss = 0
    for i in range(min(effectiveAttackers, effectiveDefenders)):
        if atkDice[i] > defDice[i]:
            defLoss += 1
        else:
            atkLoss += 1

    return atkLoss, defLoss





attackers = int(sys.argv[1])
defenders = int(sys.argv[2])
while(attackers > 0 and defenders > 0):
    aL, dL = playRound(attackers, defenders)
    attackers -= aL
    defenders -= dL

print(f"Attackers left: {attackers}, Defenders left: {defenders}")
