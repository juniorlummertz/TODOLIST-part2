from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet que fornece automaticamente as ações:
    list, create, retrieve, update, partial_update, destroy.
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def concluir(self, request, pk=None):
        task = self.get_object()
        task.is_done = True
        task.save()
        return Response({'status': 'tarefa concluída', 'id': task.id})
