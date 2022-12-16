from rest_framework import serializers

from .models import Consult


class EnvioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Consult
        fields = ('id', 'para', 'titulo', 'texto')