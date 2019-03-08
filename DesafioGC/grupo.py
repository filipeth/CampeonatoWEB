import json
from DesafioGC.partida import Partida

class Grupo():
    def __init__(self, name):
        self.name = name
        self.id = None
        self.teams = []
        self.jogos = []
        self.max = 5

    def add_team(self, team):
        if self.max <= 0:
            print("Grupo já contem 5 times")
        else:
            self.teams.append(team)
            self.max -= 1

    def imprimir_tabela(self):
        print("TABELA {}".format(self.name))
        for team in self.teams:

            print("Time: {}, Jogos:{}, Pontos:{}, Rounds Ganhos:{}".format(team.name, team.jogos, team.pontos, team.rounds_ganhos))

    def grupo_json(self):
        print(json.dumps(self.teams))

    def gerar_jogos(self):
        for i in range(len(self.teams)):
            for j in range(i+1, len(self.teams)):
                # print("{}X{}".format(i, j))
                self.jogos.append(Partida(self.teams[i], self.teams[j]))
        # for jogo in self.jogos:
        #     print(jogo)

    def simular_partidas(self):
        for jogo in self.jogos:
            jogo.simular_partida()

    def atualizar_tabela(self):
        self.teams.sort(key=lambda x: (x.pontos, x.rounds_ganhos), reverse=True)
        self.imprimir_tabela()

    def __str__(self):
        return self.name
