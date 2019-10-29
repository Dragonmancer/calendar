from django.shortcuts import render
from .models import *
from .forms import *
from .utils import Calendar
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

def customer_main(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'lunch_tracker/customer_main.html',
                  {'customers': customer})


def edit_account(request):
    return render(request, 'lunch_tracker/edit_account.html',)


def faq(request):
    return render(request, 'lunch_tracker/faq.html',)


def login(request):
    return render(request, 'lunch_tracker/login.html',)


def logout(request):
    return render(request, 'lunch_tracker/logout.html',)


def meal_list(request):
    meal = Meal.objects.filter(created_date__lte=timezone.now())
    return render(request, 'lunch_tracker/meal_list.html',
                  {'meals': meal})


def password_reset(request):
    return render(request, 'lunch_tracker/password_reset.html',)


def sign_up(request):
    return render(request, 'lunch_tracker/sign_up.html',)


def staff_main(request):
    return render(request, 'lunch_tracker/staff_main.html',)

class CalendarView(generic.ListView):
    model = Event
    template_name = 'lunch_tracker/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()