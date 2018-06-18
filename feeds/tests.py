from django.test import TestCase

from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from feeds import views


# Create your tests here.
# from feedit.feeds import views


class ApiRootTest(APITestCase,URLPatternsTestCase):

    urlpatterns = [

        path("",views.ApiRoot.as_view()),

    ]

    def test_url(self):

        url = reverse('')
        response = self.client.get(url,format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data),1)


class UserTestCase(APITestCase):

    def test_user(self):
        url = reverse('users')
        response = self.client.get(url,format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEquals(response.status_code,status.HTTP_404_NOT_FOUND)

        self.assertEquals(len(response.data),1)

class ProfileTestCase(APITestCase):


    def test_profile(self):
        url = reverse('profiles')
        response = self.client.get(url,format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(len(response.data), 1)

class CommentTestCase(APITestCase):
    def test_comment(self):
        url = reverse('comments')
        response = self.client.get(url,format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(len(response.data), 1)


class ProfilePostTestCase(APITestCase):

    def test_profile_comment(self):
        url = reverse('profiles-post')
        response = self.client.post(url,format('json'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEquals(len(response.data), 1)
