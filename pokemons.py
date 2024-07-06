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
    def __init__(self, dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2):
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

    # Definir qual ataque vai ser executado:
    def golpes(self, golpe, pokemon):
        match golpe:
            case 1:
                self.ataque(self.golpe1, pokemon)
            case 2:
                self.ataque(self.golpe2, pokemon)

    # Código para Atacar o Pokémon Adversário
    def ataque(self, golpe, pokemon):

        # RNG(acc) Pra ver se o golpe acertou ou não
        acc = random.randint(1,100)
        if acc < golpe.acerto:

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
                    self.golpe1.acerto = round(self.golpe1.acerto * 0.75)
                    self.golpe1.acerto = round(self.golpe2.acerto * 0.75)
                    print(f"A precisão de {pokemon.nome} caiu!")
                    time.sleep(1)

            # Subtrair o dano Calculado.
            self.hp -= Dano

        # Caso o Pokémon Erre o golpe...
        else:
            print(f"...mas ele falhou o golpe...")

# Classe do Charmander
class Charmander(Pokemon):
    def __init__(self, dex=4, nome="Charmander", tipo="Fogo", hp=39, attack=52, defense=43,
                 spc=50, speed=65, level=10, golpe1=Tackle, golpe2=Growl):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2)

# Classe do Pidgey
class Pidgey(Pokemon):
    def __init__(self, dex=16, nome="Pidgey", tipo="Normal", hp=40,
                 attack=45, defense=40, spc=35, speed=56, level=10, golpe1=Gust, golpe2=Sand_Attack):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, level, golpe1, golpe2)
