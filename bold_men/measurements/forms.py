from django import forms
from measurements.models import  Measurement


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        exclude = ('user',)


