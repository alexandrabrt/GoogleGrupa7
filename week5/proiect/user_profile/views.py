from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from user_profile.models import Pontaj


@login_required
def new_timesheet(request):
    Pontaj.objects.create(user_id=request.user.id,
                          start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id,
                          end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
