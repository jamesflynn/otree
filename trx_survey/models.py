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

GENDER_CHOICES = (('','please select'),('m','male'),('f','female'),('o','other'))
EXP_CHOICES = (('','please select'),('0','no experience'),('12','1-12 months'),('24','1-2 years'),('36','more than 2 years'))
TRANS_CHOICES = (('','please select'),('0','no experience') , ('12','1-12 months') , ('24','1-2 years') , ('36','more than 2 years') )
EDU_CHOICES = (('','please select'),('someHS','some high school'),('HS','completed high school'),('someColl','some college'),('undergrad','undergrad degree'),('postgrad','graduate degree'))
#COUNTRY_CHOICES = (('','please select'),('china','China'),('usa','USA'),('india','India'),('other','Not Listed'))
P1_CHOICES = (('3','$3 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P2_CHOICES = (('4','$4 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P3_CHOICES = (('5','$5 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P4_CHOICES = (('6','$6 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P5_CHOICES = (('7','$7 each page for up to five pages of transcription'),('2','$2 only, without transcription'))

class Player(BasePlayer):

	devSkip = models.BooleanField(blank=True)
	paymentOK = models.BooleanField()
	neverWorked = models.BooleanField()
	yearBorn = models.PositiveIntegerField(min=1916, max=2005)
	gender = models.CharField(widget=widgets.Select(choices=GENDER_CHOICES))
#	country = models.CharField(widget=widgets.Select(choices=COUNTRY_CHOICES))
	experience = models.CharField(widget=widgets.Select(choices=EXP_CHOICES))
	transExp = models.CharField(widget=widgets.Select(choices=TRANS_CHOICES))
	eduLevel = models.CharField(widget=widgets.Select(choices=EDU_CHOICES))
	dailyHHEarn = models.CurrencyField()
	howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
	pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
	pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
	pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
	pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
	pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))
	bid = models.CurrencyField()

