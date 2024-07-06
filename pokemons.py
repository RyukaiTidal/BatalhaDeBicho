# Importar movimentos, delay, e random.
import movimentos
import time
import random

# Guardar Movimentos em variáveis

Tackle = movimentos.Tackle()
Gust = movimentos.Gust()
Sand_Attack = movimentos.SandAttack()
Growl = movimentos.Growl()


# Classe Construtora Pokémon
class Pokemon():
    def __init__(self, dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2,ataques):
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
        self.Maxhp = hp
        self.nAtaques = ataques

    # Definir qual ataque vai ser executado:
    def selectGolpes(self,Ataque, pokemon):
        match Ataque:
            case 1:
                self.ataque(self.golpe1, pokemon)
            case 2:
                self.ataque(self.golpe2, pokemon)
            case _:
                print("ErRo")

    # Código para Atacar o Pokémon Adversário
    def ataque(self, golpe, pokemon):

        # RNG(acc) Pra ver se o golpe acertou ou não
        acc = random.randint(1, 100)
        print(acc)
        if acc <= golpe.acerto:

            # Calcular dano
            Dano = golpe.calculoDano(self.tipo, self.level, self.attack, pokemon.defense)

            # Executar Texto da Ação
            golpe.texto(self.nome, pokemon.nome, golpe.nome)

            # Adicional para golpes de Efeito (Se for efeito, o dano será 0.)
            match golpe.nome:

                case "Growl":

                    Dano = 0
                    pokemon.defense = round(pokemon.defense * 0.75)
                    print(f"A defesa de {pokemon.nome} caiu!")
                    time.sleep(1)

                case "Sand Attack":
                    Dano = 0
                    pokemon.golpe1.acerto = round(pokemon.golpe1.acerto * 0.75)
                    pokemon.golpe2.acerto = round(pokemon.golpe2.acerto * 0.75)
                    print(f"A precisão de {pokemon.nome} caiu!")
                    time.sleep(1)

            # Subtrair o dano Calculado.
            self.hp -= Dano

        # Caso o Pokémon Erre o golpe...
        else:
            erros = ["...mas ele falhou o golpe...","...mas ele perdeu forças...","...mas ele escorrega e erra...","...mas ele erra por um triz!","...mas ele não consegue..."]
            x = random.randint(0, len(erros))
            print(f"{self.nome} Tenta usar {golpe.nome}...")
            time.sleep(0.5)
            print(erros[x])


# Classe do Charmander
class Charmander(Pokemon):
    def __init__(self, dex=4, nome="Charmander", tipo="Fogo", hp=39, attack=52, defense=43,
                 spc=50, speed=65, level=10, golpe1=Tackle, golpe2=Growl,ataques=["1. Tackle","2.Growl"]):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2,ataques)



# Classe do Pidgey
class Pidgey(Pokemon):
    def __init__(self, dex=16, nome="Pidgey", tipo="Normal", hp=40,
                 attack=45, defense=40, spc=35, speed=56, level=10, golpe1=Gust, golpe2=Sand_Attack,ataques = ["Gust","Sand Attack"]):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2, ataques)
