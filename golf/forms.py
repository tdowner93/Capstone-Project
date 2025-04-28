from django import forms
from .models import ScoreEntry

from django import forms
from .models import ScoreEntry

class ScoreEntryForm(forms.ModelForm):
    class Meta:
        model = ScoreEntry
        fields = ['hole_number', 'strokes', 'putts', 'green_in_regulation', 'fairways_hit', 'up_and_down']

    hole_number = forms.IntegerField()
    strokes = forms.IntegerField()
    putts = forms.IntegerField()
    green_in_regulation = forms.BooleanField(required=False)
    fairways_hit = forms.BooleanField(required=False)
    up_and_down = forms.BooleanField(required=False)