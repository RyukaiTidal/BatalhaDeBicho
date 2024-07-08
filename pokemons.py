# Importar movimentos, delay, e random.
import movimentos
import time
import random

# Guardar Movimentos em variáveis

Tackle = movimentos.Tackle()
Gust = movimentos.Gust()
Sand_Attack = movimentos.SandAttack()
Growl = movimentos.Growl()
Ember = movimentos.Ember()


# Classe Construtora Pokémon
class Pokemon():
    def __init__(self, dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2, golpe3, golpe4,
                 ataques):
        self.dex = dex
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special = spc
        self.speed = speed
        self.level = level
        self.golpe1 = golpe1
        self.golpe2 = golpe2
        self.golpe3 = golpe3
        self.golpe4 = golpe4
        self.Maxhp = hp
        self.nAtaques = ataques

    # Definir qual ataque vai ser executado:
    def selectGolpes(self, Ataque, pokemon):  # Indice do Pokemon, Pokémon que será atacado.
        match Ataque:
            case 1:

                self.ataque(self.golpe1, pokemon)

            case 2:

                self.ataque(self.golpe2, pokemon)

            case 3:

                self.ataque(self.golpe3, pokemon)

            case 4:

                self.ataque(self.golpe4, pokemon)

            case _:
                pass

    # Código para Atacar o Pokémon Adversário
    def ataque(self, golpe, pokemon):  # Golpe utilizado, Pokemon adversário
        # RNG(acc) Pra ver se o golpe acertou ou não
        acc = random.randint(1, 100)
        if acc <= golpe.acerto:

            # Calcular dano
            Dano = golpe.calculoDano(self, pokemon)

            # Executar Texto da Ação
            golpe.texto(self.nome, pokemon.nome, golpe)

            # Adicional para golpes de Efeito (Se for efeito, o dano será 0.)
            match golpe.nome:

                case "Growl":

                    Dano = 0
                    pokemon.defense = round(pokemon.defense * 0.75)
                    print(f"\nA defesa de {pokemon.nome} caiu!")
                    time.sleep(1)

                case "Sand Attack":
                    Dano = 0
                    pokemon.golpe1.acerto = round(pokemon.golpe1.acerto * 0.75)
                    pokemon.golpe2.acerto = round(pokemon.golpe2.acerto * 0.75)
                    print(f"\nA precisão de {pokemon.nome} caiu!")
                    time.sleep(1)

            # Subtrair o dano Calculado.
            pokemon.hp -= Dano
            if pokemon.hp <0:
                pokemon.hp = 0

        # Caso o Pokémon Erre o golpe...
        else:
            erros = ["...mas ele falhou o golpe...", "...mas ele perdeu forças...", "...mas ele escorrega e erra...",
                     "...mas ele erra por um triz!", "...mas ele não consegue..."]
            x = random.randint(0, len(erros) - 1)
            print(f"{self.nome} Tenta usar {golpe.nome}...")
            time.sleep(0.5)
            print(erros[x])

    def validarGolpe(self, ataque):
        match ataque:
            case 1:
                if self.golpe1 is None:
                    return False
                else:
                    return True

            case 2:
                if self.golpe2 is None:
                    return False
                else:
                    return True
            case 3:
                if self.golpe3 is None:
                    return False
                else:
                    return True
            case 4:
                if self.golpe4 is None:
                    return False
                else:
                    return True


# Classe do Charmander
class Charmander(Pokemon):

    def __init__(self, dex=4, nome="Charmander", tipo="Fogo", hp=39, attack=52, defense=43,
                 spc=50, speed=65, level=10, golpe1=Tackle, golpe2=Growl, golpe3=Ember, golpe4=None,
                 ataques=["1. Tackle", "2.Growl", "3. Ember", ""]):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2, golpe3, golpe4,
                         ataques)
        self.golpe3 = Ember


# Classe do Pidgey
class Pidgey(Pokemon):
    def __init__(self, dex=16, nome="Pidgey", tipo="Normal", hp=40,
                 attack=45, defense=40, spc=35, speed=56, level=10, golpe1=Gust, golpe2=Sand_Attack, golpe3=None,
                 golpe4=None, ataques=["Gust", "Sand Attack", "", ""]):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2, golpe3, golpe4,
                         ataques)


