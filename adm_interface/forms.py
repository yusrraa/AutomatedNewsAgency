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


class TextConfrForm(forms.ModelForm):

    class Meta:
        model = ArticleTextConfiguration
        fields = ('tag_name','attribute_name','scrape_type')
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name',
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
      
    def __init__(self, *args, **kwargs):
        super(TextConfrForm,self).__init__(*args, **kwargs)
        self.fields['scrape_type'].label = ""



class ImgConfrForm(forms.ModelForm):

    class Meta:
        model = ArticleImgConfiguration
        fields = ('tag_name','attribute_name','scrape_type')
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name',
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
      
    def __init__(self, *args, **kwargs):
        super(ImgConfrForm,self).__init__(*args, **kwargs)
        self.fields['scrape_type'].label = ""


class DateConfrForm(forms.ModelForm):

    class Meta:
        model = ArticlePublishDateConfiguration
        fields = ('tag_name','attribute_name','scrape_type')
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name',
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
      
    def __init__(self, *args, **kwargs):
        super(DateConfrForm,self).__init__(*args, **kwargs)
        self.fields['scrape_type'].label = ""




class HeadlineConfrForm(forms.ModelForm):

    class Meta:
        model = ArticleTopicHeadlineConfiguration
        fields = ('parent_tag_name', 'child_tag_name','attribute_name','scrape_type')
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'parent_tag_name': 'Parent Tag Name',
            'child_tag_name': 'Child Tag Name',
            'attribute_name': 'Attribute Name',
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
      
    def __init__(self, *args, **kwargs):
        super(HeadlineConfrForm,self).__init__(*args, **kwargs)
        self.fields['scrape_type'].label = ""




class URLConfrForm(forms.ModelForm):

    class Meta:
        model = ArticleUrlConfiguration
        fields = ('tag_name','attribute_name','scrape_type')
        widgets = {'scrape_type': forms.RadioSelect}
        labels = {
            'tag_name': 'Tag Name',
            'attribute_name': 'Attribute Name',
            }
        helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('scrape_type'),
            )
        helper.use_custom_control = True
      
    def __init__(self, *args, **kwargs):
        super(URLConfrForm,self).__init__(*args, **kwargs)
        self.fields['scrape_type'].label = ""














