from django import forms
from .models import *

class DomainForm(forms.ModelForm):

    class Meta:
        model = Category
        fields ="__all__"
        labels = {
            'name': 'Domain Name'
        }

class URLform(forms.ModelForm):

    class Meta:
        model = DomainUrl
        fields = ('category','url')     ##*****Include is active here later........
        labels = {
            'category': 'Domain Name',
            'url': 'URL'
            }

    def __init__(self, *args, **kwargs):
        super(URLform,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Domain"



class TextConfiguraton(forms.ModelForm):

    class Meta:
        model = ArticleTextConfiguration
        fields = {'tag_name','attribute_name'}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name'
            }



