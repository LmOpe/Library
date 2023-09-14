from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Django for APIS",
            subtitle = "Build web APIS with python and Django",
            author = "William S. Vincent",
            isbn = "2837462781923",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK),
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)