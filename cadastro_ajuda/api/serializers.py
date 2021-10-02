from django.db.models import fields
from rest_framework import serializers
from cadastro_ajuda import models


class CadastroAjudaSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.CadastroAjuda
    fields = '__all__'



