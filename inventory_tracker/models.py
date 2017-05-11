from django.db import models
from django.utils.text import slugify

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

    site_control = models.BooleanField(default=False, verbose_name="Renew Indianapolis site control")

    originally_renew_owned = models.BooleanField(default=False)
    originally_city_owned = models.BooleanField(default=False)
    originally_county_surplus = models.BooleanField(default=False)
    originally_tax_sale_unsold = models.BooleanField(default=False)

    originally_privately_owned = models.BooleanField(default=False)
    original_private_owner_name = models.CharField(max_length=255, blank=True, null=False)

    on_ihcda_list = models.BooleanField(default=False, verbose_name='On IHCDA list')
    on_ihcda_list_date = models.DateField(blank=True, null=True, verbose_name='IHCDA list date')

    add_requested = models.BooleanField(default=False)
    add_requested_note = models.CharField(max_length=255, blank=True)
    add_requested_date = models.DateField(blank=True, null=True)
    add_waiver_submitted = models.DateField(blank=True, null=True)

    remove_requested = models.BooleanField(default=False)
    remove_requested_note = models.CharField(max_length=255, blank=True)
    remove_requested_date = models.DateField(blank=True, null=True)
    remove_waiver_submitted = models.DateField(blank=True, null=True)

    planned_end_use = models.CharField(max_length=512, blank=True)

    program_partner = models.ForeignKey(ProgramPartner, null=True, blank=True, default=6)

    scoring_matrix_complete = models.BooleanField(default=False)

    public_notice_complete = models.BooleanField(default=False)
    public_notice_date = models.DateField(blank=True, null=True)

    landmarks_response_date = models.DateField(blank=True, null=True)
    landmarks_cleared = models.NullBooleanField(default=None)

    preinspection_complete = models.BooleanField(default=False)
    preinspection_date = models.DateField(blank=True, null=True)

    #environmental_report_submitted = models.DateField(blank=True, null=True)
    environmental_report_received = models.DateField(blank=True, null=True)
    #environmental_report_complete = models.BooleanField(default=False)
    abatement_required = models.NullBooleanField(default=None)
    abatement_complete = models.DateField(blank=True, null=True, verbose_name='Visual Inspection Certification')

    bid_date = models.DateField(blank=True, null=True)
    bid_group = models.CharField(max_length=25, blank=True)

    bidder_awarded = models.ForeignKey(Bidder, null=True, blank=True)
    contract_date = models.DateField(blank=True, null=True)
    notice_to_proceed_given = models.DateField(blank=True, null=True, verbose_name='Date notice to proceed given')


    demolished_date = models.DateField(blank=True, null=True, verbose_name='Invoice received date')
    demolished = models.BooleanField(default=False)
    all_demolition_checklist_components_completed = models.BooleanField(default=False, verbose_name='All demolition checklist components completed')

    greening_form_submitted_date = models.DateField(blank=True, null=True, verbose_name='Date Greening Form submitted with claim')
    notes = models.CharField(max_length=512, blank=True)

    demolition_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    COMPLETE_STATUS = 1
    ORDERED_STATUS = 2
    NOT_COMPLETE_STATUS = 3

    QUIET_TITLE_STATUS_CHOICES = (
        (COMPLETE_STATUS,'Quiet Title Complete'),
        (ORDERED_STATUS,'Quiet Title Action Ordered'),
        (NOT_COMPLETE_STATUS,'No Quiet Title')
    )

    quiet_title_complete = models.BooleanField(default=False)
    quiet_title_attorney = models.CharField(max_length=255, blank=True)
    quiet_title_ordered_date = models.DateField(blank=True, null=True)

    @property
    def last_status(self):
        return status.objects.filter(prop_id=self.id).order_by('date').latest('date')

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
    prop = models.ForeignKey(Property)

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

class photo(models.Model):
    description = models.CharField(max_length=1024, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    prop = models.ForeignKey(Property, related_name='photo')
    image = models.ImageField(upload_to=get_location)
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True
