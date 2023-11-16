import pytest
from django.utils import timezone
from geoapi.models import Query, QueryResult

@pytest.mark.django_db
def test_create_query_instance():
    query = Query(
        cadastre_number="123456789",
        latitude=55.7558,
        longitude=37.6173,
        created_at=timezone.now(),
    )
    query.save()
    query_from_db = Query.objects.get(pk=query.pk)
    assert query_from_db.cadastre_number == "123456789"
    assert pytest.approx(float(query_from_db.latitude), 0.0001) == 55.7558
    assert pytest.approx(float(query_from_db.longitude), 0.0001) == 37.6173

@pytest.mark.django_db
def test_create_queryresult_instance():
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
    query_result_from_db = QueryResult.objects.get(pk=query_result.pk)
    assert query_result_from_db.query == query
    assert query_result_from_db.result is True
