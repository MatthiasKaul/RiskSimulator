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





def simulate(attackers, defenders):
    while(attackers > 0 and defenders > 0):
        aL, dL = playRound(attackers, defenders)
        attackers -= aL
        defenders -= dL
    return attackers, defenders




import PySimpleGUI as sg
QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'


attackers = 1
defenders = 1

layout = [[[sg.Text('Attackers', size =(15, 1)), sg.InputText("3", key = "__ATTACKERS"), sg.Button("+", key = "__INC_ATK"), sg.Button("-", key = "__DEC_ATK")],
            [sg.Text('Defenders', size =(15, 1)), sg.InputText("1", key = "__DEFENDERS"), sg.Button("+", key = "__INC_DEF"), sg.Button("-", key = "__DEC_DEF")]],
            [sg.Button("Simulate!")]]
window = sg.Window(title="Best Risk Simulator", layout=layout, margins=(200, 200), return_keyboard_events=True)
while True:
    event, values = window.read()

    if  event == sg.WIN_CLOSED or event == "Escape:9":
        break
    try:
        attackers = int(values["__ATTACKERS"])
    except:
        attackers = 0

    try:
        defenders = int(values["__DEFENDERS"])
    except:
        defenders = 0

    if event == "__INC_ATK":
        attackers += 1
    if event == "__DEC_ATK":
        attackers -= 1

    if event == "__INC_DEF":
        defenders += 1
    if event == "__DEC_DEF":
        defenders -= 1

    if event == "Simulate!":
        attackers, defenders = simulate(attackers, defenders)
        #print(f"{attackers} {defenders}")
    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2, "Return:36"):
        attackers, defenders = simulate(attackers, defenders)


    window["__ATTACKERS"].Update(attackers)
    window['__DEFENDERS'].Update(defenders)



window.close()
