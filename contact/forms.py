from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at', 'resolved')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes and aria labels remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }

        self.fields['name'].widget.attrs['aria-label'] = 'Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Email'
        self.fields['subject'].widget.attrs['aria-label'] = 'Subject'
        self.fields['message'].widget.attrs['aria-label'] = 'Message'

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
