from django.db import models
from django.utils.text import slugify
from decimal import Decimal

class ProgramPartner(models.Model):
    name = models.CharField(max_length=255, blank=False)
    contact = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=True)
    email2 = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    mailing_address_1 = models.CharField(max_length=255, blank=True)
    mailing_address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

class Bidder(models.Model):
    name = models.CharField(max_length=255, blank=False)
    contact = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    email2 = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=False)
    mailing_address_1 = models.CharField(max_length=255, blank=True)
    mailing_address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class Property(models.Model):

    parcel = models.CharField(max_length=7, unique=True)
    street_address = models.CharField(max_length=255, unique=True)

    site_control = models.BooleanField(default=False, verbose_name="RI site control")
    dmd_site_control = models.BooleanField(default=False, verbose_name="DMD site control")
    mdc_resolution_boolean = models.BooleanField(default=False, verbose_name="MDC resolution")
    mdc_resolution_date = models.DateField(blank=True, null=True, verbose_name="Date of MDC resolution")

    originally_renew_owned = models.BooleanField(default=False)
    originally_city_owned = models.BooleanField(default=False)
    originally_county_surplus = models.BooleanField(default=False)
    originally_tax_sale_unsold = models.BooleanField(default=False)

    originally_privately_owned = models.BooleanField(default=False)
    original_private_owner_name = models.CharField(max_length=255, blank=True, null=False)
    original_private_owner_contact = models.CharField(verbose_name='Contact information for the private owner', max_length=1024, blank=True, null=False)
    private_owner_purchase_agreement_signed = models.DateField(verbose_name='Date purchase agreement signed by private owner', blank=True, null=True)


    on_ihcda_list = models.BooleanField(default=False, verbose_name='On IHCDA list')
    on_ihcda_list_date = models.DateField(blank=True, null=True, verbose_name='IHCDA list')

    AWARD_CHOICES = ((15000.00,15000.00),(25000.00,25000.00))
    award_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, choices=AWARD_CHOICES)

    add_requested = models.BooleanField(default=False)
    add_requested_note = models.CharField(max_length=255, blank=True)
    add_requested_date = models.DateField(blank=True, null=True)
    add_waiver_submitted = models.DateField(blank=True, null=True, verbose_name='Add Waiver')

    remove_requested = models.BooleanField(default=False)
    remove_requested_note = models.CharField(max_length=255, blank=True)
    remove_requested_date = models.DateField(blank=True, null=True)
    remove_waiver_submitted = models.DateField(blank=True, null=True)

    planned_end_use = models.CharField(max_length=512, blank=True)

    program_partner = models.ForeignKey(ProgramPartner, null=True, blank=True, default=6)

    scoring_matrix_complete = models.BooleanField(default=False)

    public_notice_complete = models.BooleanField(default=False)
    public_notice_date = models.DateField(blank=True, null=True, verbose_name='Public Notice')

    landmarks_response_date = models.DateField(blank=True, null=True)
    landmarks_cleared = models.NullBooleanField(default=None)

    preinspection_complete = models.BooleanField(default=False)
    preinspection_date = models.DateField(blank=True, null=True, verbose_name='Preinspection')
    preinspection_requested = models.BooleanField(default=False)

    #environmental_report_submitted = models.DateField(blank=True, null=True)
    environmental_report_received = models.DateField(blank=True, null=True, verbose_name='Environmental Report')
    environmental_report_requested = models.BooleanField(default=False)

    #environmental_report_complete = models.BooleanField(default=False)
    abatement_required = models.NullBooleanField(default=None)
    abatement_notice_to_proceed_given = models.DateField(blank=True, null=True, verbose_name='Abatement NTP')
    abatement_complete = models.DateField(blank=True, null=True, verbose_name='Visual Insp. Cert.')

    bid_date = models.DateField(blank=True, null=True)
    bid_group = models.CharField(max_length=25, blank=True)

    bidder_awarded = models.ForeignKey(Bidder, null=True, blank=True)
    contract_date = models.DateField(blank=True, null=True)
    notice_to_proceed_given = models.DateField(blank=True, null=True, verbose_name='Demolition NTP')


    demolished_date = models.DateField(blank=True, null=True, verbose_name='Invoice received')
    demolished = models.BooleanField(default=False)
    all_demolition_checklist_components_completed = models.BooleanField(default=False, verbose_name='All demolition checklist components completed')

    greening_form_submitted_date = models.DateField(blank=True, null=True, verbose_name='Date Greening Form submitted with claim')
    greening_form_accepted_date = models.DateField(blank=True, null=True, verbose_name='Date Greening Form approved by IHCDA')
    notes = models.CharField(max_length=512, blank=True)

    acquisition_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    environmental_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    demolition_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    closeout_completed_date = models.DateField(blank=True, null=True, verbose_name='Date closeout form submitted')
    mortgage_release_recorded_date = models.DateField(blank=True, null=True, verbose_name='Date mortgage release recorded')

    COMPLETE_STATUS = 1
    ORDERED_STATUS = 2
    NOT_COMPLETE_STATUS = 3

    QUIET_TITLE_STATUS_CHOICES = (
        (COMPLETE_STATUS,'Quiet Title Complete'),
        (ORDERED_STATUS,'Quiet Title Action Ordered'),
        (NOT_COMPLETE_STATUS,'No Quiet Title')
    )

    quiet_title_complete = models.BooleanField(default=False)
    quiet_title_required = models.BooleanField(default=False)
    quiet_title_attorney = models.CharField(max_length=255, blank=True)
    quiet_title_ordered_date = models.DateField(blank=True, null=True)

    POOL_4_0 = 4.0
    POOL_4_5 = 4.5
    POOL_UNKNOWN = 0

    IHCDA_GRANT_POOL_CHOICES = (
        (POOL_4_0,'4.0'),
        (POOL_4_5,'4.5'),
        #(POOL_UNKNOWN,'Unknown'),
    )

    ihcda_grant_pool = models.DecimalField(choices=IHCDA_GRANT_POOL_CHOICES, max_digits=2, decimal_places=1, default=None, blank=True, verbose_name='IHCDA Grant Pool', null=True)

    TIER_1 = Decimal(18000.00)
    TIER_2 = Decimal(25000.00)
    TIER_0 = Decimal(0)
    IHCDA_TIER_CHOICES = (
        (TIER_1, '$18k'),
        (TIER_2, '$25k'),
        (TIER_0, 'Unassigned'),
    )

    ihcda_tier = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    total_claimed_2019 = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    maintenance_year_one = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True,null=True, verbose_name='Year one claimed')
    maintenance_year_two = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Year two claimed', null=True)
    maintenance_year_three = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Year three claimed', null=True)
    claimed_since_2019 = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    unused_maintenance_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    sold = models.BooleanField(default=False)


    @property
    def last_status(self):
        return status.objects.filter(prop_id=self.id).order_by('date').latest('date')

    @property
    def total_cost(self):
        return (self.environmental_cost if self.environmental_cost else 0) + \
            (self.acquisition_cost if self.acquisition_cost else 0) + \
            (self.demolition_cost if self.demolition_cost else 0)


    class Meta:
        verbose_name_plural = "properties"

    def __unicode__(self):
        return '%s - %s' % (self.street_address, self.parcel)


class claim(models.Model):
    date = models.DateField(blank=False, null=False)
    claim_paid = models.BooleanField(default=False)
    claim_paid_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    claim_confirmation_number = models.CharField(max_length=25, blank=True)
    Properties = models.ManyToManyField(Property)

    def __unicode__(self):
        return '%s - %s' % (self.date, self.description)

class status(models.Model):

    ADD_REQUESTED_STATUS = 1 # some party has requested that the property be added to BEP
    ADD_REJECTED_STATUS =  2 # Renew Indianapolis rejected the request to add the property to BEP
    ADD_SUBMITTED_STATUS = 3 # Add request submitted to IHCDA

    IHCDA_ACCEPTED_STATUS = 4 # IHCDA added the property to BEP
    IHCDA_REJECTED_STATUS = 5 # IHCDA rejected the BEP add request

    REMOVE_REQUESTED_STATUS = 6 # some party has requested that the property be removed from BEP
    REMOVE_REJECTED_STATUS = 7 # Renew Indianapolis rejected the rqeuest to remove the property from BEP
    REMOVE_SUBMITED_STATUS = 8 # Remove request submitted to IHCDA
    REMOVE_COMPLETED_STATUS = 9 # removed

    STATUS_CHOICES = (
        (ADD_REQUESTED_STATUS, 'Some party has requested that the property be added to BEP'),
        (ADD_REJECTED_STATUS, 'Renew Indianapolis rejected the request to add the property to BEP'),
        (ADD_SUBMITTED_STATUS, 'Add request submitted to IHCDA'),
        (IHCDA_ACCEPTED_STATUS, 'IHCDA added the property to BEP'),
        (IHCDA_REJECTED_STATUS, 'IHCDA rejected the BEP add request'),
        (REMOVE_REQUESTED_STATUS, 'Some party has requested that the property be removed from BEP'),
        (REMOVE_REJECTED_STATUS, 'Renew Indianapolis rejected the request to remove the property from BEP'),
        (REMOVE_SUBMITED_STATUS, 'Remove request submitted to IHCDA'),
        (REMOVE_COMPLETED_STATUS, 'IHCDA removed the property from BEP'),
    )

    state = models.IntegerField(choices=STATUS_CHOICES, blank=False)
    note = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    prop = models.ForeignKey(Property, related_name='status')

    class Meta:
        verbose_name_plural = 'statuses'

    def __unicode__(self):
        return '%s - %s' % (self.get_state_display(), self.note)

def get_location(instance, filename):
    return '{0}/{1}/{2}'.format('photos',slugify(instance.prop), filename)

class PropertyProxy(Property):
    class Meta:
        proxy = True
        verbose_name = 'Property (from summary view)'
        verbose_name_plural = 'Summary View of Properties'

class PropertyCostProxy(Property):
    class Meta:
        proxy = True
        verbose_name = 'Property'
        verbose_name_plural = 'Cost View of Properties'

class PropertyMaintenanceCostProxy(Property):
    class Meta:
        proxy = True
        verbose_name = 'Property'
        verbose_name_plural = 'Maintenance Cost View of Properties'

class ReadOnlyPropertyProxy(PropertyProxy):
    class Meta:
        proxy = True
        verbose_name = 'Read Only Property'
        verbose_name_plural = 'Read Only Properties'


class photo(models.Model):
    description = models.CharField(max_length=1024, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    prop = models.ForeignKey(Property, related_name='photo')
    image = models.ImageField(upload_to=get_location)
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True
