from dataclasses import fields
import email
from pyexpat import model
from rest_framework import serializers
from .models import restframework

class demo_restframe(serializers.ModelSerializer):
    class Meta:
        model=restframework
        # fields=('name','email')
        fields='__all__'