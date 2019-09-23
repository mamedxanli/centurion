# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from money.models import Money

#we need to add form validation here
class MoneyForm(ModelForm):
    class Meta:
        model = Money
        fields = ['date',
                  'amount',
                  'incoming',
                 ]
        widgets = {'date': forms.TextInput(attrs={'placeholder': 'Misal: 2018-12-31'})}