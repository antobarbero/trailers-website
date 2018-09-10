from django.conf.urls import url
from .views import SearchView

app_name = 'website'

urlpatterns = [
    url(r'^$', SearchView.as_view(), name='search'),
]
