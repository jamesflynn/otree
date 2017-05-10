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

author = 'James Flynn'

doc = """
Transcription Negotiation
"""

class Constants(BaseConstants):
    name_in_url = 'trx_survey'
    players_per_group = 128
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass

P1_CHOICES = (('3','$3 each ($15 for all 5 pages)'),('2','$2 each ($10)'))
P2_CHOICES = (('4','$4 each ($20 for all 5 pages)'),('2','$2 each ($10)'))
P3_CHOICES = (('5','$5 each ($25 for all 5 pages)'),('2','$2 each ($10)'))
P4_CHOICES = (('6','$6 each ($30 for all 5 pages)'),('2','$2 each ($10)'))
P5_CHOICES = (('7','$7 each ($35 for all 5 pages)'),('2','$2 each ($10)'))

class Player(BasePlayer):
    howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
    bid = models.CurrencyField()
    pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
    pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
    pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
    pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
    pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))

