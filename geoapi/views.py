from rest_framework import status, views
from rest_framework.response import Response
from .models import Query
from .serializers import QuerySerializer
from .tasks import emul_request

class QueryView(views.APIView):
    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save()
            emul_request(query.id)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryView(views.APIView):
    def get(self, request, cadastre_number=None):
        if cadastre_number:
            queries = Query.objects.filter(cadastre_number=cadastre_number)
        else:
            queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)
