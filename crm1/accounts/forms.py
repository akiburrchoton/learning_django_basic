from django.forms import ModelForm
from .models import Order


# This is another model like the models in models.py
class OrderForm(ModelForm):
    class Meta:
        model   = Order
        fields  = '__all__' # These are the fields which will be shown in the front end form
        