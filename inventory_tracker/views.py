from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.admin.views.decorators import staff_member_required

from .models import photo, Property, claim, status
from .forms import PropertyFieldworkForm

@staff_member_required
class PropertyView(SuccessMessageMixin, FormView):
    template_name = 'photo_form.html'
    form_class = PropertyFieldworkForm
    success_url = '/'
    success_message = "%(prop)s image saved."

    def form_valid(self, form):
        form.save()
        return super(PropertyView, self).form_valid(form)
