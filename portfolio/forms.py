from django import forms


class SearchForm(forms.Form):
    value = forms.CharField()
