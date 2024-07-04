import movimentos

Tackle = movimentos.Tackle()
Gust = movimentos.Gust()
Sand_Attack = movimentos.SandAttack()
Growl = movimentos.Growl()
class Pokemon():
    def __init__(self, dex, nome, tipo, hp, attack, defense, spc, speed, moves, level):
        self.dex = dex
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special = spc
        self.speed = speed
        self.moves = moves
        self.level = level

    def ataque(self,pokemon):
        Dano = Tackle.calculoDano(self.tipo,self.level,self.attack,pokemon.defense)
        print(Dano)
class Charmander(Pokemon):
    def __init__(self, dex = 4, nome = "Charmander", tipo = "Fogo", hp = 39, attack = 52, defense = 43,
                 spc = 50, speed = 65, moves = ["Scratch", "Growl"], level = 10):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, moves, level)


class Pidgey(Pokemon):
    def __init__(self, dex = 16, nome = "Pidgey", tipo = "Normal", hp = 40,
                 attack  = 45, defense = 40, spc = 35, speed = 56, moves = ["Gust", "Sand Attack"],
                 level = 10):
        super().__init__(dex, nome, tipo, hp, attack, defense, spc, speed, moves, level)