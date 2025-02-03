from django import forms
from ..models import EntryPassword
class EntryPasswordForm(forms.ModelForm):
    
    class Meta:
        model=EntryPassword
        fields=['website_name', 'website_url', 'username', 'password']