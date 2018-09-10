from django.conf.urls import url
from .views import MoviesTrailersAPIView

app_name = 'trailers_api'

urlpatterns = [
    url(r'^$', MoviesTrailersAPIView.as_view(), name='movies_trailers'),
]
