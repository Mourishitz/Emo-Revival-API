from django.urls import path
from .views import Create, Read, List

crudpatterns = [
    path('create/', Create.as_view({'post': 'create'})),
    path('retrieve/<id>/', Read.as_view({'get': 'retrieve'})),
    path('list/', List.as_view({'get': 'list'})),
]

urlpatterns = crudpatterns
