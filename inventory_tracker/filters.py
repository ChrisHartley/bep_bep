import django_filters
from .models import Property

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Property
