from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    genres = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Movie
        fields = '__all__'
