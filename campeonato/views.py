from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets


from campeonato.models import Campeonato, Team, Partida, Grupo
from .serializers import CampeonatoSerializer, GrupoSerializer, PartidaSerializer, TeamSerializer


class GerarTimesView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        id = self.kwargs['pk_eu']
        camp = Campeonato.objects.get(id=id)

        for i in range(camp.num_times):
            Team.objects.update_or_create(nome="Time{}".format(i + 1), campeonato=camp)
            # t.save()

        # for i in range(camp.num_grupos):
        #     Grupo.objects.update_or_create(nome="Grupo-{}".format(i + 1), campeonato=camp)

        # Grupo.objects.update_or_create(nome="Melhor-32", campeonato=camp)
        # Grupo.objects.update_or_create(nome="Melhor-16", campeonato=camp)
        # Grupo.objects.update_or_create(nome="Melhor-8", campeonato=camp)
        # Grupo.objects.update_or_create(nome="Melhor-4", campeonato=camp)
        # Grupo.objects.update_or_create(nome="Final", campeonato=camp)

        # lista_times = list(Team.objects.all().filter(campeonato=camp.id).values_list('id', flat=True))
        # random.shuffle(lista_times)
        # print(lista_times)
        print("Errouuuu.")
        return Team.objects.all().filter(campeonato=camp.id)


class HomePageView(generics.ListCreateAPIView):
    def get(self, request, **kwargs):
        nome = request.GET.get('camp_nome')
        if nome is None:
            return render(request, 'index.html', context={"nome": None, "url": ""})
        else:
            nome_camp = str(nome)
            camp = Campeonato.objects.get(nome=nome_camp)
            url = "campeonato/{}/gerar_grupos".format(camp.id)
            return render(request, 'index.html', context={"nome": nome_camp, "url": url})


class CampeonatoList(generics.ListCreateAPIView):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

    def perform_create(self, serializer):
        serializer.save()


class CampeonatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

    def get_queryset(self):
        return Campeonato.objects.all().filter()


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        serializer.save()


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all().filter()


class PartidaList(generics.ListCreateAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

    def perform_create(self, serializer):
        serializer.save()


class PartidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

    def get_queryset(self):
        return Partida.objects.all().filter()


class GrupoList(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

    def perform_create(self, serializer):
        serializer.save()


class GrupoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

    def get_queryset(self):
        return Grupo.objects.all().filter()
