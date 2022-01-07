from django import forms
from .models import tb1_master_domain

class DomainForm(forms.ModelForm):

    class Meta:
        model = tb1_master_domain
        fields ="__all__"
        labels = {
            'domain_name': 'Domain Name'
        }

