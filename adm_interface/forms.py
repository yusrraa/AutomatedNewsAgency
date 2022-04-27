from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineRadios


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
        3




class TextConfiguraton(forms.ModelForm):
    class Meta:
        model = ArticleTextConfiguration
        fields = "__all__"
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name'
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
