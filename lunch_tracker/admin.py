from django.contrib import admin

from .models import Customer, Meal, Event


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'role')
    list_filter = ( 'cust_name', )
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class MealList(admin.ModelAdmin):
    list_display = ( 'meal_name', 'date')
    list_filter = ( 'meal_name', 'date')
    search_fields = ('meal_name', 'date')
    ordering = ['meal_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Meal, MealList)
admin.site.register(Event)