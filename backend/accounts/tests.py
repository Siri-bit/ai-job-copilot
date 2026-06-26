from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthTests(APITestCase):
    def test_register_and_login(self):
        register_url = reverse("register")
        response = self.client.post(register_url, {
            "username": "testuser",
            "email": "test@example.com",
            "password": "strongpass123",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login_url = reverse("login")
        response = self.client.post(login_url, {
            "username": "testuser",
            "password": "strongpass123",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)