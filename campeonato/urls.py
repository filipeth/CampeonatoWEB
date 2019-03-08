from campeonato import views
from django.urls import path
from django.conf.urls import url, include

# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# # router.register('', views.HomePageView.as_view(), 'homeview')
# router.register(r'campeonato/(?P<pk_eu>\d+)/gerar_grupos/$', views.GerarTimesView, 'campeonato-gerar_grupo')

app_name = "campeonato"

urlpatterns = [
    path('', views.HomePageView.as_view()),
    url(r'campeonato/(?P<pk_eu>\d+)/gerar_grupos/$', views.GerarTimesView, name='campeonato-gerar_grupo'),
    path('campeonato/', views.CampeonatoList.as_view(), name='campeonato-list'),
    path('campeonato/<int:pk>/', views.CampeonatoDetail.as_view(), name='campeonato-detail'),
    # path('campeonato/<int:pk>/gerar_grupos/', views.GerarTimesView.as_view(), name='campeonato-gerar_grupo'),
    path('campeonato/time/', views.TeamList.as_view(), name='time-list'),
    path('campeonato/time/<int:pk>/', views.TeamDetail.as_view(), name='time-detail'),
    path('campeonato/partida/', views.PartidaList.as_view(), name='partida-list'),
    path('campeonato/partida/<int:pk>/', views.PartidaDetail.as_view(), name='partida-detail'),
    path('campeonato/grupo/', views.GrupoList.as_view(), name='grupo-list'),
    path('campeonato/grupo/<int:pk>/', views.GrupoDetail.as_view(), name='grupo-detail'),
]