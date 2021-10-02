from django.db import models

# Create your models here.

class CadastroAjuda(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.CharField(max_length=255, blank=True, null=True)
  situacao = models.CharField(max_length=30, blank=True, null=True)
  conta_bancaria = models.CharField(max_length=25, blank=True, null=True)
  contato_telefone = models.CharField(max_length=20, blank=True, null=True)
  contato_email = models.CharField(max_length=30, blank=True, null=True)
  data_criacao = models.DateField(auto_now_add=True)

