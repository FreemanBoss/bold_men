from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout
from django import forms
from django.forms.models import inlineformset_factory
from fabrics.models import  Fabric, FabricImage


class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        exclude = ()
        

class FabricImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(attrs={'multiple':True, 'type':'File'}))
    class Meta:
        model = FabricImage
        # To handle the fabric id in the view
        exclude = ('fabric', )


        


# FabricImageFormSet = inlineformset_factory(Fabric, FabricImage, form=forms.ModelForm, fields=['image'], extra=1, can_delete=True)
