from django import forms
import django_filters

from .models import Property, photo

class PropertyFieldworkForm(forms.ModelForm):
    class Meta:
        model = photo
        exclude = []
        fields = ['prop', 'image', 'description']

class AllValuesNoneFilter(django_filters.ChoiceFilter):

    @property
    def field(self):
        qs = self.model._default_manager.distinct()
        qs = qs.order_by(self.name).values_list(self.name, flat=True)
        self.extra['choices'] = [(o, o) for o in qs]
        self.extra['choices'].insert(0, ('', u'------',))
        return super(AllValuesNoneFilter, self).field

class PropertySearchForm(forms.ModelForm):
    quiet_title_status = AllValuesNoneFilter(name='quiet_title_status', label="Quiet Title Status")

    class Meta:
        model = Property
        exclude = []
