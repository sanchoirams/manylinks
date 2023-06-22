from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=50)
    descricao = models.CharField(verbose_name='Descrição', max_length=70,
                                 blank=True, default='')
    url = models.URLField(verbose_name='URL', help_text='Informe a URL de destino')
    usuario = models.ForeignKey(User, verbose_name='Usuário',
                                on_delete=models.CASCADE)
    clique = models.PositiveIntegerField(verbose_name='Cliques', default=0)
    visualizacao = models.PositiveIntegerField(verbose_name='Visualização', default=0)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.titulo
