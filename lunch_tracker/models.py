from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    account_number = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)


class Meal(models.Model):
    meal_name = models.CharField(max_length=50, default="default")
    allergens = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.meal_name)


class MenuChoice(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers')
    meal_name = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meals', default="default")
    meal_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='meals')
    quantity = models.IntegerField()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.meal_name)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()