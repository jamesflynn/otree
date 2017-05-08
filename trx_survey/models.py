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
    players_per_group = 16
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass

class Player(BasePlayer):
	howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
	bid = models.CurrencyField()

