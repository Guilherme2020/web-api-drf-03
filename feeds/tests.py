from django.test import TestCase

from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import *


# Create your tests here.


class ResetDataTest(APITestCase):
    def test_reset_data(self):
        url = reverse('reset-data')
        response = self.client.get(url,format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

class UserTestCase(APITestCase):
    pass
