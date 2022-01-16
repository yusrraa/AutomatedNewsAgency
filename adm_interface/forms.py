from django import forms
from .models import *

class DomainForm(forms.ModelForm):

    class Meta:
        model = tb1_master_domain
        fields ="__all__"
        labels = {
            'domain_name': 'Domain Name'
        }

class URLform(forms.ModelForm):

    class Meta:
        model = tb2_Url_details_table
        fields = ('domain','url_string')
        labels = {
            'domain': 'Domain Name',
            'url_string': 'URL'
            }

    def __init__(self, *args, **kwargs):
        super(URLform,self).__init__(*args, **kwargs)
        self.fields['domain'].empty_label = "Select Domain"
