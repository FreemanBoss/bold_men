from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from measurements.models import Measurement
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from measurements.forms import MeasurementForm

class MeasurementCreateView(CreateView):
    model = Measurement
    form_class = MeasurementForm
    success_url = reverse_lazy('accounts:profile')


    # after adding measurement, you cannot access this page unless for update
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        



# the form created is to add crispy style to it

class MeasurementUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Measurement
    form_class = MeasurementForm
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        obj, created = Measurement.objects.get_or_create(user=self.request.user)
        return obj
        

    # checks if there is a user logged in is the one filling the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


    def test_func(self):
        measurement = self.get_object()
        if self.request.user == measurement.user:
            return True
        return False


class MeasurementDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Measurement
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
          

class MeasurementListView(ListView):
    model = Measurement
    # template_name = 'measurements/order_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'measurements'
    # ordering = ['-updated_at']




class MeasurementDetailView(DetailView):
    model = Measurement


# Create your views here.
