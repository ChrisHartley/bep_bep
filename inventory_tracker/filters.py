import django_filters
from django.contrib.admin import widgets
from django.db import models
from .models import Property, Bidder, ProgramPartner
from .forms import PropertySearchForm, NewPropertySearchForm
from django.forms import forms

class InventoryFilter(django_filters.FilterSet):

#     django_filters.filters.LOOKUP_TYPES = [
#     ('', '---------'),
#     ('exact', 'Is equal to'),
#     ('not_exact', 'Is not equal to'),
#     ('lt', 'Lesser than'),
#     ('gt', 'Greater than'),
#     ('gte', 'Greater than or equal to'),
#     ('lte', 'Lesser than or equal to'),
#     ('startswith', 'Starts with'),
#     ('endswith', 'Ends with'),
#     ('contains', 'Contains'),
#     ('not_contains', 'Does not contain'),
# ]
#


    parcel = django_filters.CharFilter(lookup_expr='icontains', help_text='7 digit parcel number')
    street_address = django_filters.CharFilter(lookup_expr='icontains', help_text='Surpports partial matching')

    site_control = django_filters.BooleanFilter(label='Site Control', help_text='Renew Indianapolis or Program Partner has site control')
    dmd_site_control = django_filters.BooleanFilter(label='DMD Site Control', help_text='DMD has site control')

    #interim_city_ownership = django_filters.BooleanFilter(label='Interim city ownership', help_text='')
    originally_renew_owned = django_filters.BooleanFilter(label='Renew Indianapolis owned', help_text='')
    originally_city_owned = django_filters.BooleanFilter(label='City owned', help_text='')
    originally_county_surplus = django_filters.BooleanFilter(label='County Surplus', help_text='')
    originally_tax_sale_unsold = django_filters.BooleanFilter(label='2015 Tax Sale Unsold', help_text='')
    originally_privately_owned = django_filters.BooleanFilter(label='Privately Owned', help_text='')
    original_private_owner_name = django_filters.CharFilter(lookup_expr='icontains', label='Private owner name', help_text='')
    original_private_owner_contact = django_filters.CharFilter(lookup_expr='icontains', label='Private owner contact information', help_text='')
    #private_owner_purchase_agreement_signed = django_filters.BooleanFilter(label='Purchase agreement signed by private seller', help_text='')
    private_owner_purchase_agreement_signed_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), name='private_owner_purchase_agreement_signed', label='Date purchase agreement to sell signed', help_text='From - To')
    private_owner_purchase_agreement_signed_boolean = django_filters.BooleanFilter(method='filter_private_owner_purchase_agreement_signed_boolean', widget=django_filters.widgets.BooleanWidget(), label='Private owner purchase agreement to sell signed', help_text='')

    add_requested = django_filters.BooleanFilter(label='Property requested to be added to BEP', help_text='')
    add_requested_note = django_filters.CharFilter(lookup_expr='icontains', label='Add requested note', help_text='Case insentive text search, partial matching supported')
    add_requested_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date add requested', help_text='From - To')
#    add_waiver_submitted = django_filters.BooleanFilter(label='Waiver to add property submitted to IHCDA', help_text='')
    add_waiver_submitted_boolean = django_filters.BooleanFilter(method='filter_add_waiver_submitted', widget=django_filters.widgets.BooleanWidget(), label='Waiver to add property submitted to IHCDA', help_text='')

    remove_requested = django_filters.BooleanFilter(label='Property requested to be removed from BEP', help_text='')
    remove_requested_note = django_filters.CharFilter(lookup_expr='icontains', label='Remove requested note', help_text='Case insentive text search, partial matching supported')
    remove_requested_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date remove requested', help_text='From - To')
    #remove_waiver_submitted = django_filters.BooleanFilter(label='Waiver to remove property submitted to IHCDA', help_text='')
    remove_waiver_submitted = django_filters.BooleanFilter(method='filter_remove_waiver_submitted', widget=django_filters.widgets.BooleanWidget(), label='Waiver to remove property submitted to IHCDA', help_text='')

    scoring_matrix_complete = django_filters.BooleanFilter(lookup_expr='exact', label='Scoring matrix completed', help_text='')
    on_ihcda_list = django_filters.BooleanFilter(lookup_expr='exact', label="On IHCDA's list", help_text="")
    on_ihcda_list_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='List Date', help_text='From - To')

    public_notice_complete = django_filters.BooleanFilter(lookup_expr='exact', label="Public notice complete", help_text="")
    public_notice_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date notice published', help_text='From - To')

    quiet_title_complete = django_filters.BooleanFilter(lookup_expr='exact', label="Quiet Title complete", help_text="")
    quiet_title_required = django_filters.BooleanFilter(lookup_expr='exact', label="Quiet Title required", help_text="")

    quiet_title_attorney = django_filters.CharFilter(lookup_expr='icontains', label='Quiet title attorney', help_text='Case insentive text search, partial matching supported')
    quiet_title_ordered_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date quiet title action ordered', help_text='From - To')

    landmarks_response_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date of Landmarks\' response', help_text='From - To')
    landmarks_cleared = django_filters.BooleanFilter(lookup_expr='exact', label="Landmarks Cleared", help_text="")

    preinspection_complete = django_filters.BooleanFilter(lookup_expr='exact', label="BLN Pre-bid survey complete", help_text="")
    preinspection_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date pre-bid survey completed', help_text='From - To')


    environmental_report_received = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Environmental report received', help_text='From - To')
    #environmental_report_complete = django_filters.BooleanFilter(lookup_expr='exact', label="Environmental report complete", help_text="")
    abatement_required = django_filters.BooleanFilter(lookup_expr='exact', label="Abatement required", help_text="")
    abatement_complete = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date Visual Inspection Certification received', help_text='From - To')
    abatement_complete_boolean = django_filters.BooleanFilter(method='filter_abatement_complete_boolean', widget=django_filters.widgets.BooleanWidget(), label='Visual Inspection Certificate received', help_text='')

    bid_group = django_filters.CharFilter(lookup_expr='icontains', label='Bid group', help_text='Case insentive text search, partial matching supported')
    bid_group_entered = django_filters.BooleanFilter(method='filter_bid_group_entered', widget=django_filters.widgets.BooleanWidget(), help_text='', label='Bid group has been entered')
    bid_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Bid Date', help_text='From - To')
    bidder_awarded = django_filters.ModelChoiceFilter(queryset=Bidder.objects.all(), label='Bidder awarded', help_text='')
    contract_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Contract date', help_text='From - To')
    notice_to_proceed_given = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Notice to proceed date', help_text='From - To')
    notice_to_proceed_given_entered = django_filters.BooleanFilter(method='filter_notice_to_proceed_given_entered', widget=django_filters.widgets.BooleanWidget(), help_text='', label='Notice to Proceed has been entered')

    program_partner = django_filters.ModelChoiceFilter(queryset=ProgramPartner.objects.all(), label='Program Partner assigned', help_text='')

    demolished_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date demolished', help_text='From - To')
    demolished = django_filters.BooleanFilter(lookup_expr='exact', label="Demolished", help_text="")
    all_demolition_checklist_components_completed = django_filters.BooleanFilter(lookup_expr='exact', label="All demolition checklist components completed", help_text="")

    greening_form_submitted_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), label='Date Greening Form submitted with claim', help_text='From - To')
    greening_form_submitted = django_filters.BooleanFilter(method='filter_greening_form_submitted_date_entered', widget=django_filters.widgets.BooleanWidget(), label='Greening Form submitted', help_text='')


    notes = django_filters.CharFilter(lookup_expr='icontains', label='Notes', help_text='Case insentive text search, partial matching supported')
    planned_end_use = django_filters.CharFilter(lookup_expr='icontains', label='Planned end use', help_text='Case insentive text search, partial matching supported')


    # public_notice_date_1 = django_filters.DateFilter(name='public_notice_date', lookup_expr=['gt', 'lt'])
    # public_notice_date_2 = django_filters.DateFilter(name='public_notice_date', lookup_expr=['gt', 'lt'])

    #street_address = django_filters.CharFilter(lookup_expr='icontains')


    def filter_bid_group_entered(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                bid_group=u''
            )
        if value == True:
            return queryset.exclude(
                bid_group=u''
            )
        return queryset

    def filter_greening_form_submitted_date_entered(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                greening_form_submitted_date__isnull=True
            )
        if value == True:
            return queryset.exclude(
                greening_form_submitted_date__isnull=True
            )
        return queryset

    def filter_notice_to_proceed_given_entered(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                notice_to_proceed_given__isnull=True
            )
        if value == True:
            return queryset.exclude(
                notice_to_proceed_given__isnull=True
            )
        return queryset

    def filter_abatement_complete_boolean(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                abatement_complete__isnull=True
            )
        if value == True:
            return queryset.exclude(
                abatement_complete__isnull=True
            )
        return queryset

    def filter_remove_waiver_submitted(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                remove_waiver_submitted__isnull=True
            )
        if value == True:
            return queryset.exclude(
                remove_waiver_submitted__isnull=True
            )
        return queryset

    def filter_add_waiver_submitted(self, queryset, name, value):
        print "!!Value: {}".format(value,)
        if value == False:
            return queryset.filter(
                add_waiver_submitted__isnull=True
            )
        if value == True:
            return queryset.exclude(
                add_waiver_submitted__isnull=True
            )
        return queryset

    def filter_private_owner_purchase_agreement_signed_boolean(self, queryset, name, value):
        if value == False:
            return queryset.filter(
                private_owner_purchase_agreement_signed__isnull=True
            )
        if value == True:
            return queryset.exclude(
                private_owner_purchase_agreement_signed__isnull=True
            )
        return queryset



    class Meta:
        model = Property
        exclude = []
        form = NewPropertySearchForm
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
