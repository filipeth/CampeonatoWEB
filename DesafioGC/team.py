class Team:
    def __init__(self, name):
        self.name = name
        self.id = self.add_to_db(name)
        self.jogos = 0
        self.pontos = 0
        self.rounds_ganhos = 0


    def imprimir_info(self):
        print("Nome-> {} ID-> {}".format(self.name, self.id))

    def add_to_db(self,name):
        id = 1
        return id

    def __str__(self):
        return self.name
