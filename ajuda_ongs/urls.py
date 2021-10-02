from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cadastro_ajuda.api import viewsets as cadastro_ajuda_viewsets


route = routers.DefaultRouter()

route.register(r'cadastro-ajuda', cadastro_ajuda_viewsets.CadastroAjudaViewSet, basename='CasdastroAjuda')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))

    #path('cadastro-ajuda/', include('cadastro_ajuda.urls'))
]
