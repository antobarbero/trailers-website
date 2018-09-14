from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MoviesSearchAPITestCase(APITestCase):
    """Test case for the search of movies."""

    def setUp(self):
        self.url = reverse('trailers_api:movies_trailers')

    def test_get_response(self):
        """
        Ensure we can get the response from a valid search.
        """
        key_words = 'harry potter'
        response = self.client.get(self.url, {'q': key_words})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_invalid_key_words(self):
        """
        With an invalid key word the result must be empty.
        """
        key_words = 'qwertyuiop'
        response = self.client.get(self.url, {'q': key_words})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('"Error":"Movie not found!"', str(response.content))
