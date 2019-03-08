from django.contrib import admin
from django.urls import path, include
from .views import api_root
from campeonato import views
from django.conf.urls import url
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('', views.HomePageView, "")
# router.register('campeonato/<int:pk>/gerar_grupos/', views.GerarTimesView, 'campeonato-gerar_grupo')



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('^$', api_root),
    # path('', include(router.urls)),
    # url(r'^', include(router.urls)),
    path('', include('campeonato.urls', namespace='campeonato'))
]
