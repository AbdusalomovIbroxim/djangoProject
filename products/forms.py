from django.forms import ModelForm
from products.models import Product


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'country', 'phone_number',
                  'tg_username']  # kiritilganlarini chiqaradi
        # exclude = ('author',)  # kiritilganlarini chiqarmidi
