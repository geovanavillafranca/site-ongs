from rest_framework import viewsets
from cadastro_ajuda.api import serializers
from cadastro_ajuda import models


class CadastroAjudaViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CadastroAjudaSerializer
  
  # é todos os campos do models
  queryset = models.CadastroAjuda.objects.all()
