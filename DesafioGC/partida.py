import random

class Partida():

    def __init__(self, team1, team2):
        self.id = None
        self.team1 = team1
        self.team2 = team2
        self.ganhador = None
        self.rounds_team1 = 0
        self.rounds_team2 = 0
        # return id

    def definir_placar(self, p1, p2):
        if p1 != 16 or p2 != 16:

            self.rounds_team1 = p1
            self.rounds_team2 = p2
            self.team1.jogos += 1
            self.team2.jogos += 1
            self.team1.rounds_ganhos += p1
            self.team2.rounds_ganhos += p2

            if p1 > p2:
                self.ganhador = self.team1
                self.team1.pontos += 1

            else:
                self.ganhador = self.team2
                self.team2.pontos += 1

        else:
            print("Placar errado!!")
            print("{}:{} || {}:{}".format(self.team1, p1, self.team2, p2))

    def simular_partida(self):
        ganhador = random.randint(0, 1)
        if ganhador:
            self.definir_placar(16, random.randint(0, 15))
        else:
            self.definir_placar(random.randint(0, 15), 16)
        # print(self.ganhador)

    def __str__(self):
        return "{} vs {}".format(self.team1, self.team2)
