from django.urls import path
from .views import QueryView, ResultView, PingView, HistoryView

urlpatterns = [
    path('query/', QueryView.as_view(), name='query'),
    path('result/<str:cadastre_number>/', ResultView.as_view(), name='result'),
    path('ping/', PingView.as_view(), name='ping'),
    path('history/', HistoryView.as_view(), name='history'),
    path('history/<str:cadastre_number>/', HistoryView.as_view(), name='history_by_number'),
]