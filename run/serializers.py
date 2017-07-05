from rest_framework import serializers

from run.models import Person, Trening


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class TreningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trening
        exclude = ['added_date']
