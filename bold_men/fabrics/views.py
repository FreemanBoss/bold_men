from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
        CreateView,
        DeleteView,
        DetailView,
        ListView,
        UpdateView
)
from fabrics.models import Fabric, FabricImage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from fabrics.forms import FabricForm, FabricImageForm 
# FabricImageFormSet

class FabricCreateView(CreateView):
    model = Fabric
    template_name = 'fabrics/fabric_form.html'
    success_url = reverse_lazy('fabrics:fabric-list')

    def get(self, request, *args, **kwargs):
        fabric_form = FabricForm()
        fabric_image_form = FabricImageForm()
        return render(request, self.template_name, {
            'fabric_form': fabric_form,
            'fabric_image_form':fabric_image_form
            })

    def post(self, request, *args, **kwargs):
        fabric_form = FabricForm(request.POST)
        fabric_image_form = FabricImageForm(request.POST, request.FILES)
        if fabric_form.is_valid():
            fabric = fabric_form.save()

            if request.FILES.getlist('image'):
                for image in request.FILES.getlist('image'):
                    FabricImage.objects.create(fabric=fabric, image=image)

            return redirect(self.success_url)
        return render(request, self.template_name, {
            'fabric_form': fabric_form,
            'fabric_image_form':fabric_image_form
            })



"""
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        data  = super().get_context_data(**kwargs)
        if self.request.POST:
            data['images'] = FabricImageFormSet(self.request.POST, self.request.FILES)
        else:
                data['fabric_image_form'] = FabricImageFormSet()
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()
        images = context['images']
        fabric = form.save()
        if images.is_valid():
            images.instance = fabric
            images.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        images = context['images']
        print(images)
        return self.render_to_response(self.get_context_data(form=form, images=images))
        
        

"""


# the form created is to add crispy style to it

class FabricUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Fabric
    template_name = 'fabrics/fabric_update.html'
    fields = ['name', 'description', 'price']

    # checks if there is a user logged in is the one filling the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class FabricDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Fabric
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
          

class FabricListView(ListView):
    model = Fabric
    # template_name = 'fabrics/order_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'fabrics'
    ordering = ['name']




class FabricDetailView(DetailView):
    model = Fabric
    template_name = 'fabrics/fabric_details.html'

