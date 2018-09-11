from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import omdb, youtube


class MoviesTrailersAPIView(APIView):
    """API View to retrieve the movies and its trailers."""
    renderer_classes = JSONRenderer,

    def get(self, request):

        key_words = request.query_params.get('q')
        movies = omdb.get_movies(key_words)

        for movie in movies:
            trailers = youtube.get_trailers(movie.get('Title'))
            movie.update({'yt_trailers_ids': [
                trailer['id']['videoId'] for trailer in trailers
            ]})

        return Response(movies)
