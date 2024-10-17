from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from orders.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from orders.forms import OrderForm

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        



# the form created is to add crispy style to it

class OrderUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Order
    form_class = OrderForm

    # checks if there is a user logged in is the one filling the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class OrderDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Order
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
          

class OrderListView(ListView):
    model = Order
    # template_name = 'orders/order_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'orders'
    ordering = ['-updated_at']




class OrderDetailView(DetailView):
    model = Order
