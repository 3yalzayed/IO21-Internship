from django.forms import ModelForm
from .models import ContactUs

class ContactFrom(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'