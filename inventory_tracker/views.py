from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from .models import photo, Property, claim, status
from .forms import PropertyFieldworkForm
from .filters import InventoryFilter

def property_filter(request):
    f = InventoryFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'inventory_tracker/property_filter.html', {'filter': f})

class PropertyView(SuccessMessageMixin, FormView):
    template_name = 'photo_form.html'
    form_class = PropertyFieldworkForm
    success_url = '/'
    success_message = "%(prop)s image saved."

    def form_valid(self, form):
        form.save()
        return super(PropertyView, self).form_valid(form)
