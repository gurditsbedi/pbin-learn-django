from django import forms
from django.core.validators import RegexValidator

class pasteForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Untitled',
                                                         'class': 'form-control'
                                                        }),
                           max_length=30,
                           required=False)
    slug = forms.CharField(required=False,
                           validators=[
                                RegexValidator(
                                    regex='^($|[a-zA-Z0-9]{5,30}$)',
                                    message='Shoud be empty or have more than '
                                            '4 chars with no spaces'
                                )
                           ],
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'pattern': '^($|[a-zA-Z0-9]{5,30}$)',
                                                         'title': 'Shoud be empty or have more than '
                                                                  '4 chars with no spaces'
                                                        }
                                                  )
                           )

    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

