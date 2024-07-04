
class Movement:
    def __init__(self, nome, tipo, categoria, poder, acerto):
        self.nome = nome
        self.tipo = tipo
        self.categ = categoria
        self.poder = poder
        self.acerto = acerto

    def calculoDano(self,TipoPokemonA,PokeAtkLvl,PokeAtkATK,PokeDefDEF):
        Crit = 1
        if TipoPokemonA == self.tipo:
            STAB = 1.5
        else:
            STAB = 1
        PokeCrit =  ((2*PokeAtkLvl*Crit)/5)+2
        PAD = ((PokeCrit * self.poder * (PokeAtkATK/PokeDefDEF))/50)+2
        STTR = PAD * STAB * 1 * 1 * 1
        return round(STTR)

class Tackle(Movement):
    def __init__(self, nome = "Tackle", tipo = "Normal", categoria = "Fisico", poder = 40, acerto = 100):
        super().__init__(nome, tipo, categoria, poder, acerto)


class Growl(Movement):
    def __init__(self, nome= "Growl", tipo = "Normal", categoria = "Status", poder = 0, acerto = 100):
        super().__init__(nome, tipo, categoria, poder, acerto)


class Gust(Movement):
    def __init__(self, nome = "Gust", tipo = "Normal", categoria = "Fisico", poder = 40, acerto = 100):
        super().__init__(nome, tipo, categoria, poder, acerto)


class SandAttack(Movement):
    def __init__(self, nome = "Sand Attack", tipo = "Normal", categoria = "Status", poder= 0, acerto = 100):
        super().__init__(nome, tipo, categoria, poder, acerto)