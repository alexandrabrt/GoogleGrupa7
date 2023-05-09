from django.urls import path
from user_profile import views

app_name = 'userprofile'

urlpatterns = [
    path('start_timesheet/', views.new_timesheet, name='start_pontaj'),
    path('end_timesheet/', views.stop_timesheet, name='stop_pontaj'),
]
