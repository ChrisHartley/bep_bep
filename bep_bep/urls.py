from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django_filters.views import FilterView
from inventory_tracker import views
from inventory_tracker.models import Property
from inventory_tracker.admin import admin_site

from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    # Examples:
    # url(r'^$', 'bep_bep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    url(r'^admin/', include(admin_site.urls)),
    url(r'^$', staff_member_required(views.PropertyView.as_view()), name='fieldwork'),
    url(r'^filter/', FilterView.as_view(model=Property)),
    url(r'^search/', staff_member_required(views.property_filter), name='filter'),
]
