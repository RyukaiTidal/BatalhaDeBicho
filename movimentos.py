# Pra delay de tempo
import time


# Classe Construtora do Movimento
class Movement:
    def __init__(self, nome, tipo, categoria, poder, acerto):
        self.nome = nome
        self.tipo = tipo
        self.categ = categoria
        self.poder = poder
        self.acerto = acerto

    # Parte mais complicada do Projeto, Calcular o dano.
    # Descrição das coisas são encontradas na Bulbapedia.
    # Formula do Cálculo de dano: https://bulbapedia.bulbagarden.net/wiki/Damage#Generation_I
    def calculoDano(self, PokemonA, PokemonB):
        global AD
        Crit = 1
        STAB = 1
        match self.categ:
            case "Fisico":
                AD = (PokemonA.attack / PokemonB.defense)
            case "Especial":
                AD = (PokemonA.special / PokemonB.special)
            case "Status":
                AD = 0

        PokeCrit = ((2 * PokemonA.level * Crit) / 5) + 2
        PAD = ((PokeCrit * self.poder * AD) / 50) + 2
        STTR = PAD * STAB * 1 * 1 * 1
        return int(STTR)

    # Definir os textos de ação do Movimento. 1 seg de delay pra Físicos, e 0,5 pra Status.
    def texto(self, pokemontime, pokemonad, golpe):
        ataque = golpe.nome
        match ataque:
            case "Tackle":
                print(f"{pokemontime} foi pra cima de {pokemonad} e lhe deu uma Investida!")
                time.sleep(1)
            case "Growl":
                print(f"{pokemontime} soltou um forte ruido, fazendo {pokemonad} tremer de medo.")
                time.sleep(0.5)
            case "Gust":
                print(f"{pokemontime} soltou uma rajada de vento contra {pokemonad}, machucando-o.")
                time.sleep(1)
            case "Sand Attack":
                print(f"{pokemontime} pega um pouco de areia, e joga nos olhos de {pokemonad}!")
                time.sleep(0.5)
            case "Ember":
                print(f"{pokemontime} solta chamas de sua boca, atingindo {pokemonad}!")
                time.sleep(0.5)
            case _:
                print(f"Tá dando algum erro, patrão")


# Classe do Movimento Tackle
class Tackle(Movement):
    def __init__(self, nome="Tackle", tipo="Normal", categoria="Fisico", poder=40, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)


# Classe do Movimento Growl
class Growl(Movement):
    def __init__(self, nome="Growl", tipo="Normal", categoria="Status", poder=0, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)


# Classe do Movimento Ember
class Ember(Movement):
    def __init__(self, nome="Ember", tipo="Fogo", categoria="Especial", poder=40, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)


# Classe do Movimento Gust
class Gust(Movement):
    def __init__(self, nome="Gust", tipo="Normal", categoria="Fisico", poder=40, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)


# Classe do Movimento SandAttack
class SandAttack(Movement):
    def __init__(self, nome="Sand Attack", tipo="Normal", categoria="Status", poder=0, acerto=80):
        super().__init__(nome, tipo, categoria, poder, acerto)
