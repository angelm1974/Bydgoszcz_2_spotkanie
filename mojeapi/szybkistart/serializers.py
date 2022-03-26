from django.contrib.auth.models import User, Group
from  .models import Pytanie,Odpowiedz
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['username','email','groups','url']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=['name','url']
        
class PytanieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Pytanie
        fields=['tekst_pytania','data_pub','obraz']