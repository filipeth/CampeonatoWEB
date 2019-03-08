from DesafioGC.team import Team
from DesafioGC.grupo import Grupo
from DesafioGC.partida import Partida


import random


class Campeonato():

    def __init__(self):
        self.name = "campeonato"
        self.times = []
        self.grupos = []
        self.num_grupos = 16
        self.num_times = 80
        self.gerar_times()
        self.gerar_grupos()
        self.simular_grupos()
        self.gerar_32()
        self.simular_32()
        self.gerar_16()
        self.simular_16()
        self.gerar_8()
        self.simular_8()
        self.gerar_4()
        self.simular_4()
        self.simular_final()

    def gerar_times(self):
        for i in range(self.num_times):
            self.times.append(Team("Time{}".format(i + 1)))

        random.shuffle(self.times)

    def gerar_grupos(self):
        j = 0
        heap = 5
        for i in range(self.num_grupos):
            self.grupos.append(Grupo("GRUPO-{}".format(i + 1)))
            for time in self.times[j:j + heap]:
                self.grupos[i].add_team(time)
            j += heap
            self.grupos[i].gerar_jogos()
        print("Campeonato criado com {} times e {} grupos.".format(self.num_times, self.num_grupos))

    def simular_grupos(self):
        for grupo in self.grupos:
            grupo.simular_partidas()
            grupo.atualizar_tabela()

    def gerar_32(self):
        self.melhor_32 = []
        self.jogos_32 = []

        for grupo in self.grupos:
            self.melhor_32.append(grupo.teams[0])
            self.melhor_32.append(grupo.teams[1])
        random.shuffle(self.melhor_32)
        for i in range(0, 32, 2):
            self.jogos_32.append(Partida(self.melhor_32[i], self.melhor_32[i + 1]))

    def simular_32(self):
        self.melhor_16 = []
        for jogo in self.jogos_32:
            jogo.simular_partida()
            self.melhor_16.append(jogo.ganhador)

    def gerar_16(self):
        self.jogos_16 = []
        for i in range(0, 16, 2):
            self.jogos_16.append(Partida(self.melhor_16[i], self.melhor_16[i + 1]))

    def simular_16(self):
        self.melhor_8 = []
        for jogo in self.jogos_16:
            jogo.simular_partida()
            self.melhor_8.append(jogo.ganhador)

    def gerar_8(self):
        self.jogos_8 = []
        for i in range(0, 8, 2):
            self.jogos_8.append(Partida(self.melhor_8[i], self.melhor_8[i + 1]))

    def simular_8(self):
        self.melhor_4 = []
        for jogo in self.jogos_8:
            jogo.simular_partida()
            self.melhor_4.append(jogo.ganhador)

    def gerar_4(self):
        self.jogos_4 = []
        for i in range(0, 4, 2):
            self.jogos_4.append(Partida(self.melhor_4[i], self.melhor_4[i + 1]))

    def simular_4(self):
        self.final = []
        for jogo in self.jogos_4:
            jogo.simular_partida()
            self.final.append(jogo.ganhador)

    def simular_final(self):
        print("FINAL")
        self.partida_final = Partida(self.final[0], self.final[1])
        print(self.partida_final)
        self.partida_final.simular_partida()
        print("Campeao {}".format(self.partida_final.ganhador))
