from django.shortcuts import render
from .models import *
from .forms import *
from .utils import Calendar
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

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
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month