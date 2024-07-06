import pokemons
import math

time = pokemons.Charmander()
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
    if pokemon == time:
        print(f"         ({int(vida)}/{maxVida} {porcento} )")  # Printa a vida, Máximo de vida, e a Porcentagem


def attackBar(pokemon):
    displayUpperBar = "┌"+ "─" * len(pokemon.nAtaques[0]) + "─┬─" + "─" * len(pokemon.nAtaques[1]) + "┐"
    displayAtaques = "│"+ pokemon.nAtaques[0] + " │ " +  pokemon.nAtaques[1] + "│"
    displayLowerBar = "└" + "─" * len(pokemon.nAtaques[0]) + "─┴─" + "─" * len(pokemon.nAtaques[1]) + "┘"

    print(displayUpperBar)
    print(displayAtaques)
    print(displayLowerBar)