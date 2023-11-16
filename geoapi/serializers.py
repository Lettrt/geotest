from rest_framework import serializers
from .models import Query, QueryResult

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'cadastre_number', 'latitude', 'longitude', 'created_at']


class QueryResultSerializer(serializers.ModelSerializer):
    query = QuerySerializer(read_only=True)
    
    class Meta:
        model = QueryResult
        fields = ['id', 'query', 'result', 'processed_at']
