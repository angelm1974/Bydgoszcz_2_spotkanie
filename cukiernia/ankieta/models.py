from pyexpat import model
from django.db import models

# Create your models here.
class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=255)
    data_pub=models.DateTimeField('data publikacji')
    obraz=models.CharField(max_length=255,default='brak.jpg')
    
    def __str__(self):
        return self.tekst_pytania.upper()
    
    class Meta:
        verbose_name ='Pytanie'
        verbose_name_plural ='Pytania'

class Odpowiedz(models.Model):
    pytanie=models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    tekst_odpowiedzi=models.CharField(max_length=255)
    glosy=models.IntegerField(default=0)
    
    def __str__(self):
        return self.tekst_odpowiedzi.upper()
    
    class Meta:
        verbose_name ='Odpowiedź'
        verbose_name_plural ='Odpowiedzi'