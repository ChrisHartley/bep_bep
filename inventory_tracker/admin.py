from django.contrib import admin
from django.forms import BaseInlineFormSet, Textarea
from .models import Property, claim, status, photo

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

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('parcel','street_address','get_current_status')
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
                    ('originally_city_owned','originally_renew_owned','originally_county_surplus','originally_privately_owned', 'original_private_owner_name')
                )
            }
        ),
        ('Scoring Matrix', {
            'fields': ('scoring_matrix_complete',),

            }
        ),
        ('Public Notice', {
            'fields': (
                ('public_notice_complete','public_notice_date'),
                )
            }
        ),
        ('Clearance and Release',
            { 'fields':
                (
                    'landmarks_clearance_date',
                    ('preinspection_complete','preinspection_date'),
                    ('environmental_report_complete','environmental_report_submitted','environmental_report_received')
                )
            }
        ),
        ('Bidding', {
            'fields':
                (
                    ('bid_group','bid_date'),
                    ('contract_winner','contract_date')
                )
            }
        ),
        ('Quiet Title', {
            'fields':
                (
                    'quiet_title_status',
                    ('quiet_title_attorney','quiet_title_ordered_date')
                )
            }
        ),
        ('Demolished', {
            'fields':
                (
                    ('demolished','demolished_date','sold_date'),
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
        claimInline,
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

admin.site.register(Property, PropertyAdmin)
admin.site.register(claim)
admin.site.register(status)
admin.site.register(photo, PhotoAdmin)
