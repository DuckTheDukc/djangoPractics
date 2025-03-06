from django import forms
from passwordManager.models import EntryPassword

class SearchWebSiteForm(forms.ModelForm):
    class Meta:
        model = EntryPassword
        fields = ['website_name']