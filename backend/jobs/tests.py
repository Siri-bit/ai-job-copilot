from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class JobDescriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.client.force_authenticate(user=self.user)

    def test_create_and_list_job_description(self):
        response = self.client.post("/api/job-descriptions/", {
            "title": "Backend Developer",
            "company": "Acme Corp",
            "raw_text": "Looking for a Django developer.",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get("/api/job-descriptions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)