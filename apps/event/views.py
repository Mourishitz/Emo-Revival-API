from rest_framework import status

from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet


class Create(mixins.CreateModelMixin, GenericViewSet):
    """
    Cadastra Eventos.

    Obrigatório fornecer:

    @data: object {Event} (fornecer em body)
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            event = serializer.save()
            event.save()

            return Response({'message': 'event created successfully',
                             'event': serializer.data,
                             }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class List(mixins.ListModelMixin, GenericViewSet):
    """
    Lista de Eventos.

    Não é obrigatório fornecer nada
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class Read(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Consulta um Evento por ID.

    Obrigatório fornecer:

    @data: object {Event} (fornecer em body)
    @id: string ($uuid) (fornecer em url)
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'
