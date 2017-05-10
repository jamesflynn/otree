from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

author = 'James Flynn'

doc = """
Transcription Exit Survey
"""

class Constants(BaseConstants):
    name_in_url = 'exit_survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass


GENDER_CHOICES = (('','please select'),('m','male'),('f','female'),('o','other'),('opt_out','I\'d rather not say'))
EXP_CHOICES = (('','please select'),('none','no experience'),('some','some experience'),('very','very experienced'),('opt_out','I\'d rather not say'))
TRANS_CHOICES = (('','please select'),('none','no experience') , ('some','some experience') , ('very','very experienced') , ('opt_out','I\'d rather not say'))
EDU_CHOICES = (('','please select'),('someHS','some high school'),('HS','completed high school'),('someColl','some college'),('undergrad','undergrad degree'),('postgrad','graduate degree'),('opt_out','I\'d rather not say'))

class Player(BasePlayer):

	yearBorn = models.PositiveIntegerField(min=1916, max=2005)
	gender = models.CharField(widget=widgets.Select(choices=GENDER_CHOICES))
	experience = models.CharField(widget=widgets.Select(choices=EXP_CHOICES))
	transExp = models.CharField(widget=widgets.Select(choices=TRANS_CHOICES))
	eduLevel = models.CharField(widget=widgets.Select(choices=EDU_CHOICES))
	dailyHHEarn = models.CurrencyField()

