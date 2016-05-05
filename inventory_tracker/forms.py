from django import forms
import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div, Reset
from crispy_forms.bootstrap import FormActions


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
    all_quiet_on_eastern_front = AllValuesNoneFilter(name='quiet_title_status', label="All Quiet on the Eastern Front")

    class Meta:
        model = Property
        exclude = ['quiet_title_status']

class NewPropertySearchForm(forms.ModelForm):

    date_field = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
            )
        ),


    class Meta:
        model = Property
        # fields = [
        #     'parcel',
        #     'street_address',
        #     'on_ihcda_list',
        #     'scoring_matrix_complete',
        #     'bid_group',
        #     'bid_date',
        #     'bidder_awarded',
        #     'contract_date',
        #     'notes',
        #     'program_partner'
        #
        # ]
        exclude = []

    def __init__(self, *args, **kwargs):
        super(NewPropertySearchForm, self).__init__(*args, **kwargs)
        #self.fields['searchArea'].widget = HiddenInput()
        self.helper = FormHelper()
        self.helper.form_id = 'NewPropertySearchForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.render_unmentioned_fields = True

        self.helper.form_method = 'get'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Address and Parcel',
                Field('street_address'),
                Field('parcel'),
            ),
            Fieldset(
                'Site Control and Property Source',
                Field('site_control'),
                Field('interim_city_ownership'),
                Field('originally_renew_owned'),
                Field('originally_city_owned'),
                Field('originally_county_surplus'),
                Field('originally_tax_sale_unsold'),
                Field('originally_privately_owned'),
                Field('original_private_owner_name')


            ),
            Fieldset(
                'Scoring Matrix',
                Field('scoring_matrix_complete'),
                Field('on_ihcda_list'),
                Field('on_ihcda_list_date'),
            ),
            Fieldset(
                'Public Notice',
                Field('public_notice_complete'),
                Field('public_notice_date'),
            ),
            Fieldset(
                'Bidding',
                Field('bid_group'),
                Field('bid_date'),
                Field('bidder_awarded'),
                Field('contract_date'),
            ),
            Fieldset(
                'Demolished',
                Field('demolished'),
                Field('demolished_date')
            ),
            Fieldset(
                'Notes',
                Field('notes')

            ),
            FormActions(
                Submit('save', 'Search'),
                #Reset('reset', 'Reset'),
            ),
        )
