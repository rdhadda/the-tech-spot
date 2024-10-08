from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'  # Use all fields from the Product model

    # custom image input
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with category choices 
        and custom styling for fields.

        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # Get category IDs and friendly names for dropdown choices
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Set category field choices
        self.fields['category'].choices = friendly_names
        # Apply custom styling to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'
        # Set aria-label for the image field
        self.fields['image'].widget.attrs[
            'aria-label'] = 'Select a Product Image'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review', 'rating']

    def clean_rating(self):
        """Validate the rating field to ensure it is between 0 and 5."""
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating must be between 0 and 5.")
        return rating

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, and aria labels, remove auto-generated
        labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review': 'Add Your Review Here',
            'rating': 'Rate Me Out Of 5',
        }

        for field_name, field in self.fields.items():
            # Set placeholder and class for each field
            field.widget.attrs['placeholder'] = placeholders.get(
                                                field_name, '')
            field.widget.attrs['class'] = 'border-blue rounded-0'
            field.label = False

        # Set aria-labels for accessibility
        self.fields['review'].widget.attrs['aria-label'] = 'Write A Review'
        self.fields['rating'].widget.attrs['aria-label'] = 'Add A Rating'
        # Set autofocus on the first field (review)
        self.fields['review'].widget.attrs['autofocus'] = True
