from django.contrib import admin
from django.forms import BaseInlineFormSet, Textarea
from .models import Property, claim, status, photo, Bidder, ProgramPartner, PropertyProxy
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group



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




class PropertyOverviewAdmin(admin.ModelAdmin):
    model = PropertyProxy
    list_display = ('parcel','street_address', 'bid_group', 'add_waiver_submitted', 'on_ihcda_list_date', 'public_notice_date', 'preinspection_date', 'environmental_report_received', 'demolished_date' )
    ordering = ['-bid_group']


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('parcel','street_address','get_current_status','site_control','on_ihcda_list','bid_group','demolished')
    search_fields = ['parcel', 'street_address']
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
                    #'interim_city_ownership',
                    'program_partner',
                    'originally_city_owned',
                    'originally_renew_owned',
                    'originally_county_surplus',
                    'originally_tax_sale_unsold',
                    'originally_privately_owned',
                    'original_private_owner_name',
                    'planned_end_use',
                )
            }
        ),
        ('Scoring Matrix', {
            'fields': (
                'scoring_matrix_complete',
                'on_ihcda_list',
                'on_ihcda_list_date',
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
        #            'environmental_report_complete',
                    'environmental_report_received',
                    'abatement_required',
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
admin_site.register(claim)
admin_site.register(status)
admin_site.register(Bidder)
admin_site.register(ProgramPartner)
admin_site.register(photo, PhotoAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
