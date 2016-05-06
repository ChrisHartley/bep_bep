import django_filters
from django.contrib.admin import widgets
from django.db import models
from .models import Property, Bidder, ProgramPartner
from .forms import PropertySearchForm, NewPropertySearchForm
from django.forms import forms

class InventoryFilter(django_filters.FilterSet):

    django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('not_contains', 'Does not contain'),
]



    parcel = django_filters.CharFilter(lookup_type='icontains', help_text='7 digit parcel number')
    street_address = django_filters.CharFilter(lookup_type='icontains', help_text='Surpports partial matching')

    site_control = django_filters.BooleanFilter(label='Site Control', help_text='Renew Indianapolis or Program Partner has site control')
    interim_city_ownership = django_filters.BooleanFilter(label='Interim city ownership', help_text='')
    originally_renew_owned = django_filters.BooleanFilter(label='Renew Indianapolis owned', help_text='')
    originally_city_owned = django_filters.BooleanFilter(label='City owned', help_text='')
    originally_county_surplus = django_filters.BooleanFilter(label='County Surplus', help_text='')
    originally_tax_sale_unsold = django_filters.BooleanFilter(label='2015 Tax Sale Unsold', help_text='')
    originally_privately_owned = django_filters.BooleanFilter(label='Privately Owned', help_text='')
    original_private_owner_name = django_filters.CharFilter(lookup_type='icontains', label='Private owner name', help_text='')



    scoring_matrix_complete = django_filters.BooleanFilter(lookup_type='exact', label='Scoring matrix completed', help_text='')
    on_ihcda_list = django_filters.BooleanFilter(lookup_type='exact', label="On IHCDA's list", help_text="")
    on_ihcda_list_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='List Date', help_text='YYYY-MM-DD')

    public_notice_complete = django_filters.BooleanFilter(lookup_type='exact', label="Public notice complete", help_text="")
    public_notice_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='Date notice published', help_text='YYYY-MM-DD')

    quiet_title_complete = django_filters.BooleanFilter(lookup_type='exact', label="Quiet Title complete", help_text="")
    quiet_title_attorney = django_filters.CharFilter(lookup_type='icontains', label='Quiet title attorney', help_text='Case insentive text search, partial matching supported')
    quiet_title_ordered_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='Date quiet title action ordered', help_text='YYYY-MM-DD')


    bid_group = django_filters.CharFilter(lookup_type='icontains', label='Bid group', help_text='Case insentive text search, partial matching supported')
    bid_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='Bid Date', help_text='YYYY-MM-DD')
    bidder_awarded = django_filters.ModelChoiceFilter(queryset=Bidder.objects.all(), label='Bidder awarded', help_text='')
    contract_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='Contract date', help_text='YYYY-MM-DD')

    program_partner = django_filters.ModelChoiceFilter(queryset=ProgramPartner.objects.all(), label='Program Partner assigned', help_text='')

    demolished_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}), label='Date demolished', help_text='YYYY-MM-DD')
    demolished = django_filters.BooleanFilter(lookup_type='exact', label="Demolished", help_text="")

    notes = django_filters.CharFilter(lookup_type='icontains', label='Notes', help_text='Case insentive text search, partial matching supported')



    # public_notice_date_1 = django_filters.DateFilter(name='public_notice_date', lookup_expr=['gt', 'lt'])
    # public_notice_date_2 = django_filters.DateFilter(name='public_notice_date', lookup_expr=['gt', 'lt'])

    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_expr': 'icontains',
            },
        },
        # models.DateField: {
        #     'filter_class': django_filters.DateFilter,
        #      'extra': lambda f: {
        #          'widget': 'forms.DateInput(format="%Y-%m-%d")',
        #          },
        #
        #        },
    }
    #street_address = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
#        model = Property
        #fields = ['street_address']
        form = NewPropertySearchForm
#        exclude = ['quiet_title_status']
        #order_by = True
#        fields = {
#            'parcel': ['icontains'],
#            'street_address': ['icontains'],
#            'scoring_matrix_complete': ['exact'],
#            'notes': ['icontains'],
#            'public_notice_date': ['gt', 'lt', 'isnull'],
    #         'landmarks_clearance_date': ['gt', 'lt', 'isnull'],
    #         'preinspection_date': ['gt', 'lt', 'isnull'],
    #         'environmental_report_received': ['gt', 'lt', 'isnull'],
    #         'abatement_complete': ['gt', 'lt', 'isnull'],
    #         'bid_date': ['gt', 'lt', 'isnull'],
    #         'contract_date': ['gt', 'lt', 'isnull'],
    #         'demolished_date': ['gt', 'lt', 'isnull'],
    #         'quiet_title_ordered_date': ['gt', 'lt', 'isnull'],
    #         'site_control': ['exact'],
    #         'interim_city_ownership': ['exact'],
    #         'originally_renew_owned': ['exact'],
    #         'originally_city_owned': ['exact'],
    #         'originally_county_surplus': ['exact'],
    #         'originally_tax_sale_unsold': ['exact'],
    #         'originally_privately_owned': ['exact'],
    #         'original_private_owner_name': ['icontains'],
    #   }
