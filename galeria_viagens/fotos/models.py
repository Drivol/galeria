from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    local = models.CharField(max_length=200, blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='viagens/')
    data_viagem = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
