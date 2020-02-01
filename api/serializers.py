from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Complain

class complainSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('Complain')
    
    class Meta:
        model = Complain
        fields = '__all__'

    def Complain(self,wall): 
         user1 = wall.user.username
         return user1
