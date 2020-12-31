from django import forms

class CreateNewBlogStorage(forms.Form):
    title = forms.CharField(label = 'title', max_length = 200)
    proceed = forms.BooleanField(required = False)
