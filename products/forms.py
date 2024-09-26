from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'  # Use all fields from the Product model

    # custom image input
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
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
