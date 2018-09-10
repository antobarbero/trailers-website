import json

import requests
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class OMDb:
    """Class to call Open Movie Database API for movies search."""
    base_url = 'http://www.omdbapi.com/'
    api_key = '28e7ad89'

    @classmethod
    def get_movies(cls, search_words):
        """Returns a list of movies that matches with the search word."""
        params = {
            'apikey': cls.api_key,
            's': search_words
        }

        response = requests.get(cls.base_url, params=params)

        if response.ok:
            dict_response = json.loads(response.text)
            movies_result = dict_response.get('Search')
        else:
            raise Http404

        return movies_result


class MoviesTrailersAPIView(OMDb, APIView):
    """API View to retrieve the movies and its trailers."""
    renderer_classes = JSONRenderer,

    def get(self, request):
        search_words = request.query_params.get('s')
        response_dict = self.get_movies(search_words)
        return Response(response_dict)
