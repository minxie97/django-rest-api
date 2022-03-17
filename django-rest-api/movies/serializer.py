from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'director', 'description', 'watcher', 'created_at', 'updated_at']
        model = Movie