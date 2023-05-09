from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie1.models import Location, AuditLocation


# Create your views here.
class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'
    paginate_by = 5
    queryset = model.objects.all().order_by('id')

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data['page'] = self.request.GET.get('page') if self.request.GET.get('page') else 1
        return data



class CreateLocationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'
    permission_required = 'user_profile.add_pontaj'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


@login_required
def delete_location(request, pk):
    location_value = Location.objects.get(id=pk)
    AuditLocation.objects.create(location=location_value.id,
                                 city=location_value.city,
                                 country=location_value.country,
                                 active=location_value.active,
                                 user_id=request.user.id)
    Location.objects.filter(id=pk).delete()
    return redirect(f'/locations/?page={request.GET.get("page")}')


@login_required
def deactivate_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect(f'/locations/?page={request.GET.get("page")}')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect(f'/locations/?page={request.GET.get("page")}')
