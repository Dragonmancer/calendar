from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'lunch_tracker'
urlpatterns = [
    path('', views.login, name='login'),
    path('customer_main', views.customer_main, name='customer_main'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('faq', views.faq, name='faq'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    # path('customer/<int:lpk>/edit/', views.customer_edit, name='customer_edit'),
    # path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    # path('meal_list', views.meal_list, name='meal_list'),
    # path('meal/create/', views.meal_new, name='meal_new'),
    # path('meal/<int:pk>/edit/', views.meal_edit, name='meal_edit'),
    # path('meal/<int:pk>/delete/', views.meal_delete, name='meal_delete'),
    # path('customer/<int:pk>/summary/', views.summary, name='summary'),
]
