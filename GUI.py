import movimentos
import pokemons
import math
import random

equipe = pokemons.Charmander()
adversario = pokemons.Pidgey()


def hpBar(pokemon):
    vida = float(pokemon.hp)  # Vida Atual (float, pra que a divisão não faça um int)
    maxVida = pokemon.Maxhp  # Máximo de Vida
    vidaIndic = 20  # Indicadores máximos de vida
    math.log10(pokemon.level) // 1 + 1

    hpBar = int((vida / maxVida) * 100)
    indicAtuais = int((hpBar / 100) * vidaIndic)
    vidaRestante = vidaIndic - indicAtuais

    displayNome = " " * vidaRestante
    displayVida = '█' * indicAtuais  # Converte 5 para 5 traços como String: "-----"
    displayRestante = " " * vidaRestante  # Converte 15 para 15 espaços como string: "               "
    porcento = str(int((vida / maxVida) * 100)) + "%"  # Pega a porcentagem como número inteiro:  25%


    print("   ", pokemon.nome, displayNome, "Lv", pokemon.level)
    print("│" + displayVida + displayRestante + "│")  # Printa a barra de vida em texto
    # if pokemon == equipe:
    print(f"         ({int(vida)}/{maxVida} {porcento} )")  # Printa a vida, Máximo de vida, e a Porcentagem


def displayAttackBar(pokemon):
    length1 = max(len(pokemon.nAtaques[0]),len(pokemon.nAtaques[2]))
    length2 = max(len(pokemon.nAtaques[1]),len(pokemon.nAtaques[3]))
    length3 = len(pokemon.nAtaques[0]) - len(pokemon.nAtaques[2])
    length4 = len(pokemon.nAtaques[2]) - len(pokemon.nAtaques[0])

    displayUpperBar = "┌" + "─" * length1 + "─┬─" + "─" * length2 + "┐"
    displayAtaques1 = "│" + pokemon.nAtaques[0] +" " * length4 + " │ " + pokemon.nAtaques[1] + " " * len(pokemon.nAtaques[3]) +"│"
    displayMiddleBar = "├" + "─" * length1 + "─┼─" + "─" * length2 + "┤"
    displayAtaques2 = "│" + pokemon.nAtaques[2]+ " " * length3 + " │ " + pokemon.nAtaques[3] + " " * len(pokemon.nAtaques[1])  + "│"
    displayLowerBar = "└" + "─" * length1 + "─┴─" + "─" * length2 + "┘"

    print(displayUpperBar)
    print(displayAtaques1)
    print(displayMiddleBar)
    print(displayAtaques2)
    print(displayLowerBar)


def displayOptionsBar():
    displayUpperBar = "┌" + "────────" + "─┬─" + "────────" + "┐"
    displayAtaques =  "│" + "1.Atacar" + " │ " + "2.Correr" + "│"
    displayLowerBar = "└" + "────────" + "─┴─" + "────────" + "┘"

    print(displayUpperBar)
    print(displayAtaques)
    print(displayLowerBar)


def battleUI():
    hpBar(adversario)
    print(' \n' *5)
    hpBar(equipe)
    print('\n','─'*30)



def select():

    print(f"\nO que {equipe.nome} irá fazer?\n")
    displayOptionsBar()
    choice = int(input(">"))
    if choice == 1:
        displayAttackBar(equipe)
        choice = int(input(">"))
        if choice == 1 or choice == 2 or choice  == 3 or choice == 4:
            validar = equipe.validarGolpe(choice)
            if validar == False:
                pass
            else:
                moveadversario = random.randint(1, 2)
                if equipe.speed > adversario.speed:
                    print('\n', '─' * 30)
                    equipe.selectGolpes(choice, adversario) # Charmander
                    print()
                    adversario.selectGolpes(moveadversario, equipe) # Pidgey
                else:
                    print('\n', '─' * 30)
                    adversario.selectGolpes(moveadversario, equipe)
                    print()
                    equipe.selectGolpes(choice, adversario)
        else:
            pass
        condV = vitoria()
    elif choice == 2:
        print("Você pegou o seu pokémon e fugiu de medo...")
        condV = False
    else:
        condV = True
    return condV

def battleUI():
    hpBar(adversario)
    print(' \n' *5)
    hpBar(equipe)
    print('\n','─'*30)
    return select()

def vitoria():
    if equipe.hp < 1:
        print()
        hpBar(adversario)
        print(' \n' * 5)
        hpBar(equipe)
        print('\n', '─' * 30)
        print(f"{equipe.nome} Está incapacitado e não pode mais lutar!")
        return False
    elif adversario.hp < 1:
        print()
        hpBar(adversario)
        print(' \n' * 5)
        hpBar(equipe)
        print('\n', '─' * 30)
        print(f"{adversario.nome} Está incapacitado e não pode mais lutar!")
        return False
    else:
        return True
