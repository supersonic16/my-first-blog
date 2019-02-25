from django import forms
from .models import Name

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)

    def save(self):
        get_name=Name.objects.create(
        name=self.cleaned_data['name'],
        )
        return get_name
