from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Query, QueryResult
from .serializers import QueryResultSerializer, QuerySerializer
from .tasks import emul_request

class QueryView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Создать запрос",
        operation_description="Создание нового запроса с указанными данными",
        request_body=QuerySerializer,
        responses={
            202: QuerySerializer(many=False), 
            400: 'Неверный запрос'
        }
        
    )
    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save()
            emul_request(query.id)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResultView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Получение резуьтата с сервера",
        operation_description="Для получения результата с сервера",
        manual_parameters=[
            openapi.Parameter(
                name='cadastre_number',
                in_=openapi.IN_PATH,
                description='Введите кадастровый номер для получения результата',
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, cadastre_number):
        try:
            query = Query.objects.filter(cadastre_number=cadastre_number).latest('created_at')
            query_result = QueryResult.objects.filter(query=query).latest('processed_at')
        except (Query.DoesNotExist, QueryResult.DoesNotExist):
            return Response({"message": "Результат не найден"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QueryResultSerializer(query_result)
        return Response(serializer.data)

class HistoryView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Получить историю запросов",
        operation_description="Получить всю историю запросов или по кадастровому номеру",
        
    )
    def get(self, request, cadastre_number=None):
        if cadastre_number:
            queries = Query.objects.filter(cadastre_number=cadastre_number)
        else:
            queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

class PingView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Доступность сервера",
        operation_description="Сделаем вид, что сервер всегда доступен",
        
    )
    def get(self, request):
        return Response({"message": "Сервер доступен"}, status=status.HTTP_200_OK)
