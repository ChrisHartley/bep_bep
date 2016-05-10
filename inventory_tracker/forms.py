from django import forms
import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div, Reset
from crispy_forms.bootstrap import FormActions

from .models import Property, photo, ProgramPartner

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

    class Meta:
        model = Property
        exclude = []

    def __init__(self, *args, **kwargs):
        super(NewPropertySearchForm, self).__init__(*args, **kwargs)
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
                Field('program_partner'),
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
                'Add to BEP',
                Field('add_requested'),
                Field('add_requested_note'),
                Field('add_waiver_submitted'),
                Field('add_requested_date'),
            ),
            Fieldset(
                'Remove from BEP',
                Field('remove_requested'),
                Field('remove_requested_note'),
                Field('remove_waiver_submitted'),
                Field('remove_requested_date'),
            ),
            Fieldset(
                'Public Notice',
                Field('public_notice_complete'),
                Field('public_notice_date'),
            ),
            Fieldset(
                'Landmarks Review',
                Field('landmarks_response_date'),
                Field('landmarks_cleared'),
            ),
            Fieldset(
                'Bidding',
                Field('bid_group'),
                Field('bid_date'),
                Field('bidder_awarded'),
                Field('contract_date'),
            ),
            Fieldset(
                'Quiet Title',
                Field('quiet_title_complete'),
                Field('quiet_title_attorney'),
                Field('quiet_title_ordered_date'),

            ),
            Fieldset(
                'Demolished',
                Field('all_demolition_checklist_components_completed'),
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
