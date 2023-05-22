from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Photo (models.Model):
    
    title = models.CharField(("Titulo"), max_length=50)
    discription = models.CharField(("Descrição"), blank=True, null=True, max_length=500)
    photo = models.ImageField(("Foto"), upload_to='', height_field=None, width_field=None, max_length=None)
    send_date = models.DateTimeField(("Data de Envio"), auto_now_add=True)
    last_modified = models.DateTimeField(("Ultima Alteração"), auto_now=True)
    
    #shared_with = models.ForeignKey(User, verbose_name=("Compartilhado com"), on_delete=models.CASCADE)
    #creator = models.OneToOneField(User, verbose_name=("Criador"), on_delete=models.CASCADE)
    
    verbose_name = 'Photo'
    verbose_name_plural = 'Photos'
    
    def __str__ (self):
        return self.title