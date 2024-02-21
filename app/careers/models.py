from django.db import models
from rest_framework import serializers


class CareerModel(models.Model):
    created_datetime = models.DateTimeField(null=False, auto_now_add=True)

    username = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    author_ip = models.CharField(max_length=255, null=False, blank=False)


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerModel
        fields = '__all__'
        read_only_fields = ('id', 'created_datetime',)


class CareerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerModel
        fields = '__all__'
        read_only_fields = ('id', 'created_datetime', 'username', 'author_ip',)
