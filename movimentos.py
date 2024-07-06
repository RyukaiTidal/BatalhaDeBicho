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
    def calculoDano(self, TipoPokemonA, PokeAtkLvl, PokeAtkATK, PokeDefDEF):
        Crit = 1
        if TipoPokemonA == self.tipo:
            STAB = 1.5
        else:
            STAB = 1

        PokeCrit = ((2 * PokeAtkLvl * Crit) / 5) + 2
        PAD = ((PokeCrit * self.poder * (PokeAtkATK / PokeDefDEF)) / 50) + 2
        STTR = PAD * STAB * 1 * 1 * 1
        return round(STTR)

    # Definir os textos de ação do Movimento. 1 seg de delay pra Físicos, e 0,5 pra Status.
    def texto(self, pokemontime, pokemonad, golpe):
        ataque = str(golpe)
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

# Classe do Movimento Gust
class Gust(Movement):
    def __init__(self, nome="Gust", tipo="Normal", categoria="Fisico", poder=40, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)


# Classe do Movimento SandAttack
class SandAttack(Movement):
    def __init__(self, nome="Sand Attack", tipo="Normal", categoria="Status", poder=0, acerto=100):
        super().__init__(nome, tipo, categoria, poder, acerto)
