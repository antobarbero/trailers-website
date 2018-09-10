from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class MoviesTrailersAPIView(APIView):
	"""API View to retrieve the movies and its trailers."""
	renderer_classes = JSONRenderer,

	def get(self, request):
		return Response({'Hello': 'world'})
