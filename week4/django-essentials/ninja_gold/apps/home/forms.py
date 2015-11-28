from django import forms

class farmForm(forms.Form):
    hidden = forms.CharField(widget = forms.HiddenInput(), initial='farm')

class caveForm(forms.Form):
    hidden = forms.CharField(widget = forms.HiddenInput(), initial='cave')

class houseForm(forms.Form):
    hidden = forms.CharField(widget = forms.HiddenInput(), initial='house')

class casinoForm(forms.Form):
    hidden = forms.CharField(widget = forms.HiddenInput(), initial='casino')

