from django.conf.urls import include, url
from django.contrib import admin
from inventory_tracker import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bep_bep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.PropertyView.as_view(), name='fieldwork')
]
