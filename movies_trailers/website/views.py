from django.views.generic import FormView

from .forms import SearchForm


class SearchView(FormView):
    """Manage the search of movies."""
    form_class = SearchForm
    template_name = 'website/index.html'
