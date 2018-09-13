from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import omdb, youtube


class MoviesTrailersAPIView(APIView):
    """API View to retrieve the movies and its trailers."""
    renderer_classes = JSONRenderer,

    def get(self, request):
        key_words = request.query_params.get('q')
        result = self._merge_responses(key_words)

        return Response(result)

    def _merge_responses(self, key_words):
        """
        Merge the apis data and returns a dict with the data of movies
        and its trailers.
        """
        movies = omdb.get_movies(key_words)

        for movie in movies:
            trailers_ids = youtube.get_trailers(movie.get('Title'))
            movie.update({'trailers': trailers_ids})

        return movies
