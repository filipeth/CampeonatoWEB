from django.db import models


# Create your models here.
class Campeonato(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(default="Um campeonato a ser disputado.", blank=True)
    num_grupos = models.IntegerField(default=16, blank=True)
    num_times = models.IntegerField(default=80, blank=True)

    def __str__(self):
        return self.nome


class Team(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    jogos = models.IntegerField(default=0, blank=True)
    pontos = models.IntegerField(default=0, blank=True)
    rounds_ganhos = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.nome


class Partida(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    time1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="time1")
    time2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="time2")
    ganhador = models.ForeignKey(Team, on_delete=models.PROTECT, default=None, related_name="time_ganhador")
    rounds_t1 = models.IntegerField(default=0)
    rounds_t2 = models.IntegerField(default=0)


class Grupo(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    times = models.ManyToManyField(Team, default=None)
    jogos = models.ManyToManyField(Partida, default=None)

    def __str__(self):
        return self.nome

