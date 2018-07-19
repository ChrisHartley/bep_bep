from django.contrib import admin
from django.forms import BaseInlineFormSet, Textarea
from .models import Property, claim, status, photo, Bidder, ProgramPartner, PropertyProxy, ReadOnlyPropertyProxy, PropertyCostProxy
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin, ExportMixin, ExportActionModelAdmin

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponseRedirect


def batch_update_view(model_admin, request, queryset, field_names):

        # removes all other fields from the django admin form for a model
    def remove_fields(form):
        for field in list(form.base_fields.keys()):
            if not field in field_names:
                del form.base_fields[field]
        return form

        # the return value is the form class, not the form class instance
    form_class = remove_fields(model_admin.get_form(request))

    if request.method == 'POST':
        form = form_class()

        # the view is already called via POST from the django admin changelist
        # here we have to distinguish between just showing the intermediary view via post
        # and actually confirming the bulk edits
        # for this there is a hidden field 'form-post' in the html template
        if 'form-post' in request.POST:
            form = form_class(request.POST)
            if form.is_valid():
                for item in queryset.all():
                    changed_list = []
                    for field_name in field_names:
                        if request.POST.get('{}_use'.format(field_name,)) == 'on':
                            setattr(item, field_name, form.cleaned_data[field_name])
                            changed_list.append(field_name)
                    if len(changed_list) > 0:
                        l = LogEntry(
                                    user=request.user,
                                    content_type=ContentType.objects.get_for_model(model_admin.model, for_concrete_model=False),
                                    object_id=item.pk,
                                    object_repr=unicode(item),
                                    action_flag=CHANGE,
                                    change_message = 'Changed {}'.format(', '.join(changed_list),),
                                    )
                        l.save()
                    item.save()
                model_admin.message_user(request, "Bulk updated {} records".format(queryset.count()))
                return HttpResponseRedirect(request.get_full_path())

        return render(
            request,
            'admin/batch_editing_intermediary.html',
            context={
                'form': form,
                'items': queryset,
                'fieldnames': field_names,
                'media': model_admin.media,
            }
        )




# thanks https://yuji.wordpress.com/2011/03/18/django-ordering-admin-modeladmin-inlines/
class OrderedFormSet(BaseInlineFormSet):
    def get_queryset(self):
        return super(OrderedFormSet, self).get_queryset().order_by('-date')

class claimInline(admin.TabularInline):
    model = claim
    extra = 1
    fields = ('claim_confirmation_number','description','amount','date','claim_paid','claim_paid_date')
    formset = OrderedFormSet


class statusInline(admin.TabularInline):
    model = status
    formset = OrderedFormSet
    extra = 1

# create view to show costs per property - acquistion, environmental, demolition

class PropertyBidGroupListFilter(admin.SimpleListFilter):
    title = 'Bid Group'
    parameter_name = 'bid_group'


    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        bid_groups = qs.distinct().values('bid_group')
        results = list()
        for group in bid_groups:
            g = group['bid_group'].split('.')[0]
            if g:
                results.append(g)
        for group in sorted(set(results)):
            yield(group,group)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(bid_group__startswith=self.value())
        return queryset

class PropertyAdmin(ExportActionModelAdmin):
    list_display = ('parcel','street_address','get_current_status','site_control','on_ihcda_list','bid_group','demolished')
    search_fields = ['parcel', 'street_address']
    actions = [custom_batch_editing__admin_action]
    #list_filter = ('site_control','quiet_title_status'),
    fieldsets = (
        (None, {
            'fields':
                (
                    'parcel',
                    'street_address'
                )
            }
        ),
        ('Ownership and Control', {
            'fields':
                (
                    'site_control',
                    'dmd_site_control',
                    'mdc_resolution_boolean',
                    'mdc_resolution_date',
                    #'interim_city_ownership',
                    'program_partner',
                    'originally_city_owned',
                    'originally_renew_owned',
                    'originally_county_surplus',
                    'originally_tax_sale_unsold',
                    'originally_privately_owned',
                    'original_private_owner_name',
                    'original_private_owner_contact',
                    'private_owner_purchase_agreement_signed',
                    'planned_end_use',
                )
            }
        ),
        ('Scoring Matrix', {
            'fields': (
                'scoring_matrix_complete',
                'on_ihcda_list',
                'on_ihcda_list_date',
                'award_amount',
                'add_requested',
                'add_requested_note',
                'add_requested_date',
                'add_waiver_submitted',
                'remove_requested',
                'remove_requested_note',
                'remove_requested_date',
                'remove_waiver_submitted',
                )
            }
        ),
        ('Public Notice', {
            'fields': (
                'public_notice_complete',
                'public_notice_date',
                )
            }
        ),
        ('Landmarks Review',
            { 'fields':
                (
                    'landmarks_response_date',
                    'landmarks_cleared',
                )
            }
        ),
        ('BLN Pre-inspection Report',
            { 'fields':
                (
                    'preinspection_requested',
                    'preinspection_complete',
                    'preinspection_date',
                )
            }
        ),

        ('Quiet Title', {
            'fields':
                (
                    'quiet_title_required',
                    'quiet_title_complete',
                    'quiet_title_attorney',
                    'quiet_title_ordered_date'
                )
            }
        ),
        ('Environmental Report', {
            'fields':
                (
                    'environmental_report_requested',
                    'environmental_report_received',
                    'abatement_required',
                    'abatement_notice_to_proceed_given',
                    'abatement_complete',
                    'environmental_cost',
                )
            }

        ),
        ('Bidding', {
            'fields':
                (
                    'bid_group',
                    'bid_date',
                    'bidder_awarded',
                    'contract_date',
                    'notice_to_proceed_given',
                )
            }
        ),
        ('Demolished', {
            'fields':
                (
                    'all_demolition_checklist_components_completed',
                    'demolished',
                    'demolished_date',
                    'demolition_cost',
                    'greening_form_submitted_date',
                    'greening_form_approved_date',
                    'ihcda_grant_pool',
                    'closeout_completed_date',
                    'mortgage_release_recorded_date',
                )
            }
        ),
        ('Notes',{
            'fields':
                (
                    'notes',
                )
            }
        ),
    )


    inlines = [
        statusInline,
        ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PropertyAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'notes':
            formfield.widget = Textarea(attrs=formfield.widget.attrs)
        return formfield

    def get_current_status(self, obj):
            return status.objects.filter(prop=obj).latest('timestamp')

class PropertyOverviewAdmin(PropertyAdmin):
    model = PropertyProxy
    list_display = ('parcel','street_address', 'bid_group', 'site_control', 'dmd_site_control', 'mdc_resolution_boolean', 'add_waiver_submitted', 'on_ihcda_list_date', 'public_notice_date', 'preinspection_date', 'environmental_report_received', 'abatement_required', 'abatement_notice_to_proceed_given', 'abatement_complete', 'notice_to_proceed_given', 'demolished_date', 'ihcda_grant_pool')
    ordering = ['-bid_group']

    list_filter = (PropertyBidGroupListFilter,)

class PropertyCostOverviewAdmin(PropertyAdmin):
    model = PropertyCostProxy
    list_display = ('parcel','street_address', 'bid_group', 'acquisition_cost', 'environmental_cost', 'demolition_cost', 'total_cost', 'award_amount')
    ordering = ['-bid_group']
    list_filter = (PropertyBidGroupListFilter,)


from read_only_admin.admin import ReadonlyAdmin
class ReadOnlyPropertyOverviewAdmin(PropertyOverviewAdmin, ReadonlyAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('prop','description','image_thumb','timestamp')
    fields = ( 'prop', ('image', 'image_thumb'), 'description','timestamp')
    readonly_fields = ('image_thumb','timestamp')

class CustomAdminSite(admin.AdminSite):
    site_header = "BepBep Inventory Administration"
    site_title = "BepBep - Renew Indianapolis"

admin_site = CustomAdminSite(name='bepbep_admin')
admin_site.register(Property, PropertyAdmin)
admin_site.register(PropertyProxy, PropertyOverviewAdmin)
admin_site.register(PropertyCostProxy, PropertyCostOverviewAdmin)
admin_site.register(ReadOnlyPropertyProxy, ReadOnlyPropertyOverviewAdmin)
admin_site.register(claim)
admin_site.register(status)
admin_site.register(Bidder)
admin_site.register(ProgramPartner)
admin_site.register(photo, PhotoAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
