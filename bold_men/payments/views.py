from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from payments.models import Payment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from payments.forms import PaymentForm

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        



# the form created is to add crispy style to it

class PaymentUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Payment
    form_class = PaymentForm

    # checks if there is a user logged in is the one filling the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class PaymentDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Payment
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
          

class PaymentListView(ListView):
    model = Payment
    # template_name = 'payments/order_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'payments'
    # ordering = ['-updated_at']




class PaymentDetailView(DetailView):
    model = Payment


