from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskApiTests(APITestCase):
    def test_create_task(self):
        response = self.client.post(
            reverse('task-list'),
            {
                'title': 'Study Django REST Framework',
                'description': 'Review serializers and viewsets',
                'priority': 'HIGH',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().priority, 'HIGH')

    def test_complete_task(self):
        task = Task.objects.create(title='Publish API', priority='MED')

        response = self.client.post(
            reverse('task-concluir', args=[task.id]),
            format='json',
        )

        task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(task.is_done)
