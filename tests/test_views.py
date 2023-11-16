import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from geoapi.models import Query, QueryResult
from geoapi.serializers import QuerySerializer, QueryResultSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_query(api_client):
    url = reverse('query')
    data = {
        'cadastre_number': '123456789',
        'latitude': '55.7558',
        'longitude': '37.6173'
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_202_ACCEPTED
    assert Query.objects.count() == 1

@pytest.mark.django_db
def test_create_query_invalid_data(api_client):
    url = reverse('query')
    data = {
        'cadastre_number': '123456789',
        'latitude': 'invalid',
        'longitude': '37.6173'
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Query.objects.count() == 0

@pytest.mark.django_db
def test_get_query_result(api_client):
    query = Query.objects.create(
        cadastre_number='123456789',
        latitude='55.7558',
        longitude='37.6173'
    )
    query_result = QueryResult.objects.create(
        query=query,
        result=True
    )
    url = reverse('result', args=[query.cadastre_number])

    response = api_client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['result'] is True

@pytest.mark.django_db
def test_get_query_result_not_found(api_client):
    url = reverse('result', args=['non_existent_cadastre_number'])

    response = api_client.get(url, format='json')

    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_get_query_history(api_client):
    query1 = Query.objects.create(
        cadastre_number='123456789',
        latitude='55.7558',
        longitude='37.6173'
    )
    query2 = Query.objects.create(
        cadastre_number='987654321',
        latitude='55.7558',
        longitude='37.6173'
    )
    url = reverse('history')

    response = api_client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_query_history_by_cadastre_number(api_client):
    query1 = Query.objects.create(
        cadastre_number='123456789',
        latitude='55.7558',
        longitude='37.6173'
    )
    query2 = Query.objects.create(
        cadastre_number='123456789',
        latitude='55.7558',
        longitude='37.6173'
    )
    url = reverse('history_by_number', args=['123456789'])

    response = api_client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

def test_ping(api_client):
    url = reverse('ping')

    response = api_client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'Сервер доступен'
