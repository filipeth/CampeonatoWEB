from rest_framework import serializers

from .models import Campeonato, Team, Partida, Grupo


class CampeonatoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campeonato
        fields = ('id', 'nome', 'descricao', 'num_grupos', 'num_times')


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'nome', 'campeonato', 'jogos', 'pontos', 'rounds_ganhos')


class PartidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partida
        fields = ('id', 'nome', 'campeonato', 'time1', 'time2', 'ganhador', 'rounds_t1', 'rounds_t2')
        

class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = ('id', 'nome', 'campeonato', 'times', 'jogos')

