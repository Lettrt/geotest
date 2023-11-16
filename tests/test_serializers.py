import pytest
from django.utils import timezone
from geoapi.models import Query, QueryResult
from geoapi.serializers import QuerySerializer, QueryResultSerializer

@pytest.mark.django_db
def test_query_serializer():
    query = Query(
        cadastre_number="123456789",
        latitude=55.7558,
        longitude=37.6173,
        created_at=timezone.now(),
    )
    query.save()
    serializer = QuerySerializer(query)
    assert serializer.data['cadastre_number'] == "123456789"
    assert pytest.approx(float(serializer.data['latitude']), abs=0.0001) == 55.7558
    assert pytest.approx(float(serializer.data['longitude']), abs=0.0001) == 37.6173

@pytest.mark.django_db
def test_query_result_serializer():
    query = Query(
        cadastre_number="987654321",
        latitude=55.7558,
        longitude=37.6173,
        created_at=timezone.now(),
    )
    query.save()
    query_result = QueryResult(
        query=query,
        result=True,
        processed_at=timezone.now(),
    )
    query_result.save()
    serializer = QueryResultSerializer(query_result)
    assert serializer.data['result'] is True
    assert pytest.approx(float(serializer.data['query']['latitude']), abs=0.0001) == 55.7558
    assert pytest.approx(float(serializer.data['query']['longitude']), abs=0.0001) == 37.6173
