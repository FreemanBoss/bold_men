from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from contracts.models import Contract
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from contracts.forms import ContractForm

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        



# the form created is to add crispy style to it

class ContractUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Contract
    form_class = ContractForm

    # checks if there is a user logged in is the one filling the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class ContractDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Contract
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
          

class ContractListView(ListView):
    model = Contract
    # template_name = 'contracts/order_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'contracts'
    # ordering = ['-updated_at']




class ContractDetailView(DetailView):
    model = Contract


