from django import forms


class addCoordinatesForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
