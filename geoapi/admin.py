from django.contrib import admin
from .models import Query, QueryResult

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('cadastre_number', 'latitude', 'longitude', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('cadastre_number', 'latitude', 'longitude')
    ordering = ('-created_at',)

@admin.register(QueryResult)
class QueryResultAdmin(admin.ModelAdmin):
    list_display = ('query', 'result', 'processed_at')
    list_filter = ('result', 'processed_at')
    search_fields = ('query__cadastre_number', 'result')
    ordering = ('-processed_at',)