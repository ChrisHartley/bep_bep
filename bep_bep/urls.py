from django.conf.urls import include, url
from django.contrib import admin
from inventory_tracker import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    # Examples:
    # url(r'^$', 'bep_bep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', staff_member_required(views.PropertyView.as_view()), name='fieldwork')
]
