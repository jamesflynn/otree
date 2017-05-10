from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page
from .models import Constants
from django.conf import settings

class OptIn(Page):
    pass

class Demographics(Page):
    form_model = models.Player
    form_fields = ['yearBorn', 'gender']

class Household(Page):
    form_model = models.Player
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

class ThankYou(Page):
    pass

page_sequence = [
	OptIn,
    Demographics,
    Household,
	ThankYou
	]