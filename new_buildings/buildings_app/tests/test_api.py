# from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import BuildingsBase


class AccountTests(APITestCase):
    def test_create_building(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('buildings_list')
        data = {'year': 2020,
                'area': 'Рассказово2',
                'residence_name': 'Рассказово',
                'builder': 'Империал'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BuildingsBase.objects.count(), 1)
        self.assertEqual(BuildingsBase.objects.get().year, 2020)
        self.assertEqual(response.data, {'id': 1,
                                         'year': 2020,
                                         'area': 'Рассказово2',
                                         'residence_name': 'Рассказово',
                                         'builder': 'Империал'})

    def duplicate_test(self):
        url = reverse('buildings_list')
        data = {'year': 2020,
                'area': 'Рассказово2',
                'residence_name': 'Рассказово',
                'builder': 'Империал'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BuildingsBase.objects.count(), 3)
        self.assertEqual(BuildingsBase.objects.get().year, 2020)
