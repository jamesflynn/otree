from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import random

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s is not an acceptable answer'),
            params={'value': value},
        )

def validate_nonfalse(value):
    if value == False:
        raise ValidationError(
            _('Please consent to continue'),
            params={'value': value},
        )

author = 'Zoe Cullen'

doc = """
Transcription Negotiation
"""

class Constants(BaseConstants):
    name_in_url = 'trx_survey'
    players_per_group = None
    num_rounds = 1
    tax_max = 4
    tax_min = 2

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass

P1_CHOICES = (('3','$15, for 5 pages transcribed ($3 per page, 95% accuracy)'),('2','$9, no transcription required '))
P2_CHOICES = (('4','$20, for 5 pages transcribed ($4 per page, 95% accuracy)'),('2','$9, no transcription required '))
P3_CHOICES = (('5','$25, for 5 pages transcribed ($5 per page, 95% accuracy)'),('2','$9, no transcription required '))
P4_CHOICES = (('6','$30, for 5 pages transcribed ($6 per page, 95% accuracy)'),('2','$9, no transcription required '))
P5_CHOICES = (('7','$35, for 5 pages transcribed ($7 per page, 95% accuracy)'),('2','$9, no transcription required '))


class Player(BasePlayer):
#    howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.Slider(attrs={'step': '5'}))
    bid = models.CurrencyField()
    tax = models.CurrencyField()
    consent = models.BooleanField(validators=[validate_nonfalse],widget= widgets.CheckboxInput(),default=False)
#    pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
#    pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
#    pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
#    pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
#    pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))

