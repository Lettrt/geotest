from rest_framework import serializers
from .models import Query, QueryResult

class QuerySerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        coerce_to_string=False
    )
    longitude = serializers.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        coerce_to_string=False
    )

    class Meta:
        model = Query
        fields = ['cadastre_number', 'latitude', 'longitude', 'created_at']


class QueryResultSerializer(serializers.ModelSerializer):
    query = QuerySerializer(read_only=True)
    
    class Meta:
        model = QueryResult
        fields = ['id', 'query', 'result', 'processed_at']
