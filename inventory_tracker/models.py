from django.db import models
from django.utils.text import slugify

class Property(models.Model):

    parcel = models.CharField(max_length=7)
    street_address = models.CharField(max_length=255)

    site_control = models.BooleanField(default=False)

    originally_renew_owned = models.BooleanField(default=False)
    originally_county_surplus = models.BooleanField(default=False)
    originally_privately_owned = models.BooleanField(default=False)
    original_private_owner_name = models.CharField(max_length=255, blank=True, null=False)

    public_notice_complete = models.BooleanField(default=False)
    public_notice_date = models.DateField(blank=True, null=True)

    landmarks_clearance_date = models.DateField(blank=True, null=True)

    preinspection_complete = models.BooleanField(default=False)
    preinspection_date = models.DateField(blank=True, null=True)

    environmental_report_submitted = models.DateField(blank=True, null=True)
    environmental_report_received = models.DateField(blank=True, null=True)
    environmental_report_complete = models.BooleanField(default=False)

    bid_date = models.DateField(blank=True, null=True)
    bid_group = models.CharField(max_length=25, blank=True)

    contract_winner = models.CharField(max_length=255, blank=True)
    contract_date = models.DateField(blank=True, null=True)

    demolished_date = models.DateField(blank=True, null=True)
    demolished = models.BooleanField(default=False)

    sold_date = models.DateField(blank=True, null=True)

    notes = models.CharField(max_length=512, blank=True)

    COMPLETE_STATUS = 1
    ORDERED_STATUS = 2
    NOT_COMPLETE_STATUS = 3

    QUIET_TITLE_STATUS_CHOICES = (
        (COMPLETE_STATUS,'Quiet Title Complete'),
        (ORDERED_STATUS,'Quiet Title Action Ordered'),
        (NOT_COMPLETE_STATUS,'No Quiet Title')
    )

    quiet_title_status = models.IntegerField(choices=QUIET_TITLE_STATUS_CHOICES, default=NOT_COMPLETE_STATUS)
    quiet_title_attorney = models.CharField(max_length=255, blank=True)
    quiet_title_ordered_date = models.DateField(blank=True, null=True)

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

    STATUS_CHOICES = (
        (ADD_REQUESTED_STATUS, 'Some party has requested that the property be added to BEP'),
        (ADD_REJECTED_STATUS, 'Renew Indianapolis rejected the request to add the property to BEP'),
        (ADD_SUBMITTED_STATUS, 'Add request submitted to IHCDA'),
        (IHCDA_ACCEPTED_STATUS, 'IHCDA added the property to BEP'),
        (IHCDA_REJECTED_STATUS, 'IHCDA rejected the BEP add request'),
        (REMOVE_REQUESTED_STATUS, 'Some party has requested that the property be removed from BEP'),
        (REMOVE_REJECTED_STATUS, 'Renew Indianapolis rejected the rqeuest to remove the property from BEP'),
        (REMOVE_SUBMITED_STATUS, 'Remove request submitted to IHCDA')
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
