from random import randint
import sys

DEFAULTBG = '#FF1493'


class GameRecord:
    """docstring for GameRecord."""

    def __init__(self):
        attackerName = "defaultAtk"
        defenderName = "defaultDef"
        attackers = 1
        defenders = 1
        atkLosses = 0
        defLosses = 0
    def __repr__(self):
        print(f"{self.attackerName} attacked {self.defenderName} with {self.attackers} against {self.defenders} units. {self.attackerName} lost {self.atkLosses} units, {self.defenderName} lost {self.defLosses}")
    def __str__(self):
        return f"{self.attackerName} attacked {self.defenderName} with {self.attackers} against {self.defenders} units. {self.attackerName} lost {self.atkLosses} units, {self.defenderName} lost {self.defLosses}"
GameHistory = []
players = []


def showStatWindow():
    global GameHistory
    global players
    effectiveWins = []
    for attacker in players:
        effectiveWins.append([])
        effectiveWins[-1].append(attacker)
        for defender in players:
            atkCasualties = 0
            defCasualties = 0
            if attacker == defender:
                effectiveWins[-1].append("XXXXX")
            else:
                for gr in GameHistory:
                    if gr.attackerName == attacker and gr.defenderName == defender:
                        atkCasualties += gr.atkLosses
                        defCasualties += gr.defLosses
                effectiveWins[-1].append(f"{defCasualties} \ {atkCasualties}")

    losses = dict()
    kills = dict()
    for p in players:
        losses[p] = 0
        kills[p] = 0
    for gr in GameHistory:
        losses[gr.attackerName] += gr.atkLosses
        losses[gr.defenderName] += gr.defLosses
        kills[gr.attackerName] += gr.defLosses
        kills[gr.defenderName] += gr.atkLosses

    losses = dict(sorted(losses.items(), key=lambda item: item[1], reverse = True))
    kills = dict(sorted(kills.items(), key=lambda item: item[1], reverse = True ))

    tmp = [""]
    tmp += players
    layout = [[sg.Text("Table Entry: Def Losses / Atk Losses", size=(150,1), justification='center')],
                [sg.Text("Attacker", size=(150,1), justification='center')], [sg.Text("Defender"), sg.Table(values=effectiveWins, alternating_row_color='grey',max_col_width=10,  auto_size_columns=False, headings = tmp, num_rows = min(10, len(effectiveWins)))],
                [sg.Text("Losses:")],
                [ sg.Table(values = [[k for k in losses], [losses[k] for k in losses]], num_rows = 2) ],
                [sg.Text("Kills:")],
                [sg.Table(values = [[k for k in kills], [kills[k] for k in kills]], num_rows = 2)]
            ]
    window = sg.Window(title="Best Risk Simulator X-Treme Statistics", layout=layout, margins=(200, 200), background_color=DEFAULTBG)

    while True:
        event, values = window.read()

        if  event == sg.WIN_CLOSED or event == "Escape:9":
            break

    window.close()



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


layout = [[sg.Text('Player:', size =(15, 1)), sg.InputText("Fabi", key = "__PLAYER1")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Marius", key = "__PLAYER2")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Marc", key = "__PLAYER3")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Matthias", key = "__PLAYER4")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Herr v. Samin", key = "__PLAYER5")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Christopher", key = "__PLAYER6")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Polly", key = "__PLAYER7")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Yannik", key = "__PLAYER8")],
 [sg.Text('Player:', size =(15, 1)), sg.InputText("Lena", key = "__PLAYER9")],
 [sg.Button("Confirm", key="__CONFIRMATION BUTTON")]]

window = sg.Window(title="Best Risk Simulator", layout=layout, margins=(200, 200), background_color=DEFAULTBG)
while True:
    event, values = window.read()

    if  event == sg.WIN_CLOSED or event == "Escape:9":
        break
    if event == "__CONFIRMATION BUTTON":
        for i in range(1,10):
            player = "__PLAYER" + str(i)
            name = values[player]
            if len(name) > 1:
                players.append(name)
        break

window.close()



attackers = 1
defenders = 1

layout = [  [sg.Text("Attacker Name", size = (20,1)), sg.Text("Defender Name", size = (20,1))],
            [sg.Listbox( players, size=(20,8), key='__ATTACKER NAME'), sg.Listbox( players, size=(20,8), key='__DEFENDER NAME')],
            [[sg.Text('Attackers', size =(15, 1)), sg.InputText("3", key = "__ATTACKERS"), sg.Button("+", key = "__INC_ATK"), sg.Button("-", key = "__DEC_ATK")],
            [sg.Text('Defenders', size =(15, 1)), sg.InputText("1", key = "__DEFENDERS"), sg.Button("+", key = "__INC_DEF"), sg.Button("-", key = "__DEC_DEF")]],
            [sg.Button("Simulate!")],
            [sg.Button("Show Stats", key = "__SHOW STATS")]
            ]
window = sg.Window(title="Best Risk Simulator", layout=layout, margins=(200, 200), return_keyboard_events=True, background_color=DEFAULTBG)
while True:
    event, values = window.read()

    if  event == sg.WIN_CLOSED:
        break


    if event == "Escape:9":
        pass

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
        gr = GameRecord()
        try:
            gr.attackerName = values["__ATTACKER NAME"][0]
        except:
            gr.attackerName = players[0]
        try:
            gr.defenderName = values["__DEFENDER NAME"][0]
        except:
            gr.defenderName = players[0]
        gr.attackers = attackers
        gr.defenders = defenders
        attackers, defenders = simulate(attackers, defenders)
        gr.atkLosses = gr.attackers - attackers
        gr.defLosses = gr.defenders - defenders
        GameHistory.append(gr)
    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2, "Return:36"):
        attackers, defenders = simulate(attackers, defenders)

    if event == "__SHOW STATS":
        showStatWindow()

    window["__ATTACKERS"].Update(attackers)
    window['__DEFENDERS'].Update(defenders)


for gr in GameHistory:
    print(gr)
window.close()
