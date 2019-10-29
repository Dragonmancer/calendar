from django import forms
from .models import Customer, Meal


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'role')


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('meal_name', 'date', 'allergens')