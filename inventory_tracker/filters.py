import django_filters
from django.contrib.admin import widgets
from django.db import models
from .models import Property
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
    scoring_matrix_complete = django_filters.BooleanFilter(lookup_type='exact', label='Scoring matrix completed', help_text='')
    on_ihcda_list = django_filters.BooleanFilter(lookup_type='exact', label="On IHCDA's list", help_text="Listed on IHCDA's published list")

    bid_group = django_filters.CharFilter(lookup_type='icontains', label='Bid group', help_text='Case insentive text search, partial matching supported')
    bid_date = django_filters.DateFilter(label='Bid Date', help_text='Not sure how this works yet.')
    bidder_awarded = django_filters.CharFilter(lookup_type='icontains', label='Bidder awarded', help_text='Case insentive text search, partial matching supported')
    contract_date = django_filters.DateFilter(label='Contract date', help_text='Not sure how date searching works')


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
