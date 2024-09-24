from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = [
            'default_full_name',
            'default_phone_number',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_street_address2',
            'default_county',
            'default_country'
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Post Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_full_name'].widget.attrs['aria-label'] = (
            'Full Name'
        )
        self.fields['default_phone_number'].widget.attrs['aria-label'] = (
            'Phone Number'
        )
        self.fields['default_postcode'].widget.attrs['aria-label'] = (
            'Post Code'
        )
        self.fields['default_town_or_city'].widget.attrs['aria-label'] = (
            'Town or City'
        )
        self.fields['default_street_address1'].widget.attrs['aria-label'] = (
            'Street Address 1'
        )
        self.fields['default_street_address2'].widget.attrs['aria-label'] = (
            'Street Address 2'
        )
        self.fields['default_county'].widget.attrs['aria-label'] = (
            'County'
        )

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-blue rounded-0 profile-form-input'
            )
            self.fields[field].label = False
        self.fields['default_country'].label = False