from django import forms


class SearchForm(forms.Form):
    """Form for movies searching."""
    search_word = forms.CharField(max_length=64, min_length=1)
